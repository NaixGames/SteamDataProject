from NeuralNode import NeuralNode
from ActivationFunction import ActivationFunction

class NeuralNetwork:
	def __init__(self, number_inputs: int, hidden_layers: int, hidden_layers_widths: list[int], activation_functions: list[ActivationFunction]):
		#Note we can also change the activation function per layer. Which is fine I guess
		if (len(hidden_layers_widths) != hidden_layers):
			print("DIMENSION MISMATCH IN NN CREATION!")
			return None
		
		if (len(activation_functions) != hidden_layers+1):
			print("DIMENSION MISMATCH IN NN CREATION!")
			return None
		
		self.number_inputs = number_inputs
		self.Nodes = []
		
		if (hidden_layers > 0):
			#fill first hidden layer
			layer = []
			for _ in range(0, hidden_layers_widths[0]):
				new_node = NeuralNode(activation_functions[0], number_inputs)
				layer.append(new_node)

			self.Nodes.append(layer)

			for layer_index in range(1, len(hidden_layers_widths)):
				layer = []
				for _ in range(0, hidden_layers_widths[layer_index]):
					new_node = NeuralNode(activation_functions[layer_index], hidden_layers_widths[layer_index-1])
					layer.append(new_node)

				self.Nodes.append(layer)


		#fill output layer
		layer = []

		last_layer_inputs = number_inputs
		if (hidden_layers > 0):
			last_layer_inputs = hidden_layers_widths[hidden_layers-1]

		new_node = NeuralNode(activation_functions[hidden_layers], last_layer_inputs)
		layer.append(new_node)
		self.Nodes.append(layer)

		#hyperparameter setup
		self.learning_rate = 0.001
		self.mini_batch_size = 300
		self.batch_index = 0
		self.regularization_parameter = 0


	def __str__(self):
		result = ""
		for layer_index in range(0, len(self.Nodes)):
			result += "Printing layer: " + str(layer_index) + "\n"
			layer = self.Nodes[layer_index]
			for node_index in range(0, len(layer)):
				result += "Printing node: " + str(node_index) + "\n"
				node = layer[node_index]
				for weight_index in range(0, len(node.weights)):
					result += "weight " + str(weight_index) + " : " + str(node.weights[weight_index]) + "\n"
				result += "cached derivative: " + str(node.give_derivate_from_cache_value()) + "\n"
				result += "cached error: " + str(node.last_computed_error) + "\n"
				result += "cache pre-evaluation: " +str(node.cached_evaluation) + "\n"

		return result

	def evaluate(self, input: list[float]) -> float:
		#note that for evalute we need to be smart to not recompute repeated values!
		
		#evaluate the first layer
		results = []
		first_layer = self.Nodes[0]
		for node_index in range (0, len(first_layer)):
			results.append(first_layer[node_index].evaluate_value(input))

		#evaluate subsequent layers
		for layer_index in range(1, len(self.Nodes)):
			nodes_layer = self.Nodes[layer_index]
			next_results = []
			for node_index in range (0, len(nodes_layer)):
				next_results.append(nodes_layer[node_index].evaluate_value(results))
			
			results = next_results.copy()
		
		return results[0]
	
	def backtrack_input(self, input: list[float], expected_output:float) -> None:
		#TODO : do this with matrix multiplication instead.
		output_value = self.evaluate(input) #note this update the cache information of the node, so we dont need to reevaluate while on a iteration

		#compute error of last layer		
		last_node = self.Nodes[len(self.Nodes)-1][0]
		last_node_derivate = last_node.give_derivate_from_cache_value()
		last_node.set_error(last_node_derivate*2*(output_value-expected_output)) #note we use loss function E(x,y) = (y-x)^2

		#iterate to get other errors
		for layer_index in range(len(self.Nodes)-2, -1, -1):
			layer = self.Nodes[layer_index]
			for node_index in range(0, len(layer)):
				node = layer[node_index]
				error_sum = 0
				next_layer = self.Nodes[layer_index+1]
				for next_node_index in range(0, len(next_layer)):
					next_node = next_layer[next_node_index]
					error_sum += next_node.last_computed_error*next_node.weights[node_index]
				error_sum *= node.give_derivate_from_cache_value()
				node.set_error(error_sum)

		#iterate to update derivates. This could be a separate function call if we need to.
		self.batch_index += 1
		for layer_index in range(0, len(self.Nodes)):
			layer = self.Nodes[layer_index]
			for node_index in range (0, len(layer)):
				node = layer[node_index]
				#update all "weights"
				for weight_index in range(0, len(node.weights)-1):
					multiplier = node.cached_input[weight_index]*self.learning_rate/self.mini_batch_size
					node.update_accumulated_grad_with_error(weight_index, multiplier)
					if (self.batch_index == self.mini_batch_size):
						node.update_grad_with_cache_value(weight_index, self.learning_rate*self.regularization_parameter)

				#update the bais
				node.update_accumulated_grad_with_error(len(node.weights)-1, self.learning_rate/self.mini_batch_size)
				if (self.batch_index == self.mini_batch_size):
					node.update_grad_with_cache_value(len(node.weights)-1, 0)
					self.batch_index = 0
