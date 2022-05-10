# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:36:20 2022

@author: suman
"""

import flask
from flask import request, jsonify, Flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

from tkinter import *
#import xlwt           
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import webbrowser
#from tabulate import tabulate
import tkinter as Tk

root=Tk.Tk()
root.geometry('600x500')
root.resizable(0,0)
root.title('Database Tutorial')



x=StringVar() 
y=StringVar()

def home1():
    x.set("")
    y.set("")
     
    f1=Frame()
    f1.place(x=0,y=0,width=1200,height=800)
    f1.configure(background="pink")

    
    b1=Button(f1,text='My SQL',font=('Rockwell Extra Bold',16),bg="#ff6666",fg='black',activebackground="Violet",activeforeground="red",command=MySQL)
    b1.place(x=150,y=50,height=100,width=250)

    b1=Button(f1,text='Oracle',font=('Rockwell Extra Bold',16),bg="#ff6666",fg='black',activebackground="Violet",activeforeground="red",command=nextpage)
    b1.place(x=150,y=180,height=100,width=250)

    b1=Button(f1,text='DB Architecture',font=('Rockwell Extra Bold',16),bg="#ff6666",fg='black',activebackground="Violet",activeforeground="red",command=nextpage)
    b1.place(x=150,y=300,height=100,width=250)
    root.mainloop()

def MySQL():
    x.set("")
    y.set("")
     
    f1=Frame()
    f1.place(x=0,y=0,width=600,height=500)
    f1.configure(background="pink")

    
    b1=Button(f1,text='DB Operations',font=('Rockwell Extra Bold',16),bg="#ff6666",fg='black',activebackground="Violet",activeforeground="red",command=nextpage)
    b1.place(x=150,y=150,height=150,width=250)
    
    b1=Button(f1,text='<- Back',font=('Eras Bold ITC',16),bg='#e67300',fg='white',activebackground="Blue",activeforeground="red",command=home1)
    b1.place(x=400,y=400,height=70,width=100)
    
def nextpage():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="pink")

    b1=Button(f2,text='DML',font=('Eras Bold ITC',16),bg='#ff6666',fg='black',activebackground="purple",activeforeground="red",command=DML)
    b1.place(x=100,y=100,height=100,width=150)

    b1=Button(f2,text='DDL',font=('Eras Bold ITC',16),bg='#ff6666',fg='black',activebackground="purple",activeforeground="red",command=DDL)
    b1.place(x=300,y=100,height=100,width=150)
    
    b1=Button(f2,text='<- Back',font=('Eras Bold ITC',16),bg='#e67300',fg='white',activebackground="Blue",activeforeground="red",command=MySQL)
    b1.place(x=400,y=400,height=70,width=100)

def DML():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")

    b1=Button(f2,text='Insert ',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Insert)
    b1.place(x=100,y=50,height=100,width=150)

    b1=Button(f2,text='Update',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Update)
    b1.place(x=100,y=200,height=100,width=150)

    b1=Button(f2,text='Delete',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Delete)
    b1.place(x=100,y=350,height=100,width=150)
    
    b1=Button(f2,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=nextpage)
    b1.place(x=400,y=400,height=70,width=100)


def Insert():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")
    T = Text(f2, height = 100, width = 150)
    T.pack()
    Fact="INSERT: The INSERT statement is a SQL query. It is used to insert data into the row of a table. \n Syntax: \n INSERT INTO TABLE_NAME    \n INSERT INTO TABVALUES (value1, value2, value3, .... valueN);\n For example:INSERT INTO tablke (Author, Subject) VALUES ('Sonoo', 'DBMS');"  
    T.insert(Tk.END, Fact)
    b1=Button(T,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DML)
    b1.place(x=200,y=200,height=70,width=100)

def Delete():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")
    T2= Text(f2, height = 100, width = 150)
    T2.pack()
    Fact="DELETE: It is used to remove one or more row from a table. \n Syntax:\n DELETE FROM table_name [WHERE condition];  \nFor example:\n DELETE FROM javatpoint  WHERE \n Author='Sonoo';"
    T2.insert(Tk.END, Fact)
    b1=Button(T2,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DML)
    b1.place(x=200,y=200,height=70,width=100)

def Update():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")
    T3 = Text(f2, height = 100, width = 150)
    T3.pack()
    Fact="UPDATE: This command is used to update or modify the value of a column in the table.\n Syntax:\n UPDATE table_name SET [column_name1= value1,...column_nameN = valueN] [WHERE CONDITION]   \n For example:\n UPDATE students    \n SET User_Name = 'Sonoo'  \n WHERE Student_Id = '3'  "
    T3.insert(Tk.END, Fact)
    b1=Button(T3,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DML)
    b1.place(x=200,y=200,height=70,width=100)

def DDL():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")

    b1=Button(f2,text='Create ',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Create)
    b1.place(x=100,y=10,height=80,width=100)

    b1=Button(f2,text='Drop',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Drop)
    b1.place(x=100,y=100,height=80,width=100)

    b1=Button(f2,text='Truncate',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Truncate)
    b1.place(x=100,y=200,height=80,width=100)
    
    b1=Button(f2,text='Alter',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Alter)
    b1.place(x=100,y=300,height=80,width=100)
    
    b1=Button(f2,text='Rename',font=('Eras Bold ITC',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=Rename)
    b1.place(x=100,y=400,height=80,width=100)


    
    b1=Button(f2,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=nextpage)
    b1.place(x=400,y=400,height=70,width=100)

def Create():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#000000")
    T = Text(f2, height = 100, width = 150)
    T.pack()
    Fact=" Create an object. I mean, create a database, table, triggers, index, functions, stored procedures, etc."
    T.insert(Tk.END, Fact)
    b1=Button(T,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DDL)
    b1.place(x=200,y=200,height=70,width=100)

def Drop():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#FFFFFF")
    T = Text(f2, height = 100, width = 150)
    T.pack()
    Fact="This SQL DDL command helps to delete objects. For example, delete tables, delete a database, etc."
    T.insert(Tk.END, Fact)
    b1=Button(T,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DDL)
    b1.place(x=200,y=200,height=70,width=100)
    
def Truncate():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#FF00FF")
    T = Text(f2, height = 100, width = 150)
    T.pack()
    Fact="This SQL DDL command removes records from tables"
    T.insert(Tk.END, Fact)
    b1=Button(f2,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DDL)
    b1.place(x=200,y=200,height=70,width=100)
    
def Rename():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#00FF00")
    T = Text(f2, height = 100, width = 150)
    T.pack()
    Fact="Renaming the database objects"
    T.insert(Tk.END, Fact)
    b1=Button(T,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DDL)
    b1.place(x=200,y=200,height=70,width=100)
    
def Alter():
    f2=Frame()
    f2.place(x=0,y=0,width=600,height=500)
    f2.configure(background="#41E3E9")
    Fact="  Used to alter the existing database or its object structures."
    T = Label(f2,text=Fact)
    T.place(x=0,y=0)
    b1=Button(f2,text='Back',font=('Eras Bold ITC',16),bg='Gray',fg='white',activebackground="Blue",activeforeground="red",command=DDL)
    b1.place(x=200,y=200,height=70,width=100)



@app.route('/', methods=['GET'])

def home():
    return home1()

app.run(host = '192.168.4.30')
