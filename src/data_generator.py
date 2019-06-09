import os
import time

import pandas as pd

from src.speech_recognizer import SpeechRecognizer

LABELS_NON_INT_ERR = 'Error: Labels must be integers'

CHOOSE_DIGIT_PROMPT = 'You must choose a digit from the above options'

CHOOSE_TONE_PROMPT = 'What tone are you speaking in?\nPress the ' \
					 'corresponding digit'

DATA_DIR = os.path.join('..', 'data')
TEXT_FN = os.path.join(DATA_DIR, 'text_to_sample.csv')
LABELS_FN = os.path.join(DATA_DIR, 'labels_to_sample.csv')

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
			key, val = row['key'], row['val']
			try:
				dict[int(key)] = val
			except:
				print(LABELS_NON_INT_ERR)
				exit()
		return dict

	def generate_single_sample(self):
		tone = self.__get_tone_from_user()

	def __get_tone_from_user(self):
		'''
		Recieves tone (label) from user in the cmd line.
		:return: the chosen tone (label)
		'''
		print(CHOOSE_TONE_PROMPT)
		for key, val in self.__labels_dict.items():
			print(f'{key}\t({val.upper()})')
		chosen_tone = input()
		while (not chosen_tone.isdigit()):
			time.sleep(1)
			chosen_tone = input(CHOOSE_DIGIT_PROMPT)
		return chosen_tone

	def generate_predefined_data(self, speak_by_label=False):
		'''
		Generates data by speaking to the microphone.
		:param speak_by_label: should the prompt text be sorted label-wise?
		'''
		self.__init_label_dirs()
		if speak_by_label == True:
			self.__generate_by_label()
		else:
			self.__generate_by_text()

	def __generate_by_label(self):
		'''
		Generates training samples, label-sorted.
		'''
		for key, val in self.__labels_dict.items():
			for rec_idx, text_row in self.__text_df.iterrows():
				text = text_row['text']
				self.__record_predefined_bit(text, val, rec_idx)


	def __generate_by_text(self):
		'''
		Generates training samples, text-sorted.
		'''
		for rec_idx, text_row in self.__text_df.iterrows():
			text = text_row['text']
			for key, val in self.__labels_dict.items():
				self.__record_predefined_bit(text, val, rec_idx)

	def __record_predefined_bit(self, txt_prompt, label_key, rec_idx):
		'''
		Records a predefined bit of audio.
		:param txt_prompt: text to read out
		:param label_val: key of the text
		:param rec_idx: recording index
		'''
		label_val = self.__dict__[label_key]
		tone_prompt = label_val.upper()
		pre_prompt = f'READ the following text OUT LOUD, but be {tone_prompt}'
		txt_prompt = txt_prompt.upper()
		dir_name = self.__get_label_dir_name(label_key)
		fn = os.path.join(dir_name, label_val + f'_rec_{rec_idx}')
		self.__sr.record(fn, pre_prompt, txt_prompt=txt_prompt)

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
			os.makedirs(os.path.join(DATA_DIR, dir_name), exist_ok=True)
