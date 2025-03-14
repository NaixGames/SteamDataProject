import numpy
import pandas



dtype_dict = {
	"AppID" : "int64",
	"Name" : "str",
	"Release date": "str",
	"Estimated owners": "str", 
	"Peak CCU": "int64",
	"age": "int64",
	"Price": "float64",
	"DLC count": "int64",
	"About the game": "str",
	"Supported languages": "str",
	"Full audio languages": "str",
	"Reviews": "str",
	"Header image": "str",
	"Website": "str",
	"Support url": "str",
	"Support email": "str",
	"Windows": "bool",
	"Mac": "bool",
	"Linux": "bool",
	"Metacritic": "int64",
	"Metacritic url": "str",
	"User score": "int64",
	"Positive": "int64",
	"Negative": "int64",
	"Score rank": "str",
	"Achievements": "str",
	"Recommendations": "str",
	"Notes": "str",
	"Average playtime forever": "int64",
	"Average playtime two weeks": "int64",
	"Median playtime forever": "int64",
	"Median playtime two weeks": "int64",
	"Developer": "str",
	"Publisher": "str",
	"Categories": "str",
	"Genres": "str",
	"Tags": "str",
	"Screenshots": "str",
	"Movies" : "str",
}

dataframe = pandas.read_csv("../Data/93182_steam_games.csv", dtype = dtype_dict)

dataframe = dataframe[["AppID", "Name", "Release date","Estimated owners", "Price", "Windows", "Mac", "Linux", "Positive", "Negative", "Genres"]]
dataframe = dataframe[dataframe["Price"] > 0]

dataframe.to_csv(
    path_or_buf='../Data/data_test.csv',
    sep=',',
    na_rep='',
    header=True,
    index=True,
    index_label=None,
    mode='w',
    storage_options={},
    compression='infer',
    chunksize=None,
    date_format=None,
    doublequote=True,
    escapechar=None,
    decimal='.',
    errors='strict'
)

#Create a new data frame

#iterate through every entry
## if Price > 0 and reviews > 0 => add entry
## for entry we add the AppID, Name, Release date, AVERAGE OWNERS!,
## price, Platforms, Positive and negative reviews, categories, genres

## I would also like to have Average owners / Time it was released (to normalize wrt to time)
## for that note the time the data was scrapped is 15th of September, 2024.
## For new inputs this is actually the quantity we want to estimate
## Note that then we should not use the average owners for the estimation! We would be using the same data twice.

##At some point I need to normalize values I think

"""

dataframe_dict = {"Test": [1,2,3,4]}

new_df = pandas.DataFrame(data = dataframe_dict, columns = ["Test"])

new_df.to_csv(
    path_or_buf='../Data/cleaned_data.csv',
    sep=',',
    na_rep='',
    header=True,
    index=True,
    index_label=None,
    mode='w',
    storage_options={},
    compression='infer',
    chunksize=None,
    date_format=None,
    doublequote=True,
    escapechar=None,
    decimal='.',
    errors='strict'
)

print("Data created")
print(new_df)"
"""