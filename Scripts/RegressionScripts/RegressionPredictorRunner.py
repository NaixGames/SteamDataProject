from RegressionPredictor import RegressionPredictor


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


input = slay_input_values









release = input["Days since release data"]
input.pop('Days since release data', None)

regresssion_predictor = RegressionPredictor(1)
regresssion_predictor.predict_result(input, release, 'training_results_average_owners.txt', "D:\Github\SteamDataProject\Scripts\DataScripts\z_score_output.txt")
#regresssion_predictor.predict_result(yooka_input_values, 'training_results_lifetime_owners.txt', "D:\Github\SteamDataProject\Scripts\DataScripts\z_score_output.txt")