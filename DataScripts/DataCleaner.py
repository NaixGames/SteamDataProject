import numpy
import pandas
from datetime import datetime


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

#Load dataframe and filter intended data
dataframe = pandas.read_csv("../Data/93182_steam_games.csv", dtype = dtype_dict)
dataframe = dataframe[["AppID", "Name", "Release date","Estimated owners", "Price", "Windows", "Mac", "Linux", "Positive", "Negative", "Genres", "Categories"]]
dataframe = dataframe[dataframe["Price"] > 0]
dataframe = dataframe[dataframe["Estimated owners"].notnull()]
dataframe["Release date"] = pandas.to_datetime(dataframe["Release date"], format='mixed')

#Add the average owner column
owners_column = dataframe["Estimated owners"].values
average_owners = []
for i in range(0,len(owners_column)):
	owners = owners_column[i]
	owners_range = owners.split("-")
	average_owners.append((int(owners_range[0])+int(owners_range[1]))/2)

dataframe["Average owners"] = average_owners

#Add number of categories
categories_column = dataframe["Categories"].values
number_categories = []
for i in range(0,len(owners_column)):
	cat = str(categories_column[i])
	cat_number = len(cat.split(","))
	number_categories.append(cat_number)

dataframe["Number categories"] = number_categories



#Add the time since release to the data. Note that note the time the data was scrapped is 15th of September, 2024.
date_column = dataframe["Release date"].values
days_release = []
scrap_day = numpy.datetime64("2024-08-15")
for i in range(0,len(date_column)):
	date = date_column[i]
	dif_date = scrap_day-date+1
	days_release.append(dif_date.astype('timedelta64[D]').astype(int))

dataframe["Days since release"] = days_release
#Avoiding picking up steam games that are up in the backend for playtesting
dataframe = dataframe[dataframe["Days since release"] > 0]


#Add the average owners per day
average_owners = dataframe["Average owners"].values
days_release = dataframe["Days since release"].values
average_owners_per_day = []
for i in range(0, len(days_release)):
	average_owners_per_day.append(float(average_owners[i])/float(days_release[i]))

dataframe["Average owners per day"] = average_owners_per_day



#Estimated lifetime owners. For this we use https://newsletter.gamediscover.co/p/data-deep-dive-whats-the-long-tail
#That estimates total sales by the first year you will sell in average 3 times your first week. I think
#this is enough to determine a pareto distribution and from that I can actually have estimate for the whole life time
#Indeed, assuming a pareto Distrubition F the approximation tell us F(365) = 3 F(7). Solving that gives the parameter of
#the pareto is \alpha = 0.00537. So distribution is F(x) =  1 - x^(-0.00537). So then we can normalize time by
#estimating the total lifetime owners by dividing by F(days since release!)

#Add the estimated lifetime owners
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

dataframe.to_csv(
    path_or_buf='../Data/cleaned_data.csv',
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

## Todo: add a log object class to allow for detailed logging

## split this using a strategy pattern

##At some point I need to normalize values, but I will do so in a different script

## make this part of a data pipeline, in which a call the cleaner and the normalizer


