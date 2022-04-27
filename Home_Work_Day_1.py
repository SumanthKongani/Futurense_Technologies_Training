# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:22:00 2022

@author: suman
"""
from PyPDF2 import PdfFileWriter, PdfFileReader
import os


ipath = "D:\Downloads\pdfs"
files = os.listdir(ipath)
print(files)

for x in files:
    w = PdfFileWriter()
    if x.endswith('.pdf'):
        loc = "D:\\Downloads\\pdfs\\"+x
        file = PdfFileReader(loc)
        if file.isEncrypted == False:
            num = file.numPages
            for index in range(num):
                page = file.getPage(index)
                w.addPage(page)
            password = 'incendero'
            w.encrypt(password)
            path = x.replace('.pdf', '')+"_encrypted.pdf"
            with open(os.path.join(os.getcwd(), path), "wb") as f:
                w.write(f)
    f.close()
           
# =============================================================================
# import sqlalchemy
# from sqlalchemy import create_engine as ce
# engine = ce('sqlite:///:memory:', echo=True)
# from sqlalchemy.orm import declarative_base
# base = declarative_base()
# 
# from sqlalchemy import Table, Column, Integer, String, MetaData, DATETIME
# meta = MetaData()
# 
# pdfs = Table(
#    'pdfs', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('num_of_pages', Integer),
#    Column('Date_of_encryption', DATETIME),
# )
# meta.create_all(engine)
# 
# =============================================================================










      

