import os

import speech_recognition as sr

from src.garcon import Garcon

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

	def record_and_parse(self, record_name=''):
		'''
		Records speech from the pc's mic, parses it to text and saves it as a
		.wav file
		:param record_name: name of recording. 	type=string
		:return: text parsed from recording.	type=string
		'''
		gc.enter_func()
		audio_source = self.__record_mic()
		self.__save_wav(audio_source, record_name)
		text = self.__r.recognize_google(audio_source)
		return text

	def __record_mic(self):
		'''
		Records mic and returns an audio file of that recording.
		'''
		with sr.Microphone() as source:
			gc.log("Say something")
			audio_source = self.__r.listen(source)
			gc.log('Done recording')
		return audio_source

	def __save_wav(self, audio_source, record_name):
		'''
		Saves an audio source as a .wav file.
		:param audio_source:	type=AudioSource
		:param record_name: 	name of recording
		'''
		wav_data = audio_source.get_wav_data()
		fn = f'record_{self.__record_idx}'
		record_name = record_name if record_name else fn
		wf_name = os.path.join(RECORDING_DIR, record_name + WAVE_FN_EXT)
		with open(wf_name, 'wb') as wf:
			wf.write(wav_data)
		self.__record_idx += 1
