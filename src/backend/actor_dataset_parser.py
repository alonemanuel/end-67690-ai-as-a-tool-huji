import os
import re
import shutil
from enum import Enum

import src.other.garcon as gc

WAV_EXTN = '.wav'

DATA_DIR = os.path.join('..', 'data')
# ACTORS_DIR = os.path.join(DATA_DIR, 'Audio_Speech_Actors_01-24')
SPEECH_DIR = "E:\\alon_emanuel_drive\Downloads\Audio_Speech_Actors_01-24"
SONG_DIR = "E:\\alon_emanuel_drive\Downloads\Audio_Song_Actors_01-24"
EMOTIONS_DIR = os.path.join(DATA_DIR, 'emotions')
EMOTION_GROUP = 2

class Grouping(Enum):
	'''
	Grouping for regex matching.
	'''
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
	'''
	Parses and rearranges data in actor recordings directory.
	'''

	def __init__(self):
		'''
		Inits a parser instance.
		'''
		self._emotions_dict = self._get_emotions_dict()
		self._intensity_dict = self._get_intensity_dict()
		self._statement_dict = self._get_statement_dict()
		self._repetition_dict = self._get_repetition_dict()
		self._emotion_dirs_dict = self._get_emotion_dirs_dict()

	def parse(self):
		self._parse_specific(song=False)
		self._parse_specific(song=True)

	def _parse_specific(self, song=False):
		self._open_emotion_dirs()
		recordings_dir = SONG_DIR if song else SPEECH_DIR
		for actor_dir in os.listdir(recordings_dir):
			gc.log_var(actor_dir=actor_dir)
			for fn in os.listdir(os.path.join(recordings_dir, actor_dir)):
				# gc.log_var(fn=fn)
				emotion = self._get_file_emotion(fn)
				decoded = self._get_decoded_name(fn, actor_dir, song)
				src = os.path.join(recordings_dir, actor_dir, fn)
				emotion_dir = self._emotion_dirs_dict[emotion]
				dest = os.path.join(emotion_dir, decoded)
				shutil.move(src, dest)
	def _get_emotion_dirs_dict(self):
		dict = {}
		for emotion in self._emotions_dict.values():
			dir_name = os.path.join(EMOTIONS_DIR, emotion)
			dict[emotion] = dir_name
		return dict

	def _open_emotion_dirs(self):
		for dir_name in self._emotion_dirs_dict.values():
			os.makedirs(dir_name, exist_ok=True)

	def _get_emotions_dict(self):
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

	def _get_intensity_dict(self):
		dict = {}
		dict['01'] = 'normal'
		dict['02'] = 'strong'
		return dict

	def _get_statement_dict(self):
		dict = {}
		dict['01'] = 'kids'
		dict['02'] = 'dogs'
		return dict

	def _get_repetition_dict(self):
		dict = {}
		dict['01'] = '0'
		dict['02'] = '1'
		return dict

	def _get_file_emotion(self, fn):
		print(fn)
		m = re.findall(r'\d\d', fn)
		emotion_code = m[EMOTION_GROUP]
		return self._emotions_dict[emotion_code]


	def _get_decoded_name(self, fn, actor_dir, is_song):
		grouped = re.findall('\\d\\d', fn)

		emotion = grouped[Grouping.EMOTION.value]
		emotion = self._emotions_dict[emotion]
		actor = self._get_actor(actor_dir)
		gender = self._get_gender(grouped[Grouping.ACTOR.value])
		audio_type = 'song' if is_song else 'speech'
		repetition = grouped[Grouping.REPETITION.value]
		repetition = self._repetition_dict[repetition]
		intensity = grouped[Grouping.INTENSITY.value]
		intensity = self._intensity_dict[intensity]
		statement = grouped[Grouping.STATEMENT.value]
		statement = self._statement_dict[statement]

		segs = [emotion, audio_type, intensity, statement, actor, gender,
				repetition]
		return '_'.join(segs) + WAV_EXTN

	def _get_gender(self, gender_encoding):
		digit_char = gender_encoding[-1]
		digit = int(digit_char)
		gender = 'm' if (digit % 2) else 'f'
		return gender

	def _get_actor(self, actor_dir):
		grouped = re.findall('\\d\\d', actor_dir)
		return 'act' + grouped[0]
