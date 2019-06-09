import os
import pandas as pd

from src.speech_recognizer import SpeechRecognizer

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
		self.__labels_df = pd.read_csv(LABELS_FN)
		self.__sr = SpeechRecognizer()

	def generate_single_sample(self):
		pass

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
		for _, label_row in self.__labels_df.iterrows():
			label_key, label_val = label_row['key'], label_row['val']
			for rec_idx, text_row in self.__text_df.iterrows():
				text = text_row['text']
				self.__record_predefined_bit(text, label_val, rec_idx)

	def __generate_by_text(self):
		'''
		Generates training samples, text-sorted.
		'''
		for rec_idx, text_row in self.__text_df.iterrows():
			text = text_row['text']
			for _, label_row in self.__labels_df.iterrows():
				label_key, label_val = label_row['key'], label_row['val']
				self.__record_predefined_bit(text, label_val, rec_idx)

	def __record_predefined_bit(self, txt_prompt, label_val, rec_idx):
		'''
		Records a predefined bit of audio.
		:param txt_prompt: text to read out
		:param label_val: label of the text
		:param rec_idx: recording index
		'''
		tone_prompt = label_val.upper()
		pre_prompt = f'READ the following text OUT LOUD, but be {tone_prompt}'
		txt_prompt = txt_prompt.upper()
		dir_name = self.__get_label_dir_name(label_val)
		fn = os.path.join(dir_name,label_val+f'_rec_{rec_idx}')
		self.__sr.record(fn, pre_prompt, txt_prompt=txt_prompt)

	def __get_label_dir_name(self, label_val):
		'''
		Returns the directory path associated with the label.
		'''
		return os.path.join(DATA_DIR, f'{label_val}_recordings')

	def __init_label_dirs(self):
		'''
		Inits (creates) all label-directories.
		'''
		for _, row in self.__labels_df.iterrows():
			val = row['val']
			dir_name = self.__get_label_dir_name(val)
			os.makedirs(os.path.join(DATA_DIR, dir_name), exist_ok=True)
