import os
from enum import Enum

from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

MODEL_NAME, MODEL_CLASS = 0, 1

# Models #
class Models(Enum):
	KNN = 'k-Nearest Neighbors', KNeighborsClassifier
	LOG_REG = 'Logistic Regression', LogisticRegression
	SVM = 'Suport Vector Machines', svm.SVC
	RF = 'Random Forest', RandomForestClassifier
	# LASSO = 'Lasso', Lasso
	# ELASTIC = 'Elastic net', ElasticNet
	# MNB = 'Multinomial Naive-Bayes', MultinomialNB
	LDA = 'Linear Discriminant Analysis', LinearDiscriminantAnalysis

	@staticmethod
	def list():
		return list(map(lambda m: m.value[MODEL_CLASS], Models))

	def get_name(self):
		return self.value[MODEL_NAME]

	def get_class(self):
		return self.value[MODEL_CLASS]

CHOSEN_MODEL = LogisticRegression

# Audio #
WAV_EXTN = '.wav'

# Directories #
DATA_DIR = os.path.join('..', '..', 'data')
EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions')
DEPLOY_EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions2')
LABEL_DIR_DICT = {0: '0_happy', 1: '1_surprised', 2: '2_sad', 3: '3_angry'}
DIR_LABEL_DICT = {'0_happy': 0, '1_surprised': 1, '2_sad': 2, '3_angry': 3}

# Learning #
# TEST_RATIO = 0.15
TEST_RATIO = 0.15
N_MFCCS = 40

# GUI #
WINDOW_LENGTH = 720
WINDOW_WIDTH = 1280
TITLE_TXT = 'emotio.'
REC_TXT = 'Record'

MENU_PAGE = 'MenuPage'
DEPLOY_PAGE = 'DeployPage'
DEBUG_PAGE = 'DebugPage'
