import os
import pandas as pd

from src.speech_recognizer import SpeechRecognizer

DATA_DIR = 'data'
TEXT_FN = os.path.join(DATA_DIR, 'text_to_sample.csv')
LABELS_FN = os.path.join(DATA_DIR, 'labels_to_sample.csv')

class DataGenerator:
	def __init__(self):
		self.__text_df = pd.read_csv(TEXT_FN)
		self.__labels_df = pd.read_csv(LABELS_FN)
		self.__sr = SpeechRecognizer()

	def generate_by_speech(self, speak_by_label=False):
		self.__init_label_dirs()
		if speak_by_label == True:
			self.__generate_by_label()
		else:
			self.__generate_by_text()

	def __generate_by_label(self):
		for _, label_row in self.__labels_df:
			label_key, label_val = label_row['key'], label_row['val']
			for rec_idx, text_row in self.__text_df:
				text = text_row['text']
				self.__record_bit(text, label_val, rec_idx)

	def __generate_by_text(self):
		for rec_idx,text_row in self.__text_df:
			text = text_row['text']
			for _,label_row in self.__labels_df:
				label_key, label_val = label_row['key'], label_row['val']
				self.__record_bit(text, label_val, rec_idx)


	def __record_bit(self, txt_prompt, label_val, rec_idx):
		tone_prompt = label_val.upper()
		pre_prompt = f'READ the following text OUT LOUD, but be {tone_prompt}'
		txt_prompt = txt_prompt.upper()
		fn = self.__get_label_dir_name(label_val) + f'{rec_idx}'
		self.__sr.record(fn, pre_prompt, txt_prompt=txt_prompt)

	def __get_label_dir_name(self, label_val):
		return os.path.join(DATA_DIR, f'{label_val}_recordings')

	def __init_label_dirs(self):
		for _, row in self.__labels_df.iterrows():
			val = row['val']
			dir_name = self.__get_label_dir_name(val)
			os.makedirs(os.path.join(DATA_DIR, dir_name))
