import numpy
import pandas
from datetime import datetime


import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger
from DataSaver import save_data

class DataShuffler:
	def __init__(self, print_level: int):
		self.logger = Logger(print_level)
	
	def shuffle_data(self, read_path:str, write_data_path: str) -> None:
		self.logger.log_message("Randomizating data rows", 1)
		dataframe = pandas.read_csv(read_path)
		dataframe = dataframe.sample(frac=1)
		save_data(dataframe, write_data_path, 1)