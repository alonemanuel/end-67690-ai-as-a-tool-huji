import src.garcon as gc

class ModelSelector():
	'''
	Selects the best model for the given learning task.
	'''

	def __init__(self, X_train, y_train, verbose=False):
		'''
		Inits a model selector.
		:param X_train:
		:param y_train:
		'''
		self._verbose = verbose
		self._X_train, self._y_train = None, None
		self._X_validate, self._y_validate = None, None
		self._init_train_validate(X_train, y_train)
		self._has_explored = False
		self._models = self._get_models()

	def _init_train_validate(self, X_train, y_train):
		'''
		Inits a train and validation set.
		:param X_train:	type=np.array,	shape=(m,	d)
		:param y_train: type=np.array,	shape=(m,	)
		'''
		gc.enter_func()
		pass

	def _get_models(self):
		gc.enter_func()
		models = {}

	def explore(self):
		gc.enter_func()
		self._has_explored = True

	def get_chosen_model(self):
		gc.enter_func()
		self._expect_explored()

	def _expect_explored(self):
		'''
		Expecting explorer has already explored. If not, an assertion
		exception is raised.
		'''
		gc.enter_func()
		err_msg = "Model selector should first explore() before " \
				  "choosing a model"
		assert self._has_explored, err_msg
