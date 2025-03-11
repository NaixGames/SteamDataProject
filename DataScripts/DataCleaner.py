import numpy
import pandas

dataframe = pandas.read_csv("../Data/93182_steam_games.csv")

#Create a new data frame

#iterate through every entry
## if Price > 0 and reviews > 0 => add entry
## for entry we add the AppID, Name, Release date, AVERAGE OWNERS!,
## price, Platforms, Positive and negative reviews, recomendations, categories, genres

## I would also like to have Average owners / Time it was released (to normalize wrt to time)
## for that note the time the data was scrapped is 15th of September, 2024.
## For new inputs this is actually the quantity we want to estimate
## Note that then we should not use the average owners for the estimation! We would be using the same data twice.


