import tkinter as tk
from winsound import *

import src.other.constants as const

class DebugPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self._controller = controller
		self._init_title()
		self._init_widgets()

	def _init_widgets(self):
		self._init_navigation_buttons()
		self._init_debugging_buttons()

	def _init_debugging_buttons(self):
		self._record_btn = tk.Button(self, text='Record something',
						   command=self._record)
		self._record_btn.pack()
		self._init_play_button()

	def _record(self):
		self._last_record_fn = self._controller._recorder.record(
				shell_verbose=False)
		self._play_button.config(state=tk.NORMAL)


	def _init_play_button(self):
		play = lambda :PlaySound(self._last_record_fn,flags=SND_FILENAME)
		self._play_button = tk.Button(self, text='Play last recording',
								  command=play)
		self._play_button.config(state=tk.DISABLED)
		self._play_button.pack(pady=10)



	def _init_title(self):
		label = tk.Label(self, text="This is Debug mode",
						 font=self._controller.title_font)
		label.pack(side="top", fill="x", pady=10)

	def _init_navigation_buttons(self):
		button = tk.Button(self, text="Go to the Menu page",
						   command=lambda: self._controller._show_frame(
								   const.MENU_PAGE))
		button.pack(side='bottom', pady=10)
