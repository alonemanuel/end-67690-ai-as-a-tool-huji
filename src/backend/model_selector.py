import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, cross_val_predict

import src.other.constants as const
import src.other.garcon as gc
from src.other.constants import Models

class ModelSelector():
	'''
	Selects the best model for the given learning task.
	'''

	def __init__(self):
		'''
		Inits a model selector.
		'''
		self._X_train, self._y_train = None, None
		self._preprocessor = None
		self._models = {}
		self._scores = {}

	def init(self, proprocessor, X_train, y_train):
		'''
		:param proprocessor:	implementing 'preprocess' method.
		:param X_train:	type=list>filename,	shape=(m,	)
		:param y_train:	type=list>label,	shape=(m,	)
		'''
		gc.enter_func()
		self._preprocessor = proprocessor
		self._init_data(X_train, y_train)
		self._init_models()

	def choose_model(self):
		'''
		Chooses the best model for the learning task.
		:return: A model which is already instantiated.
		'''
		gc.enter_func()
		self._cross_validate_models()
		best_model = max(self._scores, key=self._scores.get)
		chosen_model = (best_model.get_class())()
		chosen_model.fit(self._X_train, self._y_train)
		return chosen_model, best_model.get_name()

	def _init_data(self, X_train, y_train):
		'''
		:param X_train:	type=list>filename,	shape=(m,	)
		:param y_train:	type=list>label,	shape=(m,	)
		'''
		X_prep = self._preprocessor.preprocess(X_train)
		y_prep = np.array(y_train)
		self._X_train, self._y_train = X_prep, y_prep

	def _init_models(self):
		for model in Models:
			self._models[model] = (model.get_class())()

	def _cross_validate_models(self):
		gc.enter_func()
		# learner =
		# pipeline = Pipeline([('vect', vectorizer),
		# 					 ('chi', SelectKBest(chi2, k=18000)),
		# 					 ('clf', LinearSVC(penalty='l2',
		# 									   tol=1e-5))])
		for model_enum, model in self._models.items():
			accuracy = cross_val_score(model, self._X_train, self._y_train,
									   scoring='accuracy', cv=5).mean() * 100
			self._scores[model_enum] = accuracy
			y_pred = cross_val_predict(model, self._X_train, self._y_train)
			self._report(model_enum, self._y_train, y_pred, is_test=False)

	def _report(self, model_enum, y_real, y_pred, is_test=False):
		gc.enter_func()
		cm = confusion_matrix(y_real, y_pred)
		accu_score = '{0:.3f}'.format(accuracy_score(y_real, y_pred))
		cm_df = pd.DataFrame(cm)
		cm_df.rename(columns=const.LABEL_DICT, index=const.LABEL_DICT,
					 inplace=True)
		title_suffix = 'Test set' if is_test else 'Train set'
		gc.init_plt(
				f'{model_enum.get_name()}, {title_suffix}\nAccuracy: '
				f'{accu_score}')
		sns.heatmap(cm_df, annot=True)
		plt.xlabel('True label')
		plt.ylabel('Predicted label')
		fn_suffix = 'testset' if is_test else 'trainset'
		fn_learner_name = model_enum.get_name().replace(' ', '')
		gc.save_plt(f'{fn_learner_name}_{fn_suffix}')

	def _get_models(self):
		gc.enter_func()
		models = {}
