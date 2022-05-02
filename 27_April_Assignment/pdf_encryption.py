# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:25:21 2022

@author: suman
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import hashlib

# take the path using tkinter
def rot13(text):
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return text.translate(rot13trans)


def pdf_encrypt():
    ipath = "D:\Downloads\pdfs"
    files = os.listdir(ipath)
    
    for x in files:
        w = PdfFileWriter()
        if x.endswith('.pdf'):
            # take path using tkinter 
            loc = "D:\\Downloads\\pdfs\\"+x
            file = PdfFileReader(loc)
            if file.isEncrypted == False:
                num = file.numPages
                for index in range(num):
                    page = file.getPage(index)
                    w.addPage(page)
                # Dynamic file password    
                password = 'incendero' + x.replace('.pdf', '')
                w.encrypt(password)
                fpath = x.replace('.pdf', '')+"_encrypted.pdf"
                with open(os.path.join(os.getcwd(), fpath), "wb") as f:
                    w.write(f)
                encrypter = hashlib.sha256()
                encrypter.update(password.encode()) 
                encrypted_pass_1 = encrypter.hexdigest()
                encrypted_pass_2 = rot13(password)

