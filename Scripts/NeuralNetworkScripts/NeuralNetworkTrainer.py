import pandas as pandas

from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction

load_network = True

sigmoid = "lambda x : 1.0/(1+math.exp(-x)) "
sigmoid_der = "lambda x : math.exp(-x)/((1.0+math.exp(-x))**2)"

activation_sigmoid = ActivationFunction(sigmoid, sigmoid_der)

rel_alpha = "lambda x: x if x >= 0 else 0.1*x"
rel_alpha_der = "lambda x: 1 if x >= 0 else 0.1"

activation_rel = ActivationFunction(rel_alpha, rel_alpha_der)

srel = "lambda x: x if x >= 0 else math.exp(x)-1"
srel_der = "lambda x: 1 if x >= 0 else math.exp(x)"

activation_srel = ActivationFunction(srel, srel_der)


linear = "lambda x: x"
linear_der = "lambda x: 1"

activation_linear = ActivationFunction(linear, linear_der)


if (load_network):
	reserializer = NeuralNetworkSerializer(None, 1)
	network = reserializer.load_data("serializer_trained.txt")
else:
	network = NeuralNetwork(19, 2, [10, 3], [activation_linear, activation_srel, activation_srel])

#Hyperparams
learning_rate = 0.01
network.mini_batch_size = 300
network.regularization_parameter = 0.01

network.learning_rate = learning_rate
print("training starting")

data_read_path = "../../Data/shuffled_data.csv"
dataframe = pandas.read_csv(data_read_path)
outputs = dataframe[["Average owners per day"]]
dataframe = dataframe[["Price", "Windows", "Mac", "Linux", "Positive", "Negative", "Number categories", "Number tags", "Number languages", "Main Genre is Action", "Main Genre is Adventure", "Main Genre is Casual", "Main Genre is Indie", "Main Genre is Simulation", "Main Genre is RPG", "Main Genre is Strategy", "Main Genre is Racing", "Main Genre is Sports", "Main Genre is Other"]]
iterations = 50
repetitions = 5
validation_set_fraction = 0.1
loss_computation_frequency = 10
learning_rate_decrease = 0.95

data_size = len(outputs)
testing_size = int(data_size*(1-validation_set_fraction))

for j in range(0, repetitions):
	for i in range(0,iterations):
		#learn on the dataset
		for j in range(0, testing_size):
			row = dataframe.iloc[j].to_list()
			network.backtrack_input(row, outputs.iloc[j]["Average owners per day"])

		network.learning_rate *= learning_rate_decrease

		#compute loss
		if (i%loss_computation_frequency == 0):
			loss = 0
			for j in range(testing_size, data_size):
				row = dataframe.iloc[j].to_list()
				result = network.evaluate(row)
				output = outputs.iloc[j]["Average owners per day"]
				loss += (result - output)**2

			print(loss / (data_size - testing_size)) #note this is the loss without the regularization term, so might be a bit deceiving

	network.learning_rate = learning_rate

serializer = NeuralNetworkSerializer(network, 1)
serializer.save_data("serializer_trained.txt")
	

print("training ended. Hope it works!")
print(network)

