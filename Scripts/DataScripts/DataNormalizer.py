import numpy
import pandas
from datetime import datetime
import math
from scipy.stats import zscore

import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger


class DataNormalizer:
	valid_genres = [
		"Action",
		"Adventure",
		"Casual",
		"Indie",
		"Simulation",
		"RPG",
		"Strategy",
		"Racing",
		"Sports",
		"Other",
	]


	def __init__(self, print_level: int):
		self.logger = Logger(print_level)


	def normalize_data(self, clean_data_read_path: str, normalize_data_write_path: str) -> None:
		self.logger.log_message("Starting data normalization", 1)
		self.dataframe = pandas.read_csv(clean_data_read_path)
		self.drop_unused_field(["Name", "Estimated owners", "Release date", "Categories", "Tags", "Genres", "Average owners", "Supported languages","Days since release",])
		self.apply_log_scale("Number categories")
		self.apply_log_scale("Price")
		self.apply_log_scale("Positive")
		self.apply_log_scale("Negative")
		self.apply_log_scale("Number languages")
		self.apply_log_scale("Average owners per day")
		self.apply_log_scale("Estimated lifetime owners")
		self.remap_category_scale("Number tags", 0, 20, 0, 1)
		self.remap_category_to_z_score("Number tags")
		self.remap_category_to_one_shot("Main Genre", self.valid_genres)
		self.save_normalized_data(normalize_data_write_path)


	def drop_unused_field(self, unused_fields: list[str]) -> None:
		self.dataframe = self.dataframe.drop(columns = unused_fields)


	def apply_log_scale(self, category: str) -> None:
		self.logger.log_message("Applying log scale to category " + category, 2)
		self.dataframe[category] = self.dataframe[category].apply(lambda x: math.log(x+1))


	def remap_category_scale(self, category: str, old_min: int, old_max:int, new_min:int, new_max:int) -> None:
		self.logger.log_message("Remapping scale to category " + category, 2)
		self.dataframe[category] = self.dataframe[category].apply(lambda x: (x-old_min)*(new_max-new_min)/(old_max- old_min) + new_min)


	def remap_category_to_z_score(self, category:str) -> None:
		self.logger.log_message("Remapping to Z-score category:" + category, 2)
		self.dataframe[category] = zscore(self.dataframe[category])


	def remap_category_to_one_shot(self, category: str, valid_values: list[str]) -> None:
		self.logger.log_message("Remapping to one shot category:" + category, 2)
		one_shot_vectors = []
		#note we append new arrays to avoid the "copy by reference" problem python have if we do []*len(valid_values)
		for j in range(0,len(valid_values)):
			one_shot_vectors.append([])

		genre_column = self.dataframe[category].values
		
		for i in range(0,len(genre_column)):
			genre = genre_column[i]
			if (not genre in valid_values):
				Warning("Not valid genre detected. This is clearly an error")
				genre = "Other"
				continue

			index = valid_values.index(genre)
			
			for j in range (0, len(valid_values)):
				one_shot_vectors[j].append(j == index)

		for j in range(0,len(one_shot_vectors)):
			self.dataframe[category + " is " + valid_values[j]] = one_shot_vectors[j]


	def save_normalized_data(self, write_path:str) -> None:
		self.logger.log_message("Writting normalized data", 1)
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
		self.logger.log_message("Normalized data generated correctly at " + write_path, 1)