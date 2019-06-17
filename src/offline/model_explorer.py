import src.garcon2 as gc

class ModelExplorer():
	def __init__(self, X_train, y_train):
		self._X_train, self._y_train = None, None
		self._X_validate, self._y_validate = None, None
		self._init_train_validate(X_train, y_train)

		self._models = self._get_models()
		self._init_models()

	def _init_train_validate(self, X_train, y_train):
		gc.enter_func()
		pass

	def _get_models(self):
		gc.enter_func()
		models = {}

	def explore(self, report=False):
		gc.enter_func()
		pass
