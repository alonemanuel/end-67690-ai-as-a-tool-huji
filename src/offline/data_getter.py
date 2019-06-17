import os
import src.garcon2 as gc

DATA_DIR_PATH = os.path.join('..', 'data')

class DataGetter:

	def __init__(self, data_dir_path=DATA_DIR_PATH):
		self._dir_path = data_dir_path

	def get_train_test(self):
		'''
		Returns train and test data.
		:return:	type=tuple,	shape=(2, m, d)
		'''
		gc.enter_func()