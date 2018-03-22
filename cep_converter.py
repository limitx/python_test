#!/usr/bin/env python3

from tkinter import *
#from encrypt import Encrypt
import os
import sys
 

class cep_converter(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("CEP converter: Decimal to ASCII")    
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        # inputText

        self.inputText0 = Label(self, text='input:', width=10)
        self.inputText0.grid(row=0, column=0)
        self.inputField0 = Text(self,height=10, width=35)
        self.inputField0.configure(font=("Calibri", 12))
        self.inputField0.grid(row=0, column=1, columnspan=1)

        self.inputText = Label(self, text='output:', width=10)
        self.inputText.grid(row=1, column=0)

        #self.inputField = Entry(self,textvariable=1,width=50)

        self.inputField = Text(self, height=16, width=35)
        self.inputField.configure(font=("Calibri", 12))
        self.inputField.grid(row=1, column=1, columnspan=2)


        # Button
        self.new = Button(self)
        self.new["text"] = "Convert"
        self.new.grid(row=2, column=1)
        self.new["command"] =  self.convertToASCII
        self.displayText = Label(self)
        self.displayText["text"] = "minche_li@2017"
        self.displayText.grid(row=3, column=0, columnspan=3)


    def convertToASCII(self):
        print ("convertToASCII")

        inputData = self.inputField0.get("1.0","end-1c")

        #inputData = "12, 13, -1, -1, -1, -1, 16, 3, 24, -47, 1, 32, 0, 10, -98, 4, 60, 63, 120, 109, 108, 32, 118, 101, 114, 115, 105, 111, 110, 61, 34, 49, 46, 48, 34, 32, 101, 110, 99, 111, 100, 105, 110, 103, 61, 34, 85, 84, 70, 45, 56, 34, 63, 62, 32, 60, 99, 111, 110, 102, 101, 114, 101, 110, 99, 101, 45, 105, 110, 102, 111, 32, 120, 109, 108, 110, 115, 61, 34, 117, 114, 110, 58, 105, 101, 116, 102, 58, 112, 97, 114, 97, 109, 115, 58"
        array = inputData.split(', ')

        #print (inputData)
        #print (array)

        out = []

        for item in array:
            #print (item)
            #print(int(item))

            tmp = int(item)

            if(tmp > 31) or (tmp == 10):
                #print(chr(int(item)))
                out.append(chr(int(item)))
            if(tmp == 62):
                out.append('\n')


        s = "".join(out)

        print(s)

        self.updateOuptput(s)


    def updateOuptput(self, s):
        # for Text widget
        self.inputField.delete('1.0',END)
        self.inputField.insert('1.0',s)

        # for Entry widget
        #self.inputField.delete(0,END)
        #self.inputField.insert(0,key)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        print ("no UI+")
        app = cep_converter()
        app.grep()
    else:
        root = Tk()
        app = cep_converter(master=root)
        app.mainloop()
