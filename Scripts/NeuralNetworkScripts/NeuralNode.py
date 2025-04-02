from ActivationFunction import ActivationFunction
import numpy as numpy

class NeuralNode:
	def __init__(self, function: ActivationFunction, number_inputs: int):
		self.activation_func = function
		self.weights = numpy.random.rand(number_inputs+1) #note the bias is the last element in this array
		#self.weights = numpy.ones(number_inputs+1)
		self.numer_inputs = number_inputs

		#this is cached values to avoid recomputing things for backtracking
		self.cached_input = []
		self.cached_evaluation = 0

		#this is to more easily do backtracking by having each node contain its own errors
		self.last_computed_error = 0

		self.accumulated_grad = numpy.zeros(number_inputs+1)


	def evaluate_value(self, inputs: list[float]) -> float:
		if (len(inputs) != self.numer_inputs):
			#Raise error
			print("DIMENSION MISMATCH!")
			return 0
		

		result = 0
		for input_index in range(0,self.numer_inputs):
			result += inputs[input_index]*self.weights[input_index]
		result += self.weights[self.numer_inputs]

		self.cached_evaluation = result
		self.cached_input = inputs.copy()
		return self.activation_func.evaluate(result)
	
	
	def give_derivate_from_cache_value(self) -> float:
		return self.activation_func.derivative(self.cached_evaluation)


	def set_error(self, error: float) -> None:
		self.last_computed_error = error


	def update_accumulated_grad_with_error(self, weight_index: int, multiplier: float) -> None:
		self.accumulated_grad[weight_index] += self.last_computed_error*multiplier

	def update_grad_with_cache_value(self, weight_index: int, regularization: float) -> None:
		#we use L^2 regularization to avoid stupidly high values of weights
		self.weights[weight_index] -= self.accumulated_grad[weight_index] + regularization*numpy.sign(self.weights[weight_index])
		self.accumulated_grad[weight_index] = 0