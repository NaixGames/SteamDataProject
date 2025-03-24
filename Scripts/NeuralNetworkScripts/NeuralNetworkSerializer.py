
import json
import ujson
import marshal
import sys
import numpy as numpy
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction

sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger


class NeuralNetworkSerializer:
	def __init__(self, neural_network: NeuralNetwork, print_level: int):
		self.neural_network = neural_network
		self.logger = Logger(print_level)

	def save_data(self, path: str) -> None:
		self.logger.log_message("Saving neural network", 1)
		
		#storage everything in one dictonary to only write to the file once
		storage_data = {}
		storage_data["number_inputs"] = self.neural_network.number_inputs
		storage_data["hidden_layers"] = len(self.neural_network.Nodes) - 1
		depths = []
		for i in range(0, len(self.neural_network.Nodes) - 1):
			depths.append(len(self.neural_network.Nodes[i]))

		storage_data["layers_depth"] = depths
	
		for i in range(0, len(self.neural_network.Nodes)):
			activation_func= []
			node = self.neural_network.Nodes[i][0]
			activation_func.append(str(node.activation_func.function_str))
			activation_func.append(str(node.activation_func.derivative_str))
			storage_data["function_data_layer_"+str(i)] = activation_func


		storage_data["weights"] = []
		for i in range (0, len(self.neural_network.Nodes)):
			for j in range(0, len(self.neural_network.Nodes[i])):
				storage_data["weights"].append(self.neural_network.Nodes[i][j].weights.tolist())

		with open(path, 'w') as file:  
			json.dump(storage_data, file, indent=4)

	def load_data(self, path: str) -> NeuralNetwork:
		with open(path, 'r') as json_data: 
			stored_data = json.load(json_data)
			json_data.close()
			
		number_inputs = stored_data["number_inputs"]
		hidden_layer = stored_data["hidden_layers"]
		depths = stored_data["layers_depth"]
		#recreate callbacks for activation functions
		activation_functions = []
			
		for i in range(0, hidden_layer+1):
			function_data = stored_data["function_data_layer_"+str(i)]
			function = ActivationFunction(function_data[0], function_data[1])
			activation_functions.append(function)

		network = NeuralNetwork(number_inputs, hidden_layer, depths, activation_functions)

		for i in range (0, len(network.Nodes)):
			for j in range(0, len(network.Nodes[i])):
				network.Nodes[i][j].weights = numpy.array(stored_data["weights"][i+j], dtype = 'float32')


		return network