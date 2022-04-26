# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pyautogui
from tkinter import *
from tkinter import filedialog
import os
from datetime import datetime

k = 4
for i in range(5):
    for j in range(5):
        print(' '*k, end = '')
        print('* ' * (i+1), end = '')
        break
    k=k-1   
    print('', end = '\n')

time.sleep(5)

im2 = pyautogui.screenshot()
root = Tk()
folder = filedialog.askdirectory()
ct = datetime.now().replace(microsecond = 0)
form = "%y_%b_%d_%H_%M_%S"
ct = datetime.strftime(ct, form)
filename = 'star1' + ct + '.png'
file = os.path.join(folder, filename)
im2.save(file)
root.withdraw()