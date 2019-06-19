import os

import scipy.io.wavfile as wav
import librosa
from tqdm import tqdm
import wavio

class Dummy:
	def run(self):
		speech_dir = 'E:\\alon_emanuel_drive\Downloads' \
					 '\Audio_Speech_Actors_01-24'
		song_dir = 'E:\\alon_emanuel_drive\Downloads\Audio_Song_Actors_01-24'
		good = 0
		bad =0

		for dir in os.listdir(speech_dir):
			for file in tqdm( os.listdir(os.path.join(speech_dir, dir))):
				file = os.path.join(speech_dir, dir, file)
				try:
					wavo = wavio.read(file)
				except:
					bad +=1
				else:
					good+=1

		for dir in os.listdir(song_dir):
			for file in tqdm(os.listdir(os.path.join(song_dir, dir))):
				file = os.path.join(song_dir, dir, file)
				try:
					wavo = wavio.read(file)
				except:
					bad +=1
				else:
					good+=1

		print(f'Good: {good}')
		print(f'Bad: {bad}')