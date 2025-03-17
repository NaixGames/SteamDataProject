import pandas
from LinearRegression import LinearRegression

#Params
data_read_path = "../../Data/shuffled_data.csv"
print_level = 2


input_variables = {
	"Price",
	"Windows",
	"Mac",
	"Linux",
	"Positive",
	"Negative",
	"Number categories",
	"Number tags",
	"Number languages",
	"Main Genre is Action",
	"Main Genre is Adventure",
	"Main Genre is Casual",
	"Main Genre is Indie",
	"Main Genre is Simulation",
	"Main Genre is RPG",
	"Main Genre is Strategy",
	"Main Genre is Racing",
	"Main Genre is Sports",
	"Main Genre is Other",
}

output_variables = {
	"Average owners per day",
	"Estimated lifetime owners",
}

HyperParams = {
	"learning_rate" : 0.1,
	"mini_batch_size": 50,
	"validation_size_fraction": 0.1,
	"iteration_steps": 100,
}

read_path = "../../Data/shuffled_data.csv"
dataframe = pandas.read_csv(read_path)
linear_regression = LinearRegression(dataframe, input_variables, "Average owners per day", HyperParams, 1)