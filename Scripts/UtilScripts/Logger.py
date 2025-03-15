class Logger:
	#Intended is level 0 => no print, level 1 => Basic print, level 2 => verbose
	Access = 0
	def __init__(self, access_level: int):
		self.Access = access_level

	def log_message(self, message: str, message_level: int):
		if (message_level > self.Access):
			return
		print(message)