import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import src.other.constants as const
import src.other.garcon as gc
from src.backend.data_getter import DataGetter
from src.backend.model_selector import ModelSelector
from src.backend.preprocessor import Preprocessor

class Logic():
	'''
	Manages the logic behind the prosody-mate system.
	'''

	def __init__(self):
		'''
		Inits a logic manager.
		:var _X_train: 	type=list>filenames,	shape=(m_train,	)
		:var _y_train: 	type=list>labels,		shape=(m_train,	)
		:var _X_train: 	type=list>filenames,	shape=(m_test,	)
		:var _X_train: 	type=list>filenames,	shape=(m_train,	)
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
		self._preprocessor.init(self._X_train, self._y_train)
		self._model_selector.init(self._preprocessor, self._X_train,
								  self._y_train)
		self._init_model()

	def predict(self, record_fns):
		'''

		:param record_fns:
		:return:
		'''
		gc.log(f'record_fns = {record_fns}')
		X = self._preprocessor.preprocess(record_fns)
		prediction = self._chosen_model.predict(X)
		return prediction

	def _init_data(self):
		self._X_train, self._y_train, self._X_test, self._y_test = \
			self._data_getter.get_train_test()

	def _init_model(self):
		self._chosen_model, self._model_name = \
			self._model_selector.choose_model()
		self._report(self._X_test, self._y_test, is_test=True)
		X_all = self._X_train + self._X_test
		y_all = self._y_train + self._y_test
		# X_all = np.row_stack((self._X_train, self._X_test))
		# y_all = np.row_stack((self._y_train, self._y_test))
		# self._chosen_model.fit(self._X_train, self._y_train)

	# self._model_selector.report(self._chosen_model, self._X_test,
	# 							self._y_test, is_test=True)

	def _report(self, X, y, is_test=False):
		gc.enter_func()
		y_pred = self.predict(X)
		y_real = np.array(y)
		cm = confusion_matrix(y_real, y_pred)
		accu_score = '{0:.3f}'.format(accuracy_score(y_real, y_pred))
		cm_df = pd.DataFrame(cm)
		cm_df.rename(columns=const.LABEL_DICT, index=const.LABEL_DICT,
					 inplace=True)
		title_suffix = 'Test set' if is_test else 'Train set'
		gc.init_plt(
				f'{self._model_name}, {title_suffix}\nAccuracy: '
				f'{accu_score}')
		sns.heatmap(cm_df, annot=True)
		plt.xlabel('True label')
		plt.ylabel('Predicted label')
		fn_suffix = 'testset' if is_test else 'trainset'
		fn_learner_name = self._model_name.replace(' ', '')
		gc.save_plt(f'{fn_learner_name}_{fn_suffix}')
