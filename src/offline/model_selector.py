from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import NearestNeighbors

import src.garcon as gc
import sklearn.linear_model as sk

from src.constants import Models as lm, Models

class ModelSelector():
	'''
	Selects the best model for the given learning task.
	'''

	def __init__(self):
		'''
		Inits a model selector.
		'''
		self._X_train, self._y_train = None, None
		self._models = {}

	def init(self, X_train, y_train):
		gc.enter_func()
		self._init_data(X_train, y_train)
		self._init_models()

	def choose_model(self):
		self._cross_validate_models()

	def report(self, model, X_test, y_test):
		pass

	def _init_data(self, X_train, y_train):
		self._X_train, self._y_train = X_train, y_train

	def _init_models(self):
		for model in Models:
			self._models[model] = (model.get_class())()

	def _cross_validate_models(self):
		gc.enter_func()
		for model_enum, model in self._models.items():
			accuracy = cross_val_score(model, self._X_train, self._y_train,
									   scoring='accuracy', cv=5).mean() * 100
			print(f'Accuracy of {model_enum.get_name()} is {accuracy}')


	def _get_models(self):
		gc.enter_func()
		models = {}

	def choose_model(self):
		gc.enter_func()
