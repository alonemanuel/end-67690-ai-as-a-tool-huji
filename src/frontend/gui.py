import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3

import src.other.constants as const
from src.frontend.debug_page import DebugPage
from src.frontend.deploy_page import DeployPage
from src.frontend.menu_page import MenuPage
from src.frontend.sample_page import SamplePage
import src.other.garcon as gc

class GUI(tk.Tk):

	def __init__(self, recorder, logic, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.minsize(const.WINDOW_WIDTH, const.WINDOW_LENGTH)

		self.title_font = tkfont.Font(family='Helvetica', size=18,
									  weight="bold")
		self.recorder = recorder
		self.logic = logic

	def run(self):
		self.mainloop()

	def init(self):
		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self._container = tk.Frame(self)
		self._container.pack(side="top", fill="both", expand=True)
		self._container.grid_rowconfigure(0, weight=1)
		self._container.grid_columnconfigure(0, weight=1)
		self._init_pages()
		self._show_frame(const.MENU_PAGE)

	def _init_pages(self):
		self._frames = {}
		for F in (MenuPage, DebugPage, DeployPage, SamplePage):
			gc.log('entered')
			page_name = F.__name__
			frame = F(parent=self._container, controller=self)
			self._frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
		self._frames[MenuPage.__name__].init_navigation()

	def _show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self._frames[page_name]
		frame.tkraise()
