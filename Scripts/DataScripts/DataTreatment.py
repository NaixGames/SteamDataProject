from DataCleaner import DataCleaner
from DataPlotter import DataPlotter
from DataNormalizer import DataNormalizer
from DataShuffler import DataShuffler

#Params
data_read_path = "../../Data/93182_steam_games.csv"
clean_data_write_path = "../../Data/cleaned_data.csv"
normalized_data_write_path = "../../Data/normalized_data.csv"
shuffle_data_write_path = "../../Data/shuffled_data.csv"
print_level = 2
generate_clean_data = False
plot_clean_data = False
normalized_data = False
plot_normalized_data = False
shuffle_data = True


if (generate_clean_data):
	cleaner = DataCleaner(print_level)
	cleaner.clean_data(data_read_path, clean_data_write_path)


if (plot_clean_data):
	plotter = DataPlotter(print_level)
	plotter.plot_data(clean_data_write_path)


if (normalized_data):
	normalizer = DataNormalizer(print_level)
	normalizer.normalize_data(clean_data_write_path, normalized_data_write_path)


if (plot_normalized_data):
	plotter = DataPlotter(print_level)
	plotter.plot_data(normalized_data_write_path)


if (shuffle_data):
	shuffler = DataShuffler(print_level)
	shuffler.shuffle_data(normalized_data_write_path, shuffle_data_write_path)

