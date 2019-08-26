import tkinter as tk

import src.other.constants as const

class LearnPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self._init_widgets()
		self.configure(background='white')

	def _init_widgets(self):
		self._init_header()
		self._init_buttons()

	def _init_buttons(self):
		self._init_learn_button()
		self._init_test_button()

	def _init_learn_button(self):
		self._learn_button = tk.Button(self, text='Learn', height=const.WIDGET_HEIGHT,
									   width=const.WIDGET_WIDTH,
									   font=self.controller.button_font,
									   command=self._learn)
		self._learn_button.configure(background='black', foreground='white')
		self._learn_button.place(relx=const.RELX_E, rely=const.RELY_S,
								 anchor=tk.CENTER)

	def _init_test_button(self):
		self._test_button = tk.Button(self,text='Test', height=const.WIDGET_HEIGHT,
									  width=const.WIDGET_WIDTH,
									  font=self.controller.button_font,
									  command=self._test)
		self._test_button.configure(background='black', foreground='white')
		self._test_button.place(relx=const.RELX_W, rely=const.RELY_S,
								anchor=tk.CENTER)

	def _learn(self):
		self.controller.logic.learn()
		self.controller._show_frame(const.EMOTIO_PAGE)

	def _test(self):
		self.controller.logic.test()
		self._test_button.configure(state=tk.DISABLED)

	def _init_header(self):
		self._header = tk.Frame(self)
		self._header.pack(side='top', anchor='w')
		label = tk.Label(self._header, text="emotio.",
						 font=self.controller.title_font)
		label.pack(side="top", fill="x", padx=10, pady=10)
		label.configure(background='white')

		self._header.configure(background='white')

