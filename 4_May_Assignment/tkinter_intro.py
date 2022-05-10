# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:32:49 2022

@author: suman
"""

import tkinter #GUI pyQT
from tkinter import filedialog
import os

root = tkinter.Tk()

folder = filedialog.askdirectory()

print (folder)
file_name =  input("Enter the file name: ") 
if file_name.endswith(".txt"):
    pass
else:
    file_name = file_name + ".txt"

file = os.path.join(folder, file_name) 
file_mode = input("Enter the mode of the file: ") 

if file_mode in ["a", "w", "w+" "r+", "wb", "rb"]:
    pass 
else:
    file_mode="w"

with open (file, file_mode) as file_obj: 
    file_obj.write("hello to python")

root.withdraw()