import os
from enum import Enum

from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Lasso, ElasticNet
from sklearn.naive_bayes import MultinomialNB
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


# Labels #
LABEL_DICT = {0:'angry',1:'calm',2:'disgust',3:'fearful',4:'0_happy',5:'neutral',
			  6:'2_sad',7:'surprised'}
# LABEL_DICT[0] = 'neutral'
# LABEL_DICT[1] = 'calm'
# LABEL_DICT[2] = '0_happy'
# LABEL_DICT[3] = '2_sad'
# LABEL_DICT[4] = 'angry'
# LABEL_DICT[5] = 'fearful'
# LABEL_DICT[6] = 'disgust'
# LABEL_DICT[7] = 'surprised'

# Directories #
DATA_DIR = os.path.join( '..','..', 'data')
EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions')

# Learning #
# TEST_RATIO = 0.15
TEST_RATIO = 0.15
N_MFCCS = 40


# GUI #
WINDOW_LENGTH = 720
WINDOW_WIDTH = 1280
TITLE_TXT= 'emotio.'
REC_TXT = 'Record'

MENU_PAGE='MenuPage'
DEPLOY_PAGE = 'DeployPage'
DEBUG_PAGE ='DebugPage'

