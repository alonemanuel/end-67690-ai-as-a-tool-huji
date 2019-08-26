import tkinter as tk
from winsound import *

import src.other.constants as const
import src.other.garcon as gc

class EmotioPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		gc.enter_func()
		self._controller = controller
		self._last_record_fn = ''
		self._init_widgets()
		self._place_record()
		self.configure(background='white')

	def _init_widgets(self):
		gc.enter_func()
		# self._widgets = tk.Frame(self, width=350, height=300)
		# self._widgets.pack(side=tk.BOTTOM)
		self._init_header()
		self._init_buttons()

	def _init_record_button(self):
		self._record_button = tk.Button(self, text='Record', height=6,
										width=13,
										font=self._controller.button_font,
										command=self._record)
		self._record_button.configure(background='black', foreground='white')

	def _record(self):
		self._last_record_fn = self._controller.recorder.record(
				shell_verbose=False)
		self._place_play()
		self._place_predict()

	def _place_record(self):
		self._tag_button.place_forget()
		self._result_button.place_forget()
		self._play_button.place_forget()
		self._predict_button.place_forget()
		self._happy_tag_button.place_forget()
		self._angry_tag_button.place_forget()
		self._sad_tag_button.place_forget()
		self._record_button.place(relx=const.RELX_E, rely=const.RELY_S,
								  anchor=tk.CENTER)

	def _init_play_button(self):
		play = lambda: PlaySound(self._last_record_fn, flags=SND_FILENAME)
		self._play_button = tk.Button(self, text='Play', height=6,
									  width=13,
									  font=self._controller.button_font,
									  command=play)
		self._play_button.configure(background='black', foreground='white')

	def _place_play(self):
		self._play_button.place(relx=const.RELX_W, rely=const.RELY_S,
								anchor=tk.CENTER)

	def _init_predict_button(self):
		gc.enter_func()
		self._predict_button = tk.Button(self, text='Predict', height=6,
										 width=13,
										 font=self._controller.button_font,
										 command=self._predict)
		self._predict_button.configure(background='black', foreground='white')

	def _predict(self):
		gc.enter_func()
		gc.log(f'predicting {self._last_record_fn}')
		prediction = self._controller.logic.predict(self._last_record_fn)
		prediction = prediction[0]
		prediction_str = const.LABEL_DIR_DICT[prediction]
		gc.log(f'prediction: {prediction_str}')
		self._place_result(prediction)

	def _place_predict(self):
		self._predict_button.place(relx=const.RELX_E, rely=const.RELY_N,
								   anchor=tk.CENTER)

	def _init_result_button(self):
		gc.enter_func()
		self._result_button = tk.Button(self, text='Result', height=6,
										width=13,
										font=self._controller.button_font,
										command=self._result)
		self._result_button.configure(background='black', foreground='white')

	def _result(self):
		self._record_button.place_forget()
		self._predict_button.place_forget()
		self._play_button.place_forget()
		self._result_button.place_forget()
		self._place_tags()

	def _place_result(self, prediction):
		bg = const.LABEL_COLOR_DICT[prediction]
		fg = const.COLOR_TO_TEXT_COLOR_DICT[bg]
		text = const.LABEL_TEXT_DICT[prediction]
		self._result_button.configure(text=text, bg=bg, fg=fg)
		self._result_button.place(relx=const.RELX_W, rely=const.RELY_N,
								  anchor=tk.CENTER)

	def _init_tag_buttons(self):
		self._tag_button = tk.Button(self, text='Tag',
									 height=const.WIDGET_HEIGHT,
									 width=const.WIDGET_WIDTH,
									 font=self._controller.button_font,
									 bg='black', fg='white',
									 command=self._tag_switch)

		self._happy_tag_button = tk.Button(self, text='Happy',
										   height=const.WIDGET_HEIGHT,
										   width=const.WIDGET_WIDTH,
										   font=self._controller.button_font,
										   command=lambda
											   label=const.HAPPY_LBL: self
										   ._assign_label(label),
										   bg=const.HAPPY_BG,
										   fg=const.HAPPY_FG)

		self._sad_tag_button = tk.Button(self, text='Sad',
										 height=const.WIDGET_HEIGHT,
										 width=const.WIDGET_WIDTH,
										 font=self._controller.button_font,
										 command=lambda
											 label=const.SAD_LBL: self
										 ._assign_label(label),
										 bg=const.SAD_BG,
										 fg=const.SAD_FG)

		self._angry_tag_button = tk.Button(self, text='Angry',
										   height=const.WIDGET_HEIGHT,
										   width=const.WIDGET_WIDTH,
										   font=self._controller.button_font,
										   command=lambda
											   label=const.ANGRY_LBL:
										   self._assign_label(label),
										   bg=const.ANGRY_BG,
										   fg=const.ANGRY_FG)

	def _tag_switch(self):
		self._tag_button.place_forget()
		self._happy_tag_button.place_forget()
		self._sad_tag_button.place_forget()
		self._angry_tag_button.place_forget()
		self._record_button.place(relx=const.RELX_E, rely=const.RELY_S,
								  anchor=tk.CENTER)
		self._place_predict()
		self._place_play()
	def _assign_label(self, label):
		'''
		Assigns a label = moved recording to appropriate dir.
		'''
		print(f'label: {label}')
		self._controller.recorder.labelize_rec(self._last_record_fn,
											   label)
		self._place_record()

	def _place_tags(self):
		self._tag_button.place(relx=const.RELX_W, rely=const.RELY_N,
							   anchor=tk.CENTER)
		self._happy_tag_button.place(relx=const.RELX_E, rely=const.RELY_N,
									 anchor=tk.CENTER)
		self._sad_tag_button.place(relx=const.RELX_E, rely=const.RELY_S,
								   anchor=tk.CENTER)
		self._angry_tag_button.place(relx=const.RELX_W, rely=const.RELY_S,
									 anchor=tk.CENTER)

	def _init_buttons(self):
		self._init_record_button()
		self._init_play_button()
		self._init_predict_button()
		self._init_result_button()
		self._init_tag_buttons()

	# self._prediction_lbl.config(text=prediction_str)

	def _init_translate_button(self):
		pass

	def _init_labels(self):
		pass

	def _init_learn_button(self):
		self._learn_button = tk.Button(text='Learn', height=7, width=14,
									   font=self._controller.button_font,
									   command=self._learn)
		self._learn_button.configure(background='black', foreground='white')
		self._learn_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

	def _init_test_button(self):
		self._test_button = tk.Button(text='Test', height=7, width=14,
									  font=self._controller.button_font,
									  command=self._test)
		self._test_button.configure(background='black', foreground='white')
		self._test_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

	def _learn(self):
		self._controller.logic.learn()
		self._controller._show_frame(const.EMOTIO_PAGE)

	def _test(self):
		self._controller.logic.test()
		self._test_button.configure(state=tk.DISABLED)

	def _init_header(self):
		self._header = tk.Frame(self)
		self._header.pack(side='top', anchor='w')
		label = tk.Label(self._header, text="emotio.",
						 font=self._controller.title_font)
		label.pack(side="top", fill="x", padx=10, pady=10)
		label.configure(background='white')

		self._header.configure(background='white')
