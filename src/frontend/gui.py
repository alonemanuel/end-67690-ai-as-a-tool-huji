import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3

from src.frontend.debug_page import DebugPage
from src.frontend.deploy_page import DeployPage
from src.frontend.menu_page import MenuPage
import src.other.constants as const

class GUI(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.minsize(const.WINDOW_WIDTH, const.WINDOW_LENGTH)

		self.title_font = tkfont.Font(family='Helvetica', size=18,
									  weight="bold")

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
		self.frames = {}
		for F in (MenuPage, DebugPage, DeployPage):
			page_name = F.__name__
			frame = F(parent=self._container, controller=self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

	def _show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()
