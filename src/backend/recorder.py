import os
import time

import speech_recognition as sr

import src.other.garcon as gc

MAX_REC_LENGTH = 7

DEF_TXT_PROMPT = ''

DEF_POST_PROMPT = 'Done recording'

DEF_PRE_PROMPT = 'Say something...'

DEF_COUNT_DOWN = 3

RECORDING_DIR = os.path.join('..', '..', 'recordings')
WAVE_FN_EXT = '.wav'

class Recorder():

	@staticmethod
	def check_is_dir(dir_path):
		print(os.path.isdir(dir_path))

	def __init__(self):
		self._r = None
		self._record_idx = 0

	def init(self):
		gc.enter_func()
		self._r = sr.Recognizer()

	def record(self, pre_prompt=DEF_PRE_PROMPT, post_prompt=DEF_POST_PROMPT):
		gc.enter_func()
		fn = self._get_fn()
		audio_source = self._record_mic(pre_prompt, post_prompt)
		self._save_wav(audio_source, fn)
		time.sleep(1)
		return fn

	def _get_fn(self):
		dtime = time.localtime()
		base = []
		for i in range(6):
			base.append(str(dtime[i]))
		base = '_'.join(base)
		fn = os.path.join(RECORDING_DIR, base + WAVE_FN_EXT)
		return os.path.abspath(fn)

	def _record_mic(self, pre_prompt, post_prompt):
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
			time.sleep(1)
			self._countdown()
			audio_source = self._r.listen(source, timeout=1,
										  phrase_time_limit=MAX_REC_LENGTH)
			print(post_prompt)
		return audio_source

	def _countdown(self, count_down=DEF_COUNT_DOWN):
		'''
		Counts down from the given count_down value.
		'''
		for i in range(count_down, 0, -1):
			print(i)
			time.sleep(1)
		print('GO')

	def _save_wav(self, audio_source, fn):
		'''
		Saves an audio source as a .wav file.
		:param audio_source:	type=AudioSource
		:param record_name: 	name of recording
		'''
		wav_data = audio_source.get_wav_data()
		wf_name = os.path.join(fn)
		with open(wf_name, 'wb') as wf:
			wf.write(wav_data)
