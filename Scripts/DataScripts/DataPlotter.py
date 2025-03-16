import numpy
import pandas
import matplotlib.pyplot as pyplot
from datetime import datetime
import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger

class DataPlotter:
	def __init__(self, print_level: int):
		self.logger = Logger(print_level)#

	def plot_data(self, data_path: str) -> None:
		self.logger.log_message("Printing relevant data", 1)
		dataframe = pandas.read_csv(data_path)
		#dataframe["Average owners per day"].sort_index().value_counts().plot(kind = 'bar')
		#dataframe["Estimated lifetime owners"].sort_index().value_counts().plot(kind = 'bar')
		
		#dataframe["Positive"].value_counts().sort_index().plot(kind = 'bar')
		#dataframe["Number categories"].value_counts().sort_index().plot(kind = 'bar')
		#dataframe["Number genres"].value_counts().sort_index().plot(kind = 'bar')
		#dataframe["Number tags"].value_counts().sort_index().plot(kind = 'bar')
		#dataframe["Number languages"].value_counts().sort_index().plot(kind = 'bar')
		#dataframe["Days since release"].value_counts().sort_index().plot(kind = 'bar')
		#pyplot.show()