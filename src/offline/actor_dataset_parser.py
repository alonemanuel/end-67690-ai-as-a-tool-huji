import os
from enum import Enum
import re
import shutil

from src.garcon import Garcon

WAV_EXTN = '.wav'

DATA_DIR = os.path.join('..', 'data')
ACTORS_DIR = os.path.join(DATA_DIR, 'Audio_Speech_Actors_01-24')
EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions')
EMOTION_GROUP = 2

gc = Garcon()

class Grouping(Enum):
	MODALITY = 0
	VOCAL = 1
	EMOTION = 2
	INTENSITY = 3
	STATEMENT = 4
	REPETITION = 5
	ACTOR = 6

class Modality(Enum):
	FULL_AV = '01'
	VIDEO = '02'
	AUDIO = '03'

class Emotion(Enum):
	NEUTRAL = '01'
	CALM = '02'
	HAPPY = '03'
	SAD = '04'
	ANGRY = '05'
	FEARFUL = '06'
	DISGUST = '07'
	SURPRISED = '08'

class Intensity(Enum):
	NORMAL = '01'
	STRONG = '02'

class Statement(Enum):
	KIDS = '01'
	DOGS = '02'

class Repetition(Enum):
	FIRST = '01'
	SECOND = '02'

class ActorDataParser:

	def __init__(self):
		self.__emotions_dict = self.__get_emotions_dict()
		self.__intensity_dict = self.__get_intensity_dict()
		self.__statement_dict = self.__get_statement_dict()
		self.__repetition_dict = self.__get_repetition_dict()
		self.__emotion_dirs_dict = self.__get_emotion_dirs_dict()

	def __get_emotion_dirs_dict(self):
		dict = {}
		for emotion in self.__emotions_dict.values():
			dir_name = os.path.join(EMOTIONS_DIR, emotion)
			dict[emotion] = dir_name
		return dict

	def __open_emotion_dirs(self):
		for dir_name in self.__emotion_dirs_dict.values():
			os.makedirs(dir_name, exist_ok=True)

	def __get_emotions_dict(self):
		dict = {}
		dict['01'] = 'neutral'
		dict['02'] = 'calm'
		dict['03'] = 'happy'
		dict['04'] = 'sad'
		dict['05'] = 'angry'
		dict['06'] = 'fearful'
		dict['07'] = 'disgust'
		dict['08'] = 'surprised'
		return dict

	def __get_intensity_dict(self):
		dict = {}
		dict['01'] = 'normal'
		dict['02'] = 'strong'
		return dict

	def __get_statement_dict(self):
		dict = {}
		dict['01'] = 'kids'
		dict['02'] = 'dogs'
		return dict

	def __get_repetition_dict(self):
		dict = {}
		dict['01'] = '0'
		dict['02'] = '1'
		return dict

	def __get_file_emotion(self, fn):
		print(fn)
		m = re.findall(r'\d\d', fn)
		emotion_code = m[EMOTION_GROUP]
		return self.__emotions_dict[emotion_code]

	def parse(self):
		self.__open_emotion_dirs()

		for actor_dir in os.listdir(ACTORS_DIR):
			gc.log_var(actor_dir=actor_dir)
			for fn in os.listdir(os.path.join(ACTORS_DIR, actor_dir)):
				gc.log_var(fn=fn)
				emotion = self.__get_file_emotion(fn)
				decoded = self.__get_decoded_name(fn, actor_dir)
				src = os.path.join(ACTORS_DIR, actor_dir, fn)
				emotion_dir = self.__emotion_dirs_dict[emotion]
				dest = os.path.join(emotion_dir, decoded)
				shutil.move(src, dest)

	def __get_decoded_name(self, fn, actor_dir):
		grouped = re.findall('\\d\\d', fn)

		emotion = grouped[Grouping.EMOTION.value]
		emotion = self.__emotions_dict[emotion]
		gender = self.__get_gender(grouped[Grouping.ACTOR.value])
		actor = self.__get_actor(actor_dir)
		repetition = grouped[Grouping.REPETITION.value]
		repetition = self.__repetition_dict[repetition]
		intensity = grouped[Grouping.INTENSITY.value]
		intensity = self.__intensity_dict[intensity]
		statement = grouped[Grouping.STATEMENT.value]
		statement = self.__statement_dict[statement]

		segs = [emotion, intensity, statement, gender, actor, repetition]
		return '_'.join(segs) + WAV_EXTN

	def __get_gender(self, gender_encoding):
		digit_char = gender_encoding[-1]
		digit = int(digit_char)
		gender = 'm' if (digit % 2) else 'f'
		return gender

	def __get_actor(self, actor_dir):
		grouped = re.findall('\\d\\d', actor_dir)
		return 'act' + grouped[0]
