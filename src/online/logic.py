from src.offline.data_getter import DataGetter
import numpy as np
import src.garcon as gc
from src.offline.model_selector import ModelSelector

class Logic():
	'''
	Manages the logic behind the prosody-mate system.
	'''

	def __init__(self):
		'''
		Inits a logic manager.
		'''
		self._data_getter = DataGetter()

		self._X_train, self._y_train = None, None
		self._X_test, self._y_test = None, None
		self._init_train_test()
		self._is_prepared = False
		self._selector = ModelSelector(self._X_train, self._y_train)

	def init(self, verbose=True):
		'''
		Prepares the ground for the learning task.
		:param verbose:	Should this process be verbose or not?
		'''
		gc.enter_func()
		self._explore_models(report=verbose)
		self._is_prepared = True

	def predict(self, record_fn):
		pass

	def get_predictor(self):
		'''
		Returns a *fitted* model (=predictor) who can now generalize on new
		samples.
		'''
		gc.enter_func()
		# Model should be prepared before it can be used.
		self._expect_prepared()
		chosen_model = self._choose_model()
		X_all, y_all = self._get_all_data()
		chosen_model.fit(X_all, y_all)
		return chosen_model

	def _explore_models(self, report=False):
		'''
		Explored model and
		:return:
		'''
		gc.enter_func()
		self._selector.explore(report=report)

	def _init_train_test(self):
		'''
		Inits (=sets) the train and test data sets.
		'''
		gc.enter_func()
		self._X_train, self._y_train, self._X_test, self._y_test = \
			self._data_getter.get_train_test()

	def _choose_model(self):
		'''
		Chooses the best model and returns it.
		'''
		gc.enter_func()
		model = self._selector.get_chosen_model()
		return model

	def _get_all_data(self):
		'''
		Returns all data known up to now. That is, 'no data left behind'
		type=tuple,	shape=2, where:
			tuple[0]:	type=np.array,	shape=(m,	d)
			tuple[1]:	type=np.array,	shape=(m,	)
		'''
		gc.enter_func()
		X_all = np.row_stack((self._X_train, self._X_test))
		y_all = np.row_stack((self._y_train, self._y_test))
		return X_all, y_all

	def _expect_prepared(self):
		'''
		Expecting manager is already prepared. If not, an assertion exception
		is raised.
		'''
		gc.enter_func()
		err_msg = "Manager should first prepare() before producing a learner"
		assert self._is_prepared, err_msg
