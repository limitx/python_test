#!/usr/bin/env python3
from tkinter import *
import toolmanUtils
#from encrypt import Encrypt
import os
import sys
 
from ctypes import cdll
lib2 = cdll.LoadLibrary('./libUtils.so')
ss = toolmanUtils.test()
 
class toolMan(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		master.title("Tool Man")	
		# new C++
		self.obj = lib2.Utils_new()
		
		self.grid()
		self.createWidgets()


	def createWidgets(self):
		self.inputText0 = Label(self, text='configs:', width=10)
		self.inputText0.grid(row=0, column=0)
		self.inputField0 = Text(self,height=1, width=35)
		self.inputField0.configure(font=("Calibri", 12))
		self.inputField0.grid(row=0, column=1, columnspan=6)
		
		self.inputText = Label(self, text='grep keys:', width=10)
		self.inputText.grid(row=1, column=0)
		#self.inputField = Entry(self,textvariable=1,width=50)
		self.inputField = Text(self, height=3, width=35)
		self.inputField.configure(font=("Calibri", 12))
		self.inputField.grid(row=1, column=1, columnspan=6)

		self.new = Button(self)
		self.new["text"] = "save -keys"
		self.new.grid(row=2, column=0)
		self.new["command"] =  self.savekeys
		self.load = Button(self)
		self.load["text"] = "grep"
		self.load.grid(row=2, column=1)
		self.load["command"] =  self.grep()

		self.displayText = Label(self)
		self.displayText["text"] = "minche_li@2017"
		self.displayText.grid(row=3, column=0, columnspan=7)

	def loadMethod(self):
		print ("loadMethod")
		#lib2.loadfile(self.obj)

	def savekeys(self):
		print ("savekeys")
		ss.saveKey(self.inputField.get("1.0","end-1c"))
		self.updateKey()

	def updateKey(self):
		key = ss.loadKey()
		# for Text widget
		self.inputField.delete('1.0',END)
		self.inputField.insert('1.0',key)
		# for Entry widget
		#self.inputField.delete(0,END)
		#self.inputField.insert(0,key)
		
	def grep(self):
		print ("loadMethod")
		lib2.loadkeys(self.obj)
		lib2.loadfile(self.obj)
		lib2.search(self.obj)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		print ("no UI+")
		app = toolMan()
		app.grep()

	else:	
		root = Tk()
		app = toolMan(master=root)
		
		app.updateKey()

		app.mainloop()
