import math
from ActivationFunction import ActivationFunction


sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : math.exp(-x)/((1.0+math.exp(-x))**2)"

activation = ActivationFunction(sigmoid, sigmoid_der)

print(activation.evaluate(0))
print(activation.evaluate(1))
print(activation.evaluate(-1))
print(activation.derivative(0))
print(activation.derivative(0.5))
print(activation.derivative(1))
print(activation.derivative(-1))

print("Smooth REL")
srel = "lambda x: x if x >= 0 else math.exp(x)-1"
srel_der = "lambda x: 1 if x >= 0 else math.exp(x)"

activation_srel = ActivationFunction(srel, srel_der)

print(activation_srel.evaluate(0))
print(activation_srel.evaluate(1))
print(activation_srel.evaluate(-1))
print(activation_srel.derivative(0))
print(activation_srel.derivative(0.5))
print(activation_srel.derivative(1))
print(activation_srel.derivative(-1))