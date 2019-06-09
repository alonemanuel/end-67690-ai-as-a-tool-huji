import os
import time

import speech_recognition as sr

from src.garcon import Garcon

DEF_TXT_PROMPT = ''

DEF_POST_PROMPT = 'Done recording'

DEF_PRE_PROMPT = 'Say something...'

DEF_COUNT_DOWN = 3

gc = Garcon()
RECORDING_DIR = os.path.join('..', 'recordings')
WAVE_FN_EXT = '.wav'

class SpeechRecognizer():
	'''
	Class for recognizing and parsing speech.
	'''

	def __init__(self):
		'''
		Inits a speech recognizer.
		'''
		self.__r = sr.Recognizer()
		self.__record_idx = 0

	def record(self, fn, pre_prompt=DEF_PRE_PROMPT,
			   post_prompt=DEF_POST_PROMPT, txt_prompt=DEF_TXT_PROMPT,
			   parse=False):
		'''
		Records speech from the pc's mic, parses it to text and saves
		it as a		.wav file
		:param record_name: name of recording. 	type=string
		:return: text parsed from recording.	type=string
		'''
		audio_source = self.__record_mic(pre_prompt, post_prompt, txt_prompt)
		self.__save_wav(audio_source, fn)
		if parse:
			return self.__parse(audio_source)

	def __parse(self, audio_source):
		'''
		Parser a piece of audio.
		:param audio_source: audio to parse from
		:return: text parsed
		'''
		text = self.__r.recognize_google(audio_source)
		return text

	def __record_mic(self, pre_prompt, post_prompt, txt_prompt):
		'''
		Records mic and returns an audio
		file of that recording.
		:returns: AudioFile recorded
		'''
		pre_prompt = pre_prompt if pre_prompt else DEF_PRE_PROMPT
		post_prompt = post_prompt if post_prompt else DEF_POST_PROMPT
		with sr.Microphone() as source:
			print()
			time.sleep(2)
			print(pre_prompt)
			time.sleep(2)
			if txt_prompt:
				print('***')
				print(txt_prompt)
				print('***')
				time.sleep()
			self.__countdown()
			audio_source = self.__r.listen(source)
			print(post_prompt)
		return audio_source

	def __countdown(self, count_down=DEF_COUNT_DOWN):
		'''
		Counts down from the given count_down value.
		'''
		for i in range(count_down, 0, -1):
			print(i)
			time.sleep(1)
		print('GO')

	def __save_wav(self, audio_source, fn):
		'''
		Saves an audio source as a .wav file.
		:param audio_source:	type=AudioSource
		:param record_name: 	name of recording
		'''
		wav_data = audio_source.get_wav_data()
		wf_name = os.path.join(fn + WAVE_FN_EXT)
		with open(wf_name, 'wb') as wf:
			wf.write(wav_data)
