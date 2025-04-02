from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction


linear = "lambda x: x"
linear_der = "lambda x: 1"

activation_linear = ActivationFunction(linear, linear_der)

network = NeuralNetwork(2, 0, [], [activation_linear])

network.Nodes[0][0].weights[0] = 2
network.Nodes[0][0].weights[1] = 3
network.Nodes[0][0].weights[2] = 1

input = [10, 5]
print(10*2 + 5*3 + 1 )
print(network.evaluate(input))

input = [-3, 7]
print(-3*2 + 7*3 + 1 )
print(network.evaluate(input))

print(network)
