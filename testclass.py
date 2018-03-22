import re
import io
import json
import os
import sys


dbg_key = 0
dbg_path = 0
dbg_search = 1

class test():
    
    def grepx(self, path):
        config_path = os.path.dirname(os.path.abspath(__file__)) + "/config"
        text_file = open(config_path, "r")
        type = text_file.readline().strip('\n')
        keys = text_file.readline().strip('\n')
        text_file.close()
        
        #keys = "isVolteEnabledByPlatform|isWfcEnabledByPlatform|updateVolteFeatureValue|updateVideoCallFeatureValue|updateWfcFeatureAndProvisionedValues|updateImsServiceConfig|setProvisionedValue|setFeatureValue"
        #type = "radio*.txt"
        
        print (type + keys)
        
        ffile = os.getcwd() + "/" + "result.txt"
        cmd = "cat "+type+" | grep -iE "+"\""+keys+"\" >" +ffile
        #print (cmd)
        val = os.system(cmd)

    # load search Keys in json.
    def getKey(self):
        src_path = os.path.dirname(os.path.abspath(__file__))+'/data.json'
        with open(src_path) as data_file: 
            data = json.load(data_file)
            #print (data)
            if dbg_key == 1:
                for key in data["ims"]:
                    print (key)
                print ()
        return data
 
    # get search files.
    def getFilepath(self):
        # get Current Working directory
        path = os.getcwd() 

        
        files = os.listdir(path)
        my_list = list()
        if dbg_path == 1:
            print (path)
            print (files)
        for name in files:
            if ".txt" in name:
                #print (name)
                my_list.append(name)
        return my_list

    # search
    def search (self, data, path):
        for file in path:
            with io.open(file, encoding = 'utf8', errors='ignore') as origin_file:
                for line in origin_file:
                    for key in data["ims"]:
                        hit = re.search(key, line, re.IGNORECASE)
                        if hit:
                            if dbg_search == 1:
                                print (key , line)

                                
    #print (max(5, 3))
    def max(a, b):
        return a if a > b else b
