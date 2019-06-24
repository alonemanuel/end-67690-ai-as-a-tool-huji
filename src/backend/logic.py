import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV

import src.other.constants as const
import src.other.garcon as gc
from src.backend.data_getter import DataGetter
from src.backend.preprocessor import Preprocessor

class Logic():
	'''
	Manages the logic behind the prosody-mate system.
	'''

	def __init__(self):
		'''
		Inits a logic manager.
		:var _X_train: 	type=list>filenames,	shape=(m_train,	)
		:var _y_train: 	type=l	ist>labels,		shape=(m_train,	)
		:var _X_train: 	type=list>filenames,	shape=(m_test,	)
		:var _X_train: 	type=list>filenames,	shape=(m_train,	)
		'''
		# self._learner = LogisticRegression()
		grid = {
			'learning_rate': [0.1, 0.5],
			'n_estimators': [100, 300],
			'max_depth': [3, 9]
		}

		self._learner=GridSearchCV(GradientBoostingClassifier(), grid)
		# self._learner = GridSearchCV(RandomForestClassifier(), grid)
		# self._learner_name = 'Logistic Regression'
		self._learner_name = 'Grid Search CV Boosted'
		self._data_getter = DataGetter()
		self._preprocessor = Preprocessor()

	def learn(self):
		'''
		Basically, fits the learner with the most relevant training data.
		'''
		X_train, y_train = self._data_getter.get_train_data()
		X_prep = self._preprocessor.preprocess_X(X_train)
		y_prep = self._preprocessor.preprocess_y(y_train)
		self._learner.fit(X_prep, y_prep)

	def test(self):
		'''
		Runs the learner through testing.
		'''
		X_train, y_train, X_test, y_test = self._data_getter.get_train_test()
		self._test_simple(X_train, y_train, X_test, y_test)

	def predict(self, record_fns):
		'''
		:param record_fns:	type=list/string,	shape=(m,	)
		:return:			type=list,			shape=(m,	)
		'''
		gc.enter_func()
		X = self._preprocessor.preprocess_X(record_fns)
		prediction = self._learner.predict(X)
		return prediction

	def _test_simple(self, X_train, y_train, X_test, y_test):
		'''
		Tests the model on the training and on the test sets.
		X:	type=list,	shape=(m,	)
		y:	type=list,	shape=(m,	)
		'''
		gc.enter_func()
		X_train_prep = self._preprocessor.preprocess_X(X_train)
		y_train_prep = self._preprocessor.preprocess_y(y_train)
		self._learner.fit(X_train_prep, y_train_prep)
		y_train_pred = self._learner.predict(X_train_prep)
		self._report_train(y_train, y_train_pred)
		y_test_pred = self.predict(X_test)
		self._report_test(y_test, y_test_pred)

	def _report_train(self, y_true, y_pred):
		self._report(y_true, y_pred, is_test=False)

	def _report_test(self, y_true, y_pred):
		self._report(y_true, y_pred, is_test=True)

	def _report(self, y_true, y_pred, is_test):
		gc.enter_func()
		cm = confusion_matrix(y_true, y_pred)
		accu_score = '{0:.3f}'.format(accuracy_score(y_true, y_pred))
		cm_df = pd.DataFrame(cm)
		cm_df.rename(columns=const.LABEL_DIR_DICT, index=const.LABEL_DIR_DICT,
					 inplace=True)
		title_suffix = 'Test set' if is_test else 'Train set'
		gc.init_plt(
				f'{self._learner_name}, {title_suffix}\nAccuracy: '
				f'{accu_score}')
		sns.heatmap(cm_df, annot=True)
		plt.xlabel('True label')
		plt.ylabel('Predicted label')
		fn_suffix = 'testset' if is_test else 'trainset'
		fn_learner_name = self._learner_name.replace(' ', '')
		gc.save_plt(f'{fn_learner_name}_{fn_suffix}', timed=True)
