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
LABEL_DIR_DICT = {0: '0_happy', 1: '2_sad', 2: '3_angry'}
DIR_LABEL_DICT = {'0_happy': 0, '2_sad': 1, '3_angry': 2}
LABEL_COLOR_DICT = {0: 'yellow', 1: 'blue', 2: 'red'}
COLOR_TO_TEXT_COLOR_DICT = {'yellow': 'black', 'blue': 'white', 'red': 'white'}
LABEL_TEXT_DICT = {0: 'Happy', 1: 'Sad', 2: 'Angry'}

# Learning #
# TEST_RATIO = 0.15
TEST_RATIO = 0.15
N_MFCCS = 100
# N_MFCCS = 13
MAX_REC_LENGTH = 5

# GUI #
# WINDOW_LENGTH = 720
WINDOW_LENGTH = 400
# WINDOW_WIDTH = 1280
WINDOW_WIDTH = 330
TITLE_TXT = 'emotio.'
REC_TXT = 'Record'

RELX_W = 0.25
RELX_E = 0.75
RELY_N = 0.38
RELY_S = 0.79

WIDGET_WIDTH = 13
WIDGET_HEIGHT = 6

HAPPY_LBL = 0
HAPPY_BG = 'yellow'
HAPPY_FG = 'black'
SAD_LBL = 1
SAD_BG = 'blue'
SAD_FG = 'white'
ANGRY_LBL = 2
ANGRY_BG = 'red'
ANGRY_FG = 'white'

MENU_PAGE = 'MenuPage'
DEPLOY_PAGE = 'DeployPage'
DEBUG_PAGE = 'DebugPage'
LEARN_PAGE = 'LearnPage'
EMOTIO_PAGE = 'EmotioPage'
