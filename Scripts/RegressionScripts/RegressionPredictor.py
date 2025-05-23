import json
import matplotlib.pyplot as pyplot
import math
import sys
import pandas
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger



class RegressionPredictor:
	def __init__(self,  print_level: int):
		self.logger = Logger(print_level)


	def predict_result(self, input: dict[str, float], train_data_path: str, z_score_info_path: str) -> float:
		#Should run a thing that validate that input actually aligns with the ones in the stored data ... eventually ...

		self.transform_input_values(input, z_score_info_path)

		with open(train_data_path) as json_data:
			data = json.load(json_data)
			json_data.close()


		weight_values = data["weight_map"]
		result = weight_values["bias"]
		for key in input:
			result += self.normalized_input[key]*weight_values[key + " weight"]

		return result
		


	def transform_input_values(self, input: dict[str, float], z_score_info_path: str) -> None:
		self.normalized_input = input.copy()
	

		self.apply_log_scale("Number categories", 0)
		self.apply_log_scale("Price", 0.5)
		self.apply_log_scale("Positive", 1)
		self.apply_log_scale("Negative", 1)
		self.apply_log_scale("Number languages", 0)
		self.remap_category_scale("Number tags", 0, 20, 0, 1)


	def apply_log_scale(self, category: str, base_value_offset: int) -> float:
		self.logger.log_message("Applying log scale to category " + category, 2)
		self.normalized_input[category] = math.log(self.normalized_input[category]+base_value_offset)

	def remap_category_scale(self, category: str, old_min: int, old_max:int, new_min:int, new_max:int) -> float:
		self.logger.log_message("Remapping scale to category " + category, 2)
		self.normalized_input[category] = (self.normalized_input[category] -old_min)*(new_max-new_min)/(old_max- old_min) + new_min


	def remap_category_from_min_max(self, category: str, info_path: str) -> None:
		self.logger.log_message("Remapping scale to category " + category, 2)

		with open(info_path) as json_data:
			z_score_data = json.load(json_data)
			json_data.close()

		self.remap_category_scale(json_data["min"], json_data["max"], 0, 1)


	def remap_category_to_z_score(self, category:str, z_score_info_path: str) -> float:
		#I should find a better way of doing this than just reading the original value to get the mean and variance.
		self.logger.log_message("Remapping scale to category " + category, 2)

		with open(z_score_info_path) as json_data:
			z_score_data = json.load(json_data)
			json_data.close()

		mean = z_score_data[category]["mean"]
		deviation = math.sqrt(z_score_data[category]["variance"])

		self.normalized_input[category] = (self.normalized_input[category]-mean)/deviation


	def transform_output_value(self, output: str) -> float:
		return math.exp(output)