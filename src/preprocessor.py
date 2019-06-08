import librosa as lr

class Preprocessor:
	def __init__(self, raw_x, raw_y):
		self.raw_x, self.raw_y = raw_x, raw_y
		self.preprocess()

	def preprocess(self):
		pass

	def preprocess_audio(self, wfs):

