from DataCleaner import DataCleaner

#Params
data_read_path = "../../Data/93182_steam_games.csv"
clean_data_write_path = "../../Data/cleaned_data.csv"
normalized_data_write_path = "../../Data/normalized_data.csv"
print_level = 1
generate_clean_data = True

#data cleaning
if (generate_clean_data):
	cleaner = DataCleaner(print_level)
	cleaner.clean_data(data_read_path, clean_data_write_path)

#data normalization

#Data normalizer treatment here!