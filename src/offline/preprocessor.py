import librosa
import numpy as np

import src.other.constants as const
import src.other.garcon as gc

class Preprocessor():
	def __init__(self, X_train, y_train):
		'''
		Inits a preprocessor.
		:param X_train: type=list>string,	shape=(m,	)
		:param y_train: type=list>scalar,	shape=(m,	)
		'''
		self._X_train, self._y_train = X_train, y_train

	def init(self):
		gc.enter_func()
		pass

	def preprocess(self, filename):
		'''
		Preprocesses a .wav filename.
		:param filename: 	.wav filename.
		:return: 	type=np.array,	shape=(d,	)
		'''
		gc.enter_func()
		y, sr = librosa.load(filename)
		mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=const.N_MFCCS)
		return mfcc

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
