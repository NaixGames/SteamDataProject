from DataCleaner import DataCleaner

data_read_path = "../../Data/93182_steam_games.csv"
data_write_path = "../../Data/cleaned_data.csv"
print_level = 1

cleaner = DataCleaner(print_level)
cleaner.clean_data(data_read_path, data_write_path)

#Data normalizer treatment here!