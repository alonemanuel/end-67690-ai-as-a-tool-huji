import pyaudio
import wave
import os

RECORDING_DIR = os.path.join('..','recordings')

class Recorder:
	def __init__(self, recordings_dir =RECORDING_DIR):
		self.recordings_dir = recordings_dir

	def record(self):
		py = pyaudio
		pass