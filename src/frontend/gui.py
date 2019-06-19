from tkinter import *

import src.other.garcon as gc

class GUI:
	def __init__(self):
		self._root = None
		self._canvas = None
		self._rec_button = None

	def init(self):
		gc.enter_func()
		self._root = Tk()
		self._canvas = Canvas(self._root, width=200, height=200, borderwidth=0,
							  highlightthickness=0, bg='black')
		self._init_rec_button()

	def run(self):
		gc.enter_func()
		self._root.mainloop()

	def record(self):
		gc.enter_func()
		pass

	def show_emotion(self, emotion):
		gc.enter_func()
		pass

	def should_exit(self):
		gc.enter_func()
		pass

	def _init_rec_button(self):
		x, y, r = 100, 120, 50
		record = canvas.create_oval(x - r, y - r, x + r, y + r, fill='red',
									tags='record')
		canvas.tag_bind('record', '<Button-1>', self._click)
		canvas.pack()

	def _click(self, *args):
		print('You are now recording')
