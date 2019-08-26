import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3

import src.other.constants as const
import src.other.garcon as gc
from src.frontend.debug_page import DebugPage
from src.frontend.deploy_page import DeployPage
from src.frontend.emotio_page import EmotioPage
from src.frontend.menu_page import MenuPage
from src.frontend.sample_page import SamplePage
from src.frontend.learn_page import LearnPage

class GUI(tk.Tk):
	'''
	The GUI module of the program.
	'''

	def __init__(self, recorder, logic, *args, **kwargs):
		'''
		Inits the GUI.
		'''
		tk.Tk.__init__(self, *args, **kwargs)
		self.minsize(const.WINDOW_WIDTH, const.WINDOW_LENGTH)
		self.title_font = tkfont.Font(family='Helvetica',size=30,
									  weight="bold")
		self.button_font=tkfont.Font(family='Helvetica', size=15)
		self.recorder = recorder
		self.logic = logic
		self._init_style()

	def run(self):
		'''
		Runs the gui.
		'''

		self.mainloop()

	def _init_appearance(self):
		self.lift()
		self.attributes('-topmost', True)
		# self.attributes('-alpha', 0.85)

	def _init_style(self):
		'''
		Inits the style of the app.
		:return:
		'''
		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self._container = tk.Frame(self)
		self._container.pack(side="top", fill="both", expand=True)
		self._container.grid_rowconfigure(0, weight=1)
		self._container.grid_columnconfigure(0, weight=1)
		self._init_appearance()
		self._init_pages()
		self._show_frame(const.LEARN_PAGE)

	def _init_pages(self):
		'''
		Inits all pages used in the gui.
		:return:
		'''
		gc.enter_func()
		self._frames = {}
		for F in (EmotioPage,LearnPage):
			page_name = F.__name__
			frame = F(parent=self._container, controller=self)
			self._frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
		# self._frames[LearnPage.__name__].init_navigation()

	def _show_frame(self, page_name):
		'''Show a frame for the given page name'''
		gc.enter_func()
		gc.log(page_name)
		frame = self._frames[page_name]
		frame.tkraise()
