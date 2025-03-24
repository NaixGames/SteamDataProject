from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction
import math

sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : 1/4 - x*x "

activation = ActivationFunction(sigmoid, sigmoid_der)

network = NeuralNetwork(3, 2, [4,3], [activation, activation, activation])

serializer = NeuralNetworkSerializer(network, 1)
serializer.save_data("serializer_test.txt")
new_network = serializer.load_data("serializer_test.txt")
reserializer = NeuralNetworkSerializer(new_network, 1)
reserializer.save_data("serializer_retest.txt")
