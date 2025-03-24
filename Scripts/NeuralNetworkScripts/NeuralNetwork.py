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
		#fill first hidden layer
		layer = []
		for i in range(0, hidden_layers_widths[0]):
			new_node = NeuralNode(activation_functions[0], number_inputs)
			layer.append(new_node)

		self.Nodes.append(layer)

		for i in range(1, len(hidden_layers_widths)):
			layer = []
			for j in range(0, hidden_layers_widths[i]):
				new_node = NeuralNode(activation_functions[i], hidden_layers_widths[i-1])
				layer.append(new_node)

			self.Nodes.append(layer)


		#fill output layer
		layer = []
		new_node = NeuralNode(activation_functions[hidden_layers], hidden_layers_widths[hidden_layers-1])
		layer.append(new_node)
		self.Nodes.append(layer)


	def evaluate(self, input: list[float]) -> float:
		#note that for evalute we need to be smart to not recompute repeated values!
		
		#evaluate the first layer
		results = []
		nodes_layer = self.Nodes[0]
		for j in range (0, len(nodes_layer)):
			results.append(nodes_layer[j].evaluate_value(input))

		#evaluate subsequent layers
		for i in range(1, len(self.Nodes)):
			nodes_layer = self.Nodes[i]
			next_results = []
			for j in range (0, len(nodes_layer)):
				next_results.append(nodes_layer[j].evaluate_value(results))
			
			results = next_results.copy()
		
		return results[0]
	
	#for backtracking I should be smart not to recompute value when computing different derivatives.
	def backtrack(self, input: list[float]) -> None:
		return
	
	def train(self) -> None:
		return