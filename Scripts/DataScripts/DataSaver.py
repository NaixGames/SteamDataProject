import pandas
from Logger import Logger

def save_data(dataframe: pandas.DataFrame, save_path: str, print_level: int) -> None:
	logger = Logger(print_level)
	logger.log_message("Writting normalized data", 1)
	dataframe.to_csv(
		path_or_buf=save_path,
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
	logger.log_message("Normalized data generated correctly at " + save_path, 1)