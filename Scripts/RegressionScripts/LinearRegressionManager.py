import pandas
from LinearRegression import LinearRegression
from LossDataPlotter import LossDataPlotter

#Params
data_read_path = "../../Data/shuffled_data.csv"
print_level = 1
train_model = True
print_loss = True

input_variables = [
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
]


HyperParams = {
	"learning_rate" : 0.01,
	"mini_batch_size": 250,
	"validation_size_fraction": 0.1,
	"iteration_steps": 2000,
	"learning_rate_dif_stop" : 0.001,
}

if train_model:
	dataframe = pandas.read_csv(data_read_path)
	#linear_regression = LinearRegression(dataframe, input_variables, "Average owners per day", HyperParams, print_level)
	linear_regression = LinearRegression(dataframe, input_variables, "Estimated lifetime owners", HyperParams, print_level)
	linear_regression.run_regression()

if print_loss:
	loss_data_plotter = LossDataPlotter(print_level)
	loss_data_plotter.plot_loss('training_results.txt')