#!/usr/bin/env python
import os
import sys
import json
import tinker_testUI
import testclass


if len(sys.argv) > 1:
    print ("args1: ", sys.argv[1])
    print ("Tool config Setting UI: ")
# Tool config Setting UI
    ui = tinker_testUI.testUI()
    ui.iniUI()
else:    
    ss = testclass.test()
    path = ss.getFilepath()
    src_path = os.path.dirname(os.path.abspath(__file__))

    print ("++++")
    
    
    print (os.getcwd())
    print (src_path)
    #print (path)
    
    #cmd = "cat "+log_type+"*.txt | grep -iE "+"\""+keys+"\" "      
    #print cmd
    #val = os.system(cmd)  
    #print val
    
    ss.grepx(src_path)
