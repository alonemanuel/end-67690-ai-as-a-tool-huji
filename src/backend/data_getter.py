import os
import random

from sklearn.model_selection import train_test_split

import src.other.constants as const
import src.other.garcon as gc

I = 40

class DataGetter:
	'''
	Gets the initial raw (train + test) data.
	'''

	def __init__(self, test_ratio=const.TEST_RATIO):
		self._data_path = const.DEPLOY_EMOTIONS_DIR
		self._test_ratio = test_ratio
		self._X_all, self._y_all = self._get_all_data()

	def get_train_data(self):
		'''
		:return:	type=tuple:
			tuple[0]=X:	type=list,	shape=(m,	)
			tuple[1]=y:	type=list,	shape=(m,	)
		'''
		return self._X_all, self._y_all

	def get_train_test(self, test_ratio=const.TEST_RATIO):
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
															test_size=test_ratio, shuffle=True)
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
		for emotion_dir in os.listdir(self._data_path):
			if emotion_dir == '1_surprised':
				continue
			emotion_dir_path = os.path.join(self._data_path, emotion_dir)
			label = const.DIR_LABEL_DICT[emotion_dir]
			for dir in os.listdir(emotion_dir_path):
				inner_dir = os.path.join(emotion_dir_path, dir)
				for recording in os.listdir(inner_dir):
					# Comment/Uncomment this to sample only a third of their
					# recordings
					if dir =='theirs':
						toss = random.randint(0,3)
						if toss:
							continue
					recording_path = os.path.join(inner_dir, recording)
					X_all.append(recording_path)
					y_all.append(label)
		return X_all, y_all
