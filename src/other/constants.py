import os
from enum import Enum

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

MODEL_NAME, MODEL_CLASS = 0, 1

class Models(Enum):
	KNN = 'k-Nearest Neighbors', KNeighborsClassifier
	LOG_REG = 'Logistic Regression', LogisticRegression
	SVM = 'Suport Vector Machines', svm.SVC
	RF = 'Random Forest', RandomForestClassifier

	@staticmethod
	def list():
		return list(map(lambda m: m.value[MODEL_CLASS], Models))

	def get_name(self):
		return self.value[MODEL_NAME]

	def get_class(self):
		return self.value[MODEL_CLASS]


# Directories #
DATA_DIR = os.path.join( '..', 'data')
EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions')

# Learning #
# TEST_RATIO = 0.15
TEST_RATIO = 0.95
N_MFCCS = 40

