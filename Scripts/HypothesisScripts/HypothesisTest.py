import numpy
import pandas
import math
import scipy.stats as stats

import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger

class HypothesisTest:
	def __init__(self, dataframe:pandas.DataFrame, print_level: int):
		self.logger = Logger(print_level)
		self.dataframe = dataframe


	def run_test(self, category_variable: str, comparison_variable: str, yes_value, no_value) -> float:
		#note this just run test of H_0: mean_1 >= mean_2 versus H_1: mean_1 < mean_2
		yes_category = self.dataframe[self.dataframe[category_variable] == yes_value][comparison_variable] 
		no_category = self.dataframe[self.dataframe[category_variable] == no_value][comparison_variable] 

		#compute the test statistic
		N_size = len(yes_category)
		M_size = len(no_category)

		mean_yes = yes_category.mean()
		mean_no = no_category.mean()
		var_yes = yes_category.var()
		var_no = no_category.var()

		estimated_var = ((N_size-1.0)*var_yes + (M_size-1.0)*var_no)/(N_size+M_size-2.0)
		t_stats = (mean_yes+mean_no)/math.sqrt((estimated_var/N_size)+(estimated_var/M_size))

		freedom_deg = N_size+M_size-2
		return stats.t.cdf(t_stats, freedom_deg)