import numpy
import pandas
from datetime import datetime
import math
from scipy.stats import zscore

import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger
from DataSaver import save_data

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
		self.cast_bool_column_to_int("Windows")
		self.cast_bool_column_to_int("Mac")
		self.cast_bool_column_to_int("Linux")
		self.apply_log_scale("Number categories", 0)
		self.apply_log_scale("Price", 0.5)
		self.apply_log_scale("Positive", 1)
		self.apply_log_scale("Negative", 1)
		self.apply_log_scale("Number languages", 0)
		self.apply_log_scale("Average owners per day", 1)
		self.apply_log_scale("Estimated lifetime owners", 1)
		self.remap_category_scale("Number tags", 0, 20, 0, 1)
		self.remap_category_to_z_score("Number tags")
		self.remap_category_to_one_shot("Main Genre", self.valid_genres)
		save_data(self.dataframe, normalize_data_write_path, 1)


	def drop_unused_field(self, unused_fields: list[str]) -> None:
		self.dataframe = self.dataframe.drop(columns = unused_fields)


	def cast_bool_column_to_int(self, category: str) -> None:
		self.dataframe[category] = self.dataframe[category].astype(int)


	def apply_log_scale(self, category: str, base_value_offset: int) -> None:
		self.logger.log_message("Applying log scale to category " + category, 2)
		self.dataframe[category] = self.dataframe[category].apply(lambda x: math.log(x+base_value_offset))


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
				one_shot_vectors[j].append(int(j == index))

		for j in range(0,len(one_shot_vectors)):
			self.dataframe[category + " is " + valid_values[j]] = one_shot_vectors[j]