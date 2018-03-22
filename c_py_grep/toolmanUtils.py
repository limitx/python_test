import re
import json
import os


dbg_key = 0
dbg_path = 0
dbg_search = 1

class test():
	def loadConfig(self):
		text_file = open("res/config_python.txt", 'r', encoding='UTF-8')
		config = text_file.readline()  
		print (config)
		return config

	def loadKey(self,):
		text_file = open("res/keys_src.txt", 'r', encoding='UTF-8')
		key = text_file.readline()  
		print (key)
		return key

	def saveKey(self, key):
		text_file = open("res/keys_src.txt", 'w', encoding='UTF-8')
		text_file.write(key)

	def getFilepath(self):
		# get Current Working directory
		path = os.getcwd() 
		# get Print Working directory
		# path = os.getpwd() 
		
		files = os.listdir(path)
		my_list = list()
		if dbg_path == 1:
			print (path)
			print (files)
			print ()
		for name in files:
			if ".txt" in name:
				#print (name)
				my_list.append(name)
		print ()
		return my_list
