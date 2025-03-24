from ActivationFunction import ActivationFunction
import numpy as numpy

class NeuralNode:
	def __init__(self, function: ActivationFunction, number_inputs: int):
		self.activation_func = function
		self.weights = numpy.random.rand(number_inputs+1)
		self.numer_inputs = number_inputs

	def evaluate_value(self, inputs: list[float]) -> float:
		if (len(inputs) != self.numer_inputs):
			#Raise error
			print("DIMENSION MISMATCH!")
			return 0
		
		result = 0
		for i in range(0,self.numer_inputs):
			result += inputs[i]*self.weights[i]
		result += self.weights[self.numer_inputs]
		return self.activation_func.evaluate(result)
	
	def evaluate_derivative(self, inputs: list[float], weight_index: int) -> float:
		if (len(inputs) != self.numer_inputs):
			#Raise error
			print("DIMENSION MISMATCH!")
			return 0
		
		if (weight_index > self.numer_inputs):
			#Raise error
			print("DIMENSION MISMATCH!")
			return 0

		evaluation = 0
		for i in range(0,self.numer_inputs):
			evaluation += inputs[i]*self.weights[i]
		evaluation += self.weights[self.numer_inputs]

		mult = 1
		if (weight_index < self.numer_inputs):
			mult = inputs[weight_index]

		return self.activation_func.derivative(evaluation)*mult