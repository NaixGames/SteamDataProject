import math
from ActivationFunction import ActivationFunction


sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : 1/4 - x*x "

activation = ActivationFunction(sigmoid, sigmoid_der)
print(activation.evaluate(0))
print(activation.evaluate(1))
print(activation.evaluate(-1))
print(activation.derivative(0))
print(activation.derivative(0.5))
print(activation.derivative(-1))