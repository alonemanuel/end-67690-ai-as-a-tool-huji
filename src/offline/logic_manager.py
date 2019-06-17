from src.offline.data_getter import DataGetter
import src.garcon2 as gc

class LogicManager():
	'''
	Manages the logic behind the prosody-mate system.
	'''
	def __init__(self):
		self._data_getter = DataGetter()

		self._X_train, self._y_train = None, None
		self._X_test, self._y_test = None, None
		self._init_train_test()

		self._explorer = ModelExplorer()

		self._is_prepared = False

	def _init_train_test(self):
		'''
		Inits (=sets) the train and test data sets.
		'''
		gc.enter_func()
		train, test = self._data_getter.get_train_test()
		self._X_train, self._y_train = train
		self._X_test, self._y_test = test

	def prepare(self, verbose=True):
		'''
		Prepares the ground for the learning task.
		'''
		gc.enter_func()
		self._explore_models()

		self._is_prepared = True

	def _explore_models(self):

		pass

	def get_learner(self):
		gc.enter_func()
		self._expect_is_prepared()
		model = self._choose_model()
		X_all, y_all = self._get_all_data()
		model.fit(X_all, y_all)
		return model

	def _choose_model(self):
		pass

	def _get_all_data(self):
		X_all = np.

	def _expect_is_prepared(self):
		err_msg = "Manager should first prepare() before producing a learner"
		assert self._is_prepared, err_msg
