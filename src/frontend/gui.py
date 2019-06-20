from tkinter import *

from flask import Flask

import src.other.garcon as gc


class GUI:
	def __init__(self):
		self._root = None
		self._canvas = None
		self._rec_button = None
		self._display_txt = None
		self._action_txt = None

	def init(self):
		gc.enter_func()
		self._root = Tk()
		self._canvas = Canvas(self._root)
		self._action_txt = Label(self._root)
		self._action_txt.grid(column=0, row=1)
		# self._canvas = Canvas(self._root, width=200, height=200,
		# borderwidth=0,
		# 					  highlightthickness=0, bg='black')
		self._init_screen()

	# self._init_rec_button()

	def run(self):
		gc.enter_func()
		self._root.mainloop()

	def _record(self, *kwargs):
		gc.enter_func()
		self._start_record_gui()

	def show_emotion(self, emotion):
		gc.enter_func()
		pass

	def should_exit(self):
		gc.enter_func()
		pass

	def _start_record_gui(self):
		gc.enter_func()
		self._action_txt.config(text='recording.', font=('Arial Bold', 50))

	def _init_rec_button(self):
		x, y, r = 100, 120, 50
		record = self._canvas.create_oval(x - r, y - r, x + r, y + r,
										  fill='red', tags='record')
		self._canvas.tag_bind('record', '<Button-1>', self._record)
		self._canvas.pack()

	def _init_screen(self):
		self._root.geometry('350x200')
		self._display_txt = Label(self._root, text='emotio',
								  font=('Arial Bold', 50))
		self._display_txt.grid(column=0, row=0)
		self._canvas.grid(column=1, row=1)
		x, y, r = 100, 120, 50
		record = self._canvas.create_oval(x - r, y - r, x + r, y + r,
										  fill='red', tags='record')
		self._canvas.tag_bind('record', '<Button-1>', self._record)
