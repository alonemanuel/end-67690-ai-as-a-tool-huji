import librosa
import numpy as np
from tqdm import tqdm
import scipy.io.wavfile as wav
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
		mfccs = []
		for fn in tqdm(filenames):
			try:
				sr, y = wav.read(fn)
			except:
				print(fn)
				# y, sr = librosa.load(fn)
			else:
				mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=const.N_MFCCS)
				mfccs.append(mfcc)
		return np.array(mfccs)

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
