import os

from sklearn.model_selection import train_test_split

import src.other.constants as const
import src.other.garcon as gc


I = 40

class DataGetter:
	'''
	Gets the initial raw (train + test) data.
	'''

	def __init__(self, data_dir_path=const.EMOTIONS_DIR,
				 test_ratio=const.TEST_RATIO):
		self._data_path = data_dir_path
		self._test_ratio = test_ratio
		self._X_all, self._y_all = None, None

	def init(self):
		'''
		Inits a DataGetter instance and gets it ready for action.
		As part of the init, it collects the data.
		'''
		self._X_all, self._y_all = self._get_all_data()

	def get_train_test(self):
		'''
		Returns train and test data.
		:return:	type=tuple,	shape=4, where:
			tuple[0] = X_train:	type=list,	shape=(m_train,	)
			tuple[1] = y_train:	type=list,	shape=(m_train,	)
			tuple[2] = X_test:	type=list,	shape=(m_test,	)
			tuple[3] = y_test:	type=list,	shape=(m_test,	)
		'''
		gc.enter_func()
		X_train, X_test, y_train, y_test = train_test_split(self._X_all,
															self._y_all,
															test_size=const.TEST_RATIO,
															random_state=73)
		gc.log(len(X_train))
		gc.log(len(y_train))
		gc.log(len(X_test))
		gc.log(len(y_test))
		return X_train, y_train, X_test, y_test

	def _get_all_data(self):
		'''
		Gets the training data from a local dir.
		:return:	type=tuple,	shape=2, where:
			tuple[0] = 	X_all:	type=list,	shape=(m,	)
			tuple[1] = 	y_all:	type=list,	shape=(m,	)
		'''
		gc.enter_func()
		X_all, y_all = [], []
		for label, emotion_dir in enumerate(os.listdir(self._data_path)):
			emotion_dir_path = os.path.join(self._data_path, emotion_dir)
			for recording in os.listdir(emotion_dir_path):
				recording_path = os.path.join(emotion_dir_path, recording)
				X_all.append(recording_path)
				y_all.append(label)
		return X_all, y_all

# def _get_all_data2(self, n_mfcc=N_MFCCS):
# 	'''
# 	Returns raw data as found in data_path
# 	:return:	type=tuple,	shape=2, where:
# 		tuple[0] = X_raw:	type=np.array,	shape=(m,	n_mfcc)
# 		tuple[1] = y_raw:	type=np.array,	shape=(m,	)
# 	'''
# 	gc.enter_func()
# 	X_raw, y_raw = [], []
# 	for label, emotion_dir in enumerate(os.listdir(self._data_path)):
# 		for recording in os.listdir(emotion_dir):
# 			y, sr = self._get_raw_data_from_file(recording)
# 			mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
# 			meaned = np.mean(mfccs.T, axis=0)
# 			X_raw.append(meaned)
# 			y_raw.append(label)
# 	return np.array(X_raw), np.array(y_raw)
#
# def _get_raw_data_from_file(self, fn):
# 	'''
# 	Returns raw data from audio file.
# 	:param fn: filename for .wav file
# 	:return: type=tuple,	shape=2, where:
# 		tuple[0] = waveform:	type=np.array,	shape=(n,	)
# 		tuple[1] = sample rate:	type=scalar>0
# 	'''
# 	return librosa.load(fn)
