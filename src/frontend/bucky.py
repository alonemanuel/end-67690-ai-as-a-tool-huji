from tkinter import *

def _record_pressed():
	hello_lbl.configure(text='Recording...')

window = Tk()
window.title('Welcome to emotio')
window.geometry('350x200')
hello_lbl = Label(window, text='hello', font=('Arial Bold', 50))
hello_lbl.grid(column=0, row=0)

record_btn = Button(window, command=_record_pressed, text='Record',
					bg='red', fg='white')
record_btn.grid(column=1, row=0)

window.mainloop()
