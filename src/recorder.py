import pyaudio
import wave

import os

from src.garcon import Garcon

RECORDING_DIR = os.path.join('..', 'recordings')
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_FN_EXT = '.wav'

gc = Garcon()

class Recorder:
	def __init__(self, recordings_dir=RECORDING_DIR):
		self.__recordings_dir = recordings_dir
		self.__chunk = CHUNK
		self.__format = FORMAT
		self.__channels = CHANNELS
		self.__rate = RATE
		self.__record_seconds = RECORD_SECONDS
		self.__p = pyaudio.PyAudio()
		self.__record_idx = 0

	def record(self, record_name=''):
		gc.enter_func()
		record_name = record_name if record_name else f'record_n{self.record_idx}'
		wf_name = os.path.join(RECORDING_DIR, record_name, WAVE_FN_EXT)
		frames = self.__get_record_frames()
		self.__write_recording(frames, wf_name)

	def __write_recording(self, frames, wf_name):
		with wave.open(wf_name) as wf:
			wf.setnchannels(self.__channels)
			wf.setsampwidth(self.__p.get_sample_size(self.__format))
			wf.setframerate(self.__rate)
			wf.writeframes(b''.join(frames))

	def __get_record_frames(self):
		stream = self.__p.open(format=self.__format, channels=self.__channels,
							   rate=self.__rate, input=True,
							   frames_per_buffer=self.__chunk)
		frames = []
		for i in range(0,
					   int(self.__rate / self.__chunk * self.__record_seconds)):
			data = stream.read(self.__chunk)
			frames.append(data)
		gc.log('Done recording')
		stream.stop_stream()
		stream.close()
		self.__p.terminate()  # When should I actually terminate?
		return frames
