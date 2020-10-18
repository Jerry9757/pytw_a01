# github Pytw_T01, Git 練習

from tkinter import *
from tkinter import ttk


my_window =Tk()
my_window.geometry("400x450")    # window size
my_window.title("Hello tkinter")    # window size

label_one= Label(my_window, text='Message ')
label_one.grid(row=0, column=0)

text_msg=Text(my_window,height=1, width=20)
text_msg.grid(row=0, column=1)
text_msg.insert(END, "Hello world! ")



my_window.mainloop()
