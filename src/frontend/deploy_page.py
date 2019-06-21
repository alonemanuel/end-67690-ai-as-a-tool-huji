import tkinter as tk
import src.other.constants as const
class DeployPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Deploy page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Menu page",
						   command=lambda: controller._show_frame(const.MENU_PAGE))
        button.pack()

