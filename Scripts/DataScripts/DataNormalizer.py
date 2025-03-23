import numpy
import pandas
from datetime import datetime
import math
import json
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


	def normalize_data(self, clean_data_read_path: str, normalize_data_write_path: str, info_output: str) -> None:
		self.logger.log_message("Starting data normalization", 1)
		self.transform_info = {}
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
		self.remap_category_from_min_max("Estimated lifetime owners", 0, 1)
		self.remap_category_scale("Number tags", 0, 20, 0, 1)
		self.remap_category_to_z_score("Number genres")
		self.remap_category_to_one_shot("Main Genre", self.valid_genres)

		self.save_transform_info(info_output)
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

	def remap_category_from_min_max(self, category: str, new_min:int, new_max:int) -> None:
		cat = self.dataframe[category]
		#need to story max and min to undo the transform
		cat_info = {}
		cat_info["old_min"] = cat.min()
		cat_info["old_max"] = cat.max()
		self.transform_info[category] = cat_info
		self.remap_category_scale(category, cat.min(), cat.max(), new_min, new_max)

	def remap_category_to_z_score(self, category:str) -> None:
		self.logger.log_message("Remapping to Z-score category:" + category, 2)
		cat = self.dataframe[category]
		cat_info = {}
		cat_info["mean"] = cat.mean()
		cat_info["variance"] =  cat.var()
		self.transform_info[category] = cat_info
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


	def save_transform_info(self, z_scores_info_output:str) -> None:
		with open(z_scores_info_output, 'w') as file:  
			json.dump(self.transform_info, file, indent=4)