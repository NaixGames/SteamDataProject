import numpy
import pandas
from datetime import datetime


import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger

class LinearRegression:
	def __init__(self, dataframe:pandas.DataFrame, input_variables: list[str], output_variable, hyperparams: dict[str, float], print_level: int):
		self.logger = Logger(print_level)
		self.dataframe = dataframe
		self.input_var = input_variables
		self.num_inputs = len(input_variables)
		self.output_var = output_variable
		self.hyperparams = hyperparams

		weights_map = {}
		for i in range(0, len(input_variables)):
			weights_map[input_variables[i] + " weight"] = 0
		weights_map["bias"] = 0

		self.weights_map = weights_map
		self.gradient_vector = self.weights_map.copy()

	def run_regression(self):
		self.logger("Running regression", 1)

		data_frame_size = len(self.dataframe[self.output_var[0]])
		max_learn_index = data_frame_size*self.hyperparams["validation_size_fraction"]

		index_learn = 0
		index_loss = 0
		index_loss_validate = max_learn_index

		for round in range(0,self.hyperparams["iteration_steps"]):
			
			#compute gradient
			for index_batch in range(0, self.hyperparams["mini_batch_size"]):
				for i in range(0, self.num_inputs):
					self.gradient_vector[self.input_var[i] + " weight"] = self.compute_grad_weight(index_learn, self.input_var[i]) 
				
				self.gradient_vector["bias"] = self.compute_grad_bias(index_learn)

				#update indexes
				index_learn = (index_learn+1)%max_learn_index


			#update bais and weight
			for i in range(0, self.num_inputs):
				self.weights_map[self.input_var[i] + " weight"] = -self.gradient_vector[self.input_var[i] + " weight"]*self.hyperparams["learning_rate"]
				
			self.weights_map["bias"] = -self.gradient_vector["bias"]*self.hyperparams["learning_rate"] 

			#compute loss on test set (in particular on set you just computed gradient)

			sum_loss = 0
			for index_batch in range(0, self.hyperparams["mini_batch_size"]):
				sum_loss += self.compute_loss(index_loss)

				#update indexes
				index_loss = (index_loss+1)%max_learn_index
			

			#Should put this in an array and then plot
			print("Loss on test set " + str(sum_loss))

			sum_loss = 0
			#compute loss on validation set
			for index_batch in range(0, self.hyperparams["mini_batch_size"]):
				sum_loss += self.compute_loss(index_loss_validate)

				index_loss_validate += 1
				if (index_loss_validate == data_frame_size):
					index_loss_validate = max_learn_index

			print("Loss on validation set " + str(sum_loss))

			#reset gradient values to 0
			for key in self.gradient_vector.keys:
				self.gradient_vector[key] = 0



	def compute_grad_weight(self, index_data: int, input_var_name: str) -> float:
		index_val = self.compute_dif_at_index(index_data)
		return self.dataframe[input_var_name][index_data]*index_val / self.hyperparams["mini_batch_size"]
	

	def compute_grad_bias(self, index_data: int) -> float:
		index_val = self.compute_dif_at_index(index_data)
		return 2*index_val / self.hyperparams["mini_batch_size"]
	

	def compute_loss(self, index_data) -> float:
		index_val = self.compute_dif_at_index(index_data)
		return index_val*index_val / self.hyperparams["mini_batch_size"]
	

	def compute_dif_at_index(self, index_data) -> float:
		index_val = self.weights_map["bias"]
		for i in range(0, self.num_inputs):
			var_name = self.num_inputs[i]
			index_val += self.dataframe[var_name][index_data]*self.weights_map[var_name + " weight"]

		index_val -= self.dataframe[self.output_var][index_data]
		return index_val