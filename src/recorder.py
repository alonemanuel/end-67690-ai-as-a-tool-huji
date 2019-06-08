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
		self.recordings_dir = recordings_dir
		self.chunk = CHUNK
		self.format = FORMAT
		self.channels = CHANNELS
		self.rate = RATE
		self.record_seconds = RECORD_SECONDS

		self.p = pyaudio.PyAudio()
		self.record_idx = 0

	def record(self, record_name=''):
		gc.enter_func()
		record_name = record_name if record_name else f'record_n{self.record_idx}'
		wf_name = os.path.join(RECORDING_DIR, record_name, WAVE_FN_EXT)
		frames = self._get_record_frames()
		self._write_recording(frames, wf_name)

	def _write_recording(self, frames, wf_name):
		with wave.open(wf_name) as wf:
			wf.setnchannels(self.channels)
			wf.setsampwidth(self.p.get_sample_size(self.format))
			wf.setframerate(self.rate)
			wf.writeframes(b''.join(frames))

	def _get_record_frames(self):
		stream = self.p.open(format=self.format, channels=self.channels,
							 rate=self.rate, input=True,
							 frames_per_buffer=self.chunk)
		frames = []
		for i in range(0, int(self.rate / self.chunk * self.record_seconds)):
			data = stream.read(self.chunk)
			frames.append(data)
		gc.log('Done recording')
		stream.stop_stream()
		stream.close()
		self.p.terminate()  # When should I actually terminate?
		return frames
