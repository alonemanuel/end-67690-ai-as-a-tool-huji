import os
import time

import pandas as pd

from src.other.garcon import Garcon
from src.other.speech_recognizer import SpeechRecognizer

LABELS_NON_INT_ERR = 'Error: Labels must be integers'

CHOOSE_DIGIT_PROMPT = 'You must choose a digit from the above options'

CHOOSE_TONE_PROMPT = 'What tone are you speaking in?\nPress the ' \
					 'corresponding digit'

DATA_DIR = os.path.join('..', 'data')
TEXT_FN = os.path.join(DATA_DIR, 'text_to_sample.csv')
LABELS_FN = os.path.join(DATA_DIR, 'labels_to_sample.csv')
gc = Garcon()

class TrainDataGenerator:
	'''
	Generates training data.
	'''

	def __init__(self):
		'''
		Inits a new training data generator.
		'''
		self.__text_df = pd.read_csv(TEXT_FN)
		self.__labels_dict = self.__init_label_dict(LABELS_FN)
		self.__recording_counters = {}
		self.__init_label_dirs()  # Also updates counters
		self.__label_rec_counter = {}
		self.__sr = SpeechRecognizer()

	def __init_label_dict(self, labels_fn):
		'''
		Creates a dictionary of labels.
		:param labels_fn: csv file path
		:return: a dict with label keys as keys and label val as values
		'''
		dict = {}
		labels_df = pd.read_csv(labels_fn)
		for _, row in labels_df.iterrows():
			gc.log(row)
			key, val = row['key'], row['val']
			gc.log('made it to here')
			try:
				dict[int(key)] = val
			except:
				print(LABELS_NON_INT_ERR)
				exit()
		return dict

	def generate_single_sample(self):
		label = self.__get_tone_from_user()
		dir_name = self.__get_label_dir_name(label)
		fn = os.path.join(dir_name, )
		self.__sr.record(fn)

	def __get_tone_from_user(self):
		'''
		Recieves tone (label) from user in the cmd line.
		:return: the chosen tone (label) as int
		'''
		print(CHOOSE_TONE_PROMPT)
		for key, val in self.__labels_dict.items():
			print(f'{key}\t({val.upper()})')
		chosen_tone = input()
		while (not chosen_tone.isdigit()):
			time.sleep(1)
			chosen_tone = input(CHOOSE_DIGIT_PROMPT)
		return int(chosen_tone)

	def generate_predefined_data(self, speak_by_label=False):
		'''
		Generates data by speaking to the microphone.
		:param speak_by_label: should the prompt text be sorted label-wise?
		'''
		if speak_by_label == True:
			self.__generate_by_label()
		else:
			self.__generate_by_text()

	def __generate_by_label(self):
		'''
		Generates training samples, label-sorted.
		'''
		for key, val in self.__labels_dict.items():
			for _, text_row in self.__text_df.iterrows():
				text = text_row['text']
				self.__record_predefined_bit(text, key)

	def __generate_by_text(self):
		'''
		Generates training samples, text-sorted.
		'''
		for _, text_row in self.__text_df.iterrows():
			text = text_row['text']
			for key, val in self.__labels_dict.items():
				self.__record_predefined_bit(text, key)

	def __record_predefined_bit(self, txt_prompt, label_key):
		'''
		Records a predefined bit of audio.
		:param txt_prompt: text to read out
		:param label_val: key of the text
		'''
		label_val = self.__labels_dict[label_key]
		tone_prompt = label_val.upper()
		pre_prompt = f'READ the following text OUT LOUD, but be {tone_prompt}'
		txt_prompt = txt_prompt.upper()
		dir_name = self.__get_label_dir_name(label_key)
		rec_idx = self.__get_and_set_samp_idx(label_key)
		fn = os.path.join(dir_name, label_val + f'_rec_{rec_idx}')
		self.__sr.record(fn, pre_prompt, txt_prompt=txt_prompt)

	def __get_and_set_samp_idx(self, label_key):
		'''
		Gets the counter for the current label directory and sets it (++).
		'''
		ret = self.__recording_counters[label_key] + 1
		self.__recording_counters[label_key] += 1
		return ret

	def __get_label_dir_name(self, label_key):
		'''
		Returns the directory path associated with the label.
		'''
		val = self.__labels_dict[label_key]
		return os.path.join(DATA_DIR, f'{val}_recordings')

	def __init_label_dirs(self):
		'''
		Inits (creates) all label-directories.
		'''
		for key, val in self.__labels_dict.items():
			dir_name = self.__get_label_dir_name(key)
			dir_to_open = os.path.join(DATA_DIR, dir_name)
			os.makedirs(dir_to_open, exist_ok=True)
			self.__recording_counters[key] = len(os.listdir(dir_to_open))

	def __del__(self):
		self.__update_recording_counters()

	def __update_recording_counters(self):
		'''
		Updates the sample count for each label directory.
		'''
		labels_df = pd.read_csv(LABELS_FN)
		labels_df['n_of_samples'] = list(self.__recording_counters.values())
		labels_df.to_csv(LABELS_FN)

	

