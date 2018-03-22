import tkinter as tk

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
	def __init__(self):
		self.obj = lib.Foo_new()

		
	def iniUI(self):
		win=tk.Tk()
		win.title("My First Tk GUI")
		win.geometry('400x300')

		# UI
		#json_rw

		win.mainloop()

	def bar(self):
		lib.Foo_bar(self.obj)


f = Foo()
f.bar() #and you will see "Hello" on the screen
f.iniUI()
