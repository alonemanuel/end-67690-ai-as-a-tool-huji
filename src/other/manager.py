import socket

import src.other.garcon as gc
from src.backend.logic import Logic
from src.backend.recorder import Recorder
from src.frontend.gui import GUI

class Manager():
	'''
	The manager of the program. Runs all stuff that needs to run.
	'''

	def __init__(self):
		'''
		Inits a manager.
		'''
		self._logic = Logic()
		self._recorder = Recorder()
		self._gui = GUI(self._recorder, self._logic)

	def run(self):
		gc.enter_func()
		print(socket.gethostbyname(socket.gethostname()))
		self._gui.run()
