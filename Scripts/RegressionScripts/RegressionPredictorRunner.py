from RegressionPredictor import RegressionPredictor


input_values = {
	"Price" : 2.99,
	"Windows" : 1,
	"Mac" : 0,
	"Linux": 1,
	"Positive": 10,
	"Negative": 4,
	"Number categories": 2,
	"Number tags": 4,
	"Number languages": 5,
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
}


balatro_input_values = {
	"Price" : 12.74,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 0,
	"Positive": 134578,
	"Negative": 2636,
	"Number categories": 5,
	"Number tags": 3,
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
}

slay_input_values = {
	"Price" : 20,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 1,
	"Positive": 173547,
	"Negative": 3870,
	"Number categories": 12,
	"Number tags": 3,
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
}


yooka_input_values = {
	"Price" : 15,
	"Windows" : 1,
	"Mac" : 1,
	"Linux": 1,
	"Positive": 3907,
	"Negative": 1306,
	"Number categories": 10,
	"Number tags": 4,
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
}

regresssion_predictor = RegressionPredictor(1)
regresssion_predictor.predict_result(slay_input_values, 'training_results.txt')