import tkinter as tk

import src.other.constants as const

class DebugPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self._init_title()
		self._init_widgets()

	def _init_widgets(self):
		self._init_navigation_buttons()
		self._init_debugging_buttons()

	def _init_debugging_buttons(self):
		pass

	def _init_title(self):
		label = tk.Label(self, text="This is Debug mode",
						 font=self.controller.title_font)
		label.pack(side="top", fill="x", pady=10)

	def _init_navigation_buttons(self):
		button = tk.Button(self, text="Go to the Menu page",
						   command=lambda: self.controller._show_frame(
								   const.MENU_PAGE))
		button.pack(side='bottom', pady=10)
