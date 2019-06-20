import librosa
import numpy as np
import wavio
from tqdm import tqdm

import src.other.constants as const
import src.other.garcon as gc

class Preprocessor():
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

	def preprocess(self, filenames):
		'''
		Preprocesses a .wav filename.
		:param filename: 	type=list>.wav filename,	shape=(m,	)
		:return: 	type=np.array,	shape=(m,	d)
		'''
		gc.enter_func()
		gc.log(f'filenames = {filenames}')
		mfccs = []
		if type(filenames) == list:
			for fn in tqdm(filenames):
				wave = wavio.read(fn)
				sr, y = wave.rate, wave.data.ravel().astype(float)
				mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr,
													n_mfcc=const.N_MFCCS).T,
							   axis=0)
				mfccs.append(mfcc)
			numpied = np.array(mfccs)
		else:
			wave = wavio.read(filenames)
			sr, y = wave.rate, wave.data.ravel().astype(float)
			mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr,
												n_mfcc=const.N_MFCCS).T,
						   axis=0)
			numpied = np.array([mfcc])
		return self._normalize(numpied)

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
