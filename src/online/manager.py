from src.online.gui import GUI
from src.online.logic import Logic
import src.other.garcon as gc

class Manager():
	def __init__(self):
		self._gui = GUI()
		self._logic = Logic()

	def init(self):
		gc.enter_func()
		self._gui.init()
		self._logic.init()

	def run(self):
		while not self._gui.should_exit():
			record_fn = self._gui.record()
			emotion = self._logic.predict(record_fn)
			self._gui.show_emotion(emotion)
