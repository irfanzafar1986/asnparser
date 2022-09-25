# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:52:01 2021

@author: m_irf
"""

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import csv
from tkinter import filedialog
import xlsxwriter
import os
import datetime
root =Tk()
root.configure(background="#AAADBB")
sytle=ttk.Style(root)
ttk.Style().theme_use('alt')
root.geometry('600x300+50+50')
root.title("ASN to Csv")
def getFilePath():
    root.filename=filedialog.askopenfilename(initialdir="C:/users/m_irfan/Downloads",title="Select Your asf/3gpp standard File")
    f = open(root.filename, "r")
    Lines = f.readlines()  
    cT = datetime.datetime.now() 
    res='/resultOf'+str(os.path.basename(root.filename))+cT.strftime("%Y%m%d%H%M%S")+'.xlsx'
    targetFilePath=os.path.dirname(root.filename)+res
    workbook = xlsxwriter.Workbook(targetFilePath)
    worksheet = workbook.add_worksheet()
    end_date=datetime.datetime(2023, 5, 17)
    if datetime.datetime.now() > end_date:
        quit()
    headers = ['']*25
    row=0
    column=0
    for l in Lines:
       if l.find("{")>-1:
           headers[column]=l.strip()
           column=column+1
       if l.find("}")>-1:
           column=column-1
       if (l.find("{") ==-1) and (l.find("}")==-1):
           worksheet.write(row,0,l.strip())
           for c in range (column):    
               worksheet.write(row,c+1,headers[c])
           row=row+1    
    workbook.close()
    Label(root,text= "Result File ::"+targetFilePath+" generated").place(x=100,y=60)
Button(root,text="Select Input File",fg="blue",font="Times 12 bold",command=getFilePath).place(x=100,y=10)
img=PhotoImage(file="izParsers.png")
Label(root,image=img).place(x=400,y=100)
root.mainloop()
