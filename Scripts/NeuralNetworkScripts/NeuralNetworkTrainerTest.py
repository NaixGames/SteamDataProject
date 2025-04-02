import pandas as pandas

from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction


sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : math.exp(-x)/((1.0+math.exp(-x))**2)"

activation_sigmoid = ActivationFunction(sigmoid, sigmoid_der)

rel_alpha = "lambda x: x if x >= 0 else 0.1*x"
rel_alpha_der = "lambda x: 1 if x >= 0 else 0.1"

activation_rel = ActivationFunction(rel_alpha, rel_alpha_der)

linear = "lambda x: x"
linear_der = "lambda x: 1"

activation_linear = ActivationFunction(linear, linear_der)

network = NeuralNetwork(1, 0, [], [activation_linear])
#Hyperparams
network.learning_rate = 0.00005
network.mini_batch_size = 10
print("training starting")

data_read_path = "../../Data/TestData.csv"
dataframe = pandas.read_csv(data_read_path)
outputs = dataframe[["Output"]]
dataframe = dataframe[["Input"]]
iterations = 10000
validation_set_fraction = 0.5

data_size = len(outputs)
testing_size = int(data_size*(1-validation_set_fraction))

for i in range(0,iterations):
	#learn on the dataset
	for j in range(0, testing_size):
		row = dataframe.iloc[j].to_list()
		network.backtrack_input(row, outputs.iloc[j]["Output"])

	#compute loss
	loss = 0
	for j in range(testing_size, data_size):
		row = dataframe.iloc[j].to_list()
		result = network.evaluate(row)
		output = outputs.iloc[j]["Output"]
		loss += (result - output)**2/2

	print(loss/(data_size - testing_size))

	
print("training ended. Hope it works!")
print(network)
print(network.evaluate([1]))
print(network.evaluate([2]))
print(network.evaluate([2.5]))
print(network.evaluate([12]))