import numpy as np

import src.other.garcon as gc
from src.offline.data_getter import DataGetter
from src.offline.model_selector import ModelSelector
from src.offline.preprocessor import Preprocessor

class Logic():
	'''
	Manages the logic behind the prosody-mate system.
	'''

	def __init__(self):
		'''
		Inits a logic manager.
		'''
		self._data_getter = DataGetter()
		self._model_selector = ModelSelector()
		self._preprocessor = Preprocessor()

		self._X_train, self._y_train = None, None
		self._X_test, self._y_test = None, None

		self._chosen_model = None

	def init(self):
		'''
		Prepares the ground for the learning task.
		:param verbose:	Should this process be verbose or not?
		'''
		gc.enter_func()
		self._data_getter.init()
		self._init_data()
		self._preprocessor.init()
		self._model_selector.init(self._X_train, self._y_train)
		self._init_model()

	def predict(self, record_fn):
		'''

		:param record_fn:
		:return:
		'''
		features = self._preprocessor.preprocess()
		prediction = self._chosen_model.predict(record_fn)
		return prediction

	def _init_data(self):
		self._X_train, self._y_train, self._X_test, self._y_test = \
			self._data_getter.get_train_test()

	def _init_model(self):
		self._chosen_model = self._model_selector.choose_model()
		self._model_selector.report(self._chosen_model, self._X_test,
									self._y_test)
		X_all = np.row_stack((self._X_train, self._X_test))
		y_all = np.row_stack((self._y_train, self._y_test))
		self._chosen_model.fit(X_all, y_all)
