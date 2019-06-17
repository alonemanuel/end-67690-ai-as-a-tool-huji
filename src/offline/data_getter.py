import os
import src.garcon as gc
from sklearn.model_selection import train_test_split
import pandas as pd

DATA_DIR_PATH = os.path.join('..', '..', 'data')
EMOTIONS_DIR_PATH = os.path.join(DATA_DIR_PATH,'emotions')
TRAIN_RATIO = 0.85

class DataGetter:
	'''

	'''

	def __init__(self, data_dir_path=DATA_DIR_PATH, train_ratio=TRAIN_RATIO):
		self._data_path = data_dir_path
		self._train_ratio = train_ratio
		self._X_raw, self._y_raw = self._get_all_data()

	def _get_all_data(self):
		'''
		Returns raw data as found in data_path
		:return:	type=tuple,	shape=2, where:
			tuple[0] = X_raw:	type=np.array,	shape=(m,	d)
			tuple[1] = y_raw:	type=np.array,	shape=(m,	)
		'''
		gc.enter_func()
		raw_data = pd.DataFrame(columns=['']
		for emotion_dir in os.listdir(self._data_path):
			samples = []
			for recording in os.listdir(emotion_dir):

				pass
	def get_train_test(self):
		'''
		Returns train and test data.
		:return:	type=tuple,	shape=2, where:
			tuple[0][0] = X_train:	type=np.array,	shape=(m,	d)
			tuple[0][1] = y_train:	type=np.array,	shape=(m,	)
			tuple[1][0] = X_test:	type=np.array,	shape=(m,	d)
			tuple[1][1] = y_test:	type=np.array,	shape=(m,	)
		'''
		gc.enter_func()
		train = tes

	def _get_raw__data_from_file(self, fn):
		'''
		Returns raw data from audio file.
		:param fn: filename for .wav file
		:return: type=tuple,	shape=2, where:
			tuple[0] = waveform:	type=np.array,	shape=(n,	)
			tuple[1] = sample rate:	type=scalar>0
		'''
		return librosa.load(fn)