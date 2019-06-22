from sklearn.linear_model import LogisticRegression

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
		:var _y_train: 	type=list>labels,		shape=(m_train,	)
		:var _X_train: 	type=list>filenames,	shape=(m_test,	)
		:var _X_train: 	type=list>filenames,	shape=(m_train,	)
		'''
		self._learner = LogisticRegression()
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

	def predict(self, record_fns):
		'''
		:param record_fns:	type=list/string,	shape=(m,	)
		:return:			type=list,			shape=(m,	)
		'''
		gc.enter_func()
		X = self._preprocessor.preprocess_X(record_fns)
		prediction = self._learner.predict(X)
		return prediction
