from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction


sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : 1/4 - x*x "

activation_sigma = ActivationFunction(sigmoid, sigmoid_der)

rel_alpha = "lambda x: x if x >= 0 else 0.1*x"
rel_alpha_der = "lambda x: 1 if x >= 0 else 0.1"

activation_rel = ActivationFunction(rel_alpha, rel_alpha_der)

network = NeuralNetwork(1, 1, [2], [activation_sigma, activation_rel])

input = [12]
print(network.evaluate(input))
print(network)
