import src.garcon as gc
import numpy as np
import scipy.io.wavfile as wave
import librosa

class Preprocessor():
	def __init__(self, X_train, y_train):
		self._X_train, self._y_train = X_train, y_train
		pass

	def preprocess(self):
		gc.enter_func()
		self._X_train = self._normalize(self._X_train)

	def _normalize(self, X):
		'''
		Normalizes data to have mean=0 and std=1.
		:param X:	type=np.array,	shape=(m,	d)
		:return:	type=np.array,	shape=(m,	d)
		'''
		gc.enter_func()
		mean = np.mean(X, axis=0)
		std = np.std(X, axis=0)
		return (X - mean) / std

	def process_single_file(self, fn):
		'''
		Processes a .wav filename to produce a feature vector.
		:param fn: .wav filename.
		:return:	type=np.array,	shape=(d,	)
		'''
		waveform, _ = librosa.load(fn)
		