import json
import matplotlib.pyplot as pyplot

import sys
sys.path.append("D:/Github/SteamDataProject/Scripts/UtilScripts")
from Logger import Logger


class LossDataPlotter:
	def __init__(self,  print_level: int):
		self.logger = Logger(print_level)


	def plot_loss(self, path:str) -> None:
		with open(path) as json_data:
			data = json.load(json_data)
			json_data.close()

		test_loss = data["test_loss"]
		validation_loss = data["validation_loss"]

		fig = pyplot.figure()
		ax1 = fig.add_subplot(111)
		xax = range(len(test_loss))


		ax1.plot(xax, test_loss, c='b', label='test loss')
		ax1.plot(xax, validation_loss, c='r', label = 'validation loss')
		pyplot.legend()
		pyplot.show()