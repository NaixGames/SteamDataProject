from collections.abc import Callable
import math #node this is needed so eval actually is correctly casted when using math functions. Annoying, but pythons fault

class ActivationFunction:
	def __init__(self, main_function: str, derivate_function: str):
		self.function_str = main_function
		self.function = eval(main_function)
		self.derivative_str = derivate_function
		self.derivatite = eval(derivate_function)
		
	
	def evaluate(self, x: float) -> float:
		return self.function(x)
	
	def derivative(self, x: float) -> float:
		return self.derivatite(x)