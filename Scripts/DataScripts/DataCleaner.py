import numpy
import pandas
from datetime import datetime
import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger

class DataCleaner:
	dtype_dict = {
		"AppID" : "int64",
		"Name" : "str",
		"Release date": "str",
		"Estimated owners": "str", 
		"Peak CCU": "int64",
		"age": "int64",
		"Price": "float64",
		"DLC count": "int64",
		"About the game": "str",
		"Supported languages": "str",
		"Full audio languages": "str",
		"Reviews": "str",
		"Header image": "str",
		"Website": "str",
		"Support url": "str",
		"Support email": "str",
		"Windows": "bool",
		"Mac": "bool",
		"Linux": "bool",
		"Metacritic": "int64",
		"Metacritic url": "str",
		"User score": "int64",
		"Positive": "int64",
		"Negative": "int64",
		"Score rank": "str",
		"Achievements": "str",
		"Recommendations": "str",
		"Notes": "str",
		"Average playtime forever": "int64",
		"Average playtime two weeks": "int64",
		"Median playtime forever": "int64",
		"Median playtime two weeks": "int64",
		"Developer": "str",
		"Publisher": "str",
		"Categories": "str",
		"Genres": "str",
		"Tags": "str",
		"Screenshots": "str",
		"Movies" : "str",
	}

	def __init__(self, print_level: int):
		self.logger = Logger(print_level)


	def clean_data(self, read_path: str, write_path: str) -> None:
		#Maybe split this function in smaller and easy to understand functions?
		self.logger.log_message("Starting data clean", 1)

		self.logger.log_message("Starting data read", 2)
		#Load dataframe and filter intended data
		self.dataframe = pandas.read_csv(read_path, dtype = self.dtype_dict)
		self.logger.log_message("Data read correctly", 2)

		self.drop_unwanted_columns()
		self.add_average_user_data()
		self.add_number_categories_data()
		self.add_days_since_release_day_data()
		self.add_average_owners_per_day()
		self.add_estimated_lifetime_owners_data()
		self.save_cleaned_data(write_path)

		##At some point I need to normalize values, but I will do so in a different script
		## make this part of a data pipeline, in which a call the cleaner and the normalizer


	def drop_unwanted_columns(self) -> None:
		self.logger.log_message("Dropping unintended fields", 2)
		dataframe = self.dataframe
		dataframe = dataframe[["AppID", "Name", "Release date","Estimated owners", "Price", "Windows", "Mac", "Linux", "Positive", "Negative", "Genres", "Categories"]]
		dataframe = dataframe[dataframe["Price"] > 0]
		dataframe = dataframe[dataframe["Estimated owners"].notnull()]
		self.dataframe["Release date"] = pandas.to_datetime(dataframe["Release date"], format='mixed')
		self.logger.log_message("Field dropped correctly", 2)
		self.dataframe = dataframe

	def add_average_user_data(self) -> None:
		self.logger.log_message("Generating average owners column", 2)
		dataframe = self.dataframe
		owners_column = dataframe["Estimated owners"].values
		average_owners = []
		for i in range(0,len(owners_column)):
			owners = owners_column[i]
			owners_range = owners.split("-")
			average_owners.append((int(owners_range[0])+int(owners_range[1]))/2)
		dataframe["Average owners"] = average_owners
		self.dataframe = dataframe

	def add_number_categories_data(self) -> None:
		self.logger.log_message("Generating number of categories column", 2)
		dataframe = self.dataframe
		categories_column = dataframe["Categories"].values
		owners_column = dataframe["Estimated owners"].values
		number_categories = []
		for i in range(0,len(owners_column)):
			cat = str(categories_column[i])
			cat_number = len(cat.split(","))
			number_categories.append(cat_number)

		dataframe["Number categories"] = number_categories
		self.dataframe = dataframe
	
	def add_days_since_release_day_data(self) -> None:
		#Add the time since release to the data. Note that note the time the data was scrapped is 15th of September, 2024.
		self.logger.log_message("Generating days since release date", 2)
		dataframe = self.dataframe
		date_column = pandas.to_datetime(dataframe["Release date"].values, format = "mixed")
		days_release = []
		scrap_day = numpy.datetime64("2024-08-15")
		for i in range(0,len(date_column)):
			date = date_column[i]
			dif_date = scrap_day-date
			days_release.append(dif_date.days)

		dataframe["Days since release"] = days_release
		#Avoiding picking up steam games that are up in the backend for playtesting
		dataframe = dataframe[dataframe["Days since release"] > 0]
		self.dataframe = dataframe
	
	def add_average_owners_per_day(self) -> None:
		#Add the average owners per day
		self.logger.log_message("Generating average owners per days", 2)
		dataframe = self.dataframe
		average_owners = dataframe["Average owners"].values
		days_release = dataframe["Days since release"].values
		average_owners_per_day = []
		for i in range(0, len(days_release)):
			average_owners_per_day.append(float(average_owners[i])/float(days_release[i]))

		dataframe["Average owners per day"] = average_owners_per_day
		self.dataframe = dataframe

	def add_estimated_lifetime_owners_data(self) -> None:
		#Estimated lifetime owners. For this we use https://newsletter.gamediscover.co/p/data-deep-dive-whats-the-long-tail
		#That estimates total sales by the first year you will sell in average 3 times your first week. I think
		#this is enough to determine a pareto distribution and from that I can actually have estimate for the whole life time
		#Indeed, assuming a pareto Distrubition F the approximation tell us F(365) = 3 F(7). Solving that gives the parameter of
		#the pareto is \alpha = 0.00537. So distribution is F(x) =  1 - x^(-0.00537). So then we can normalize time by
		#estimating the total lifetime owners by dividing by F(days since release!)

		#Add the estimated lifetime owners
		self.logger.log_message("Generating estimated lifetime owners", 2)
		dataframe = self.dataframe
		pareto_degree = 0.00537

		average_owners = dataframe["Average owners"].values
		days_release = dataframe["Days since release"].values
		estimated_total_owners = []

		for i in range(0, len(days_release)):
			distribution_factor = 1-days_release[i]**(-pareto_degree)
			distribution_factor = max(distribution_factor, pareto_degree)
			estimation = average_owners[i]/distribution_factor
			estimated_total_owners.append(estimation)

		dataframe["Estimated lifetime owners"] = estimated_total_owners
		self.dataframe = dataframe


	def save_cleaned_data(self, write_path: str) -> None:
		self.logger.log_message("Writting cleaned data", 1)
		self.dataframe.to_csv(
			path_or_buf=write_path,
			sep=',',
			na_rep='',
			header=True,
			index=True,
			index_label=None,
			mode='w',
			storage_options={},
			compression='infer',
			chunksize=None,
			date_format=None,
			doublequote=True,
			escapechar=None,
			decimal='.',
			errors='strict'
		)

		self.logger.log_message("Cleaned data generated correctly at " + write_path, 1)

