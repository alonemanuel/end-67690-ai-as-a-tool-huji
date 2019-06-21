import tkinter as tk
import src.other.constants as const

class MenuPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="This is the start page",
						 font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)

		button1 = tk.Button(self, text="Enter Debug mode",
							command=lambda: controller._show_frame(const.DEBUG_PAGE))
		button2 = tk.Button(self, text="Enter Deploy mode",
							command=lambda: controller._show_frame(const.DEPLOY_PAGE))
		button1.pack(side='bottom', pady=10)
		button2.pack(side='bottom')