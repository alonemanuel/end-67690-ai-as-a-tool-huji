import librosa
import numpy as np
import wavio
from tqdm import tqdm

import src.other.constants as const
import src.other.garcon as gc

class Preprocessor():
	'''
	Module for preprocessing the data.
	'''

	def __init__(self):
		self._X_train, self._y_train = None, None

	def init(self, X_train, y_train):
		'''
		Inits a preprocessor.
		:param X_train: type=list>string,	shape=(m,	)
		:param y_train: type=list>scalar,	shape=(m,	)
		'''
		gc.enter_func()
		self._X_train, self._y_train = X_train, y_train

	def preprocess_X(self, filenames):
		'''
		:param filenames:	type=list,		shape=(m,	)
		:return: 			type=np.array,	shape=(m,	d)
		'''
		gc.enter_func()
		filenames = filenames if type(filenames) == list else [filenames]
		mfccs = []
		for fn in tqdm(filenames):
			mfcc = self._get_mfcc_from_fn(fn)
			mfccs.append(mfcc)
		numpied = np.array(mfccs)
		transformed = self._transform_data(numpied)
		return transformed

	def preprocess_y(self, y):
		'''
		:param y:	type=list,		shape=(m,	)
		:return: 	type=np.array,	shape=(m,	)
		'''
		return np.array(y)

	def _transform_data(self, data):
		'''
		Transform the data numerically.
		:param data:	type=np.array,	shape=(m,	d)
		:return: 		type=np.array,	shape=(m,	d)
		'''
		# centered = self._center(data)
		centered = data
		normalized = self._normalize(centered)
		return normalized

	def _get_mfcc_from_fn(self, fn):
		'''
		Return the mel-frequency-cepstrum-coefficients of the .wav filename.
		'''
		wave = wavio.read(fn)
		sr, y = wave.rate, wave.data.ravel().astype(float)
		mfcc = np.mean(
				librosa.feature.mfcc(y=y, sr=sr, n_mfcc=const.N_MFCCS).T,
				axis=0)
		return mfcc

	def _center(self, X):
		'''
		Center the data around the origin.
		:param X:	type=np.array,	shape=(m,	d)
		:return: 	type=np.array,	shape=(m,	d)
		'''
		mean = np.mean(X)
		centered = X - mean
		return centered

	def _normalize(self, X):
		'''
		Normalizes data to have mean=0 and std=1.
		:param X:	type=np.array,	shape=(m,	d)
		:return:	type=np.array,	shape=(m,	d)
		'''
		gc.enter_func()
		mean = np.mean(X, axis=0)
		std = np.std(X, axis=0)
		return (X - mean) / (std + 1 ** -6)
