from tkinter import *
from tkinter import filedialog
import tkinter as tk
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import urllib.parse
import datetime
import flask


def db():
    global mysql,oracle,mongo
    try:
        b1.destroy()
    except:
        pass
    try:
        lb.destroy()
        back1.destroy()
    except:
        pass
    mysql = Button(root, text="MYSQL", command=dboperation)
    mysql.place(x=240, y=300)
    oracle = Button(root, text="Oracle", command=fun_orc)
    oracle.place(x=540, y=300)
    mongo = Button(root, text="MONGO DB", command=fun_mong)
    mongo.place(x=740, y=300)

def fun_orc():
    global lb,back1
    try:
        mysql.destroy()
        oracle.destroy()
        mongo.destroy()
    except:
        pass
    lb = Label(text="This Operation is not configured.")
    lb.place(x=300,y=10)
    back1 = Button(root, text="Back", command=db)
    back1.place(x=50, y=30)

def fun_mong():
    global lb,back1
    try:
        mysql.destroy()
        oracle.destroy()
        mongo.destroy()
    except:
        pass
    lb = Label(text="This Operation is not configured.")
    lb.place(x=300, y=10)
    back1 = Button(root, text="Back", command=db)
    back1.place(x=50, y=30)

def dboperation():
    global ddl,dml,acid,arch

    try:
        mysql.destroy()
        oracle.destroy()
        mongo.destroy()
    except:
        pass

    try:
        inst.destroy()
        upd.destroy()
        dele.destroy()
        back.destroy()
    except:
        pass
    try:
        lb_ins.destroy()
    except:
        pass
    try:
        lb_upd.destroy()
    except:
        pass
    try:
        lb_del.destroy()
    except:
        pass

    ddl = Button(root, text="DDL", command=fun_ddl)
    ddl.place(x=240, y=300)
    dml = Button(root, text="DML", command=fun_dml)
    dml.place(x=640, y=300)
    acid = Button(root, text="ACID", command=fun_acid)
    acid.place(x=240, y=500)
    arch = Button(root, text="Architecture", command=fun_arch)
    arch.place(x=640, y=500)

def fun_acid():
    pass
def fun_arch():
    pass

def fun_dml():
    global inst,upd,dele,back
    ddl.destroy()
    dml.destroy()
    acid.destroy()
    arch.destroy()
    back = Button(root, text="Back", command=dboperation)
    back.place(x=50,y=30)
    inst = Button(root, text="Insert", command=eg_ins)
    inst.place(x=240, y=300)
    upd = Button(root, text="Update", command=eg_upd)
    upd.place(x=540, y=300)
    dele = Button(root, text="Delete", command=eg_del)
    dele.place(x=740, y=300)

def eg_ins():
    global lb_ins
    try:
        lb_upd.destroy()
    except:
        pass
    try:
        lb_del.destroy()
    except:
        pass
    lb_ins = Label(root, text="""eg. \n INSERT INTO table_name
VALUES (value, value, value  …)""")
    lb_ins.place(x=240,y=500)


def eg_upd():
    global lb_upd
    try:
        lb_ins.destroy()
    except:
        pass
    try:
        lb_del.destroy()
    except:
        pass
    lb_upd = Label(root, text="""eg. \n UPDATE table_name
SET column=value, column=value ..\n
WHERE condition""")
    lb_upd.place(x=240, y=500)

def eg_del():
    global lb_del
    try:
        lb_upd.destroy()
    except:
        pass
    try:
        lb_ins.destroy()
    except:
        pass
    lb_del = Label(root, text="""eg. \n DELETE FROM employees
WHERE department_id = (SELECT department_id FROM departments\n
                       WHERE department_name = 'Sales')""")
    lb_del.place(x=240, y=500)

def fun_ddl():
    pass




global root,b1
root = Tk()
root.geometry("1080x720")
root.configure(bg='blue')

root.title("DB Operation app")


b1 = Button(root, text="DB Operations", command=db)
b1.place(x=440, y=300)


root.mainloop()

