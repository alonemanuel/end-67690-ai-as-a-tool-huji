import src.other.garcon as gc
from src.backend.logic import Logic
from src.backend.recorder import Recorder
from src.frontend.gui import GUI

class Manager():
	def __init__(self):
		Recorder.check_is_dir('..\\..\\recordings')

		self._logic = Logic()
		self._recorder = Recorder()
		self._gui = GUI()

	def init(self):
		gc.enter_func()
		self._logic.init()
		self._recorder.init()

		self._gui.init()

	def run(self):
		gc.enter_func()
		self._record_loop()

	# self._gui.run()
	# while not self._gui.should_exit():
	# 	record_fn = self._gui.record()
	# 	emotion = self._logic.predict(record_fn)
	# 	self._gui.show_emotion(emotion)

	def _record_loop(self):
		for i in range(3):
			fn = self._recorder.record()
			label = self._logic.predict(fn)
			print(f'{i}th prediction is: {label}')
