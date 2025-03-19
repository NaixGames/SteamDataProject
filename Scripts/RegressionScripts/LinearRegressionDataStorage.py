import json

import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger

class LinearRegressionDataStorage:
	def __init__(self, input_variables: list[str], output_variable, hyperparams: dict[str, float], print_level: int):
		self.input_var = input_variables
		self.output_var = output_variable
		self.hyperparams = hyperparams
		self.logger = Logger(print_level)
		self.test_loss = []
		self.validation_loss = []

	def save_data(self, weight_map: dict[str, float]) -> None:
		self.logger.log_message("Saving trained data", 1)
		
		#storage everything in one dictonary to only write to the file once
		storage_data = {}
		storage_data["weight_map"] = weight_map
		storage_data["input variables"] = self.input_var
		storage_data["output variable"] = self.output_var
		storage_data["hyperparams"] = self.hyperparams
		storage_data["test_loss"] = self.test_loss
		storage_data["validation_loss"] = self.validation_loss

		
		with open("training_results.txt", 'w') as file:  
			json.dump(storage_data, file, indent=4)