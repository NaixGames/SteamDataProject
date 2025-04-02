import pandas as pandas
import math

from NeuralNetworkSerializer import NeuralNetworkSerializer
from NeuralNetwork import NeuralNetwork
from ActivationFunction import ActivationFunction


balatro_input_values = {
	"Price" : 12.74,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 0,
	"Positive": 134578,
	"Negative": 2636,
	"Number categories": 5,
	"Number tags": 20,
	"Number languages": 12,
	"Main Genre is Action": 0,
	"Main Genre is Adventure": 0,
	"Main Genre is Casual": 1,
	"Main Genre is Indie": 0,
	"Main Genre is Simulation": 0,
	"Main Genre is RPG": 0,
	"Main Genre is Strategy": 0,
	"Main Genre is Racing": 0,
	"Main Genre is Sports": 0,
	"Main Genre is Other": 0,
	"Days since release data": 394
}

slay_input_values = {
	"Price" : 20,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 1,
	"Positive": 173547,
	"Negative": 3870,
	"Number categories": 12,
	"Number tags": 20,
	"Number languages": 17,
	"Main Genre is Action": 0,
	"Main Genre is Adventure": 0,
	"Main Genre is Casual": 0,
	"Main Genre is Indie": 1,
	"Main Genre is Simulation": 0,
	"Main Genre is RPG": 0,
	"Main Genre is Strategy": 0,
	"Main Genre is Racing": 0,
	"Main Genre is Sports": 0,
	"Main Genre is Other": 0,
	"Days since release data": 2683
} 


yooka_input_values = {
	"Price" : 15,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 1,
	"Positive": 3907,
	"Negative": 1306,
	"Number categories": 10,
	"Number tags": 20,
	"Number languages": 9,
	"Main Genre is Action": 1,
	"Main Genre is Adventure": 0,
	"Main Genre is Casual": 0,
	"Main Genre is Indie": 0,
	"Main Genre is Simulation": 0,
	"Main Genre is RPG": 0,
	"Main Genre is Strategy": 0,
	"Main Genre is Racing": 0,
	"Main Genre is Sports": 0,
	"Main Genre is Other": 0,
	"Days since release data": 2900
} 



steamworld_dig_2_values = {
	"Price" : 20,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 1,
	"Positive": 6655,
	"Negative": 302,
	"Number categories": 7,
	"Number tags": 20,
	"Number languages": 6,
	"Main Genre is Action": 1,
	"Main Genre is Adventure": 0,
	"Main Genre is Casual": 0,
	"Main Genre is Indie": 0,
	"Main Genre is Simulation": 0,
	"Main Genre is RPG": 0,
	"Main Genre is Strategy": 0,
	"Main Genre is Racing": 0,
	"Main Genre is Sports": 0,
	"Main Genre is Other": 0,
	"Days since release data": 2737,
} 

input = yooka_input_values
#input = steamworld_dig_2_values
#input = slay_input_values
#input = balatro_input_values


## Functions por undoing scale normalization

def apply_log_scale(input: float, shift: float) -> float:
	return math.log(input + shift)


def apply_remap_category_scale(input: float, old_min: float, old_max: float, new_min: float, new_max: float) -> float:
	return (input-old_min)*(new_max-new_min)/(old_max- old_min) + new_min





#parse input for NN
inputs_array = []
inputs_array.append(apply_log_scale(input["Price"], 0.5))
inputs_array.append(input["Windows"])
inputs_array.append(input["Mac"])
inputs_array.append(input["Linux"])
inputs_array.append(apply_log_scale(input["Positive"],1))
inputs_array.append(apply_log_scale(input["Negative"],1))
inputs_array.append(apply_log_scale(input["Number categories"], 0))
inputs_array.append(apply_remap_category_scale(input["Number tags"],0,20,0,1))
inputs_array.append(apply_log_scale(input["Number languages"], 0))
inputs_array.append(input["Main Genre is Action"])
inputs_array.append(input["Main Genre is Adventure"])
inputs_array.append(input["Main Genre is Casual"])
inputs_array.append(input["Main Genre is Indie"])
inputs_array.append(input["Main Genre is Simulation"])
inputs_array.append(input["Main Genre is RPG"])
inputs_array.append(input["Main Genre is Strategy"])
inputs_array.append(input["Main Genre is Racing"])
inputs_array.append(input["Main Genre is Sports"])
inputs_array.append(input["Main Genre is Other"])



reserializer = NeuralNetworkSerializer(None, 1)
network = reserializer.load_data("serializer_trained.txt")
#network = reserializer.load_data("serializer_trained_one_layer.txt")
#network = reserializer.load_data("serializer_trained_linear.txt")
result = network.evaluate(inputs_array)
print(result)
print((math.exp(result)-1))
print((math.exp(result)-1)*input["Days since release data"])