import sqlite3
import tkinter as tk
from tkinter import ttk
import sys
import numpy as np
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
from tabs import Brand
root = Tk()
root.title("BUS BOOKING SYSTEM")
root.geometry('1500x700')
root['background'] = '#96e6de'
character = Image.open("Bus2.png")
character = ImageTk.PhotoImage(character)
L1 = Label(root, image=character, borderwidth=0)
L1.place(x=800, y=10)
Brand(root)
search_var = StringVar()

# function to search string in text


def find():
    name = search_var.get()
    print("The search is : " + name)
    search_var.set("")


# root window is the parent window
xx = 200
yy = 200


# adding label to search box
Frame(root, bg="#bbf0f1", bd=400, height=50, width=500,
      cursor="target").place(x=xx-50, y=yy-50)
name_label = Label(root, text='Search',  fg="#105c66",
                   bg="#bbf0f1", font=(
                       'calibre', 14, 'bold')).place(x=xx-30, y=yy-43)
name_entry = Entry(root, textvariable=search_var, width=22, bg="#defdfd",
                   font=('calibre', 20, 'normal')).place(x=xx+60, y=yy-43)

butt = Button(root, text="🔍", command=find, fg="#105c66",
              bg="#bbf0f1", relief=FLAT, font=(
                  'calibre', 12, 'bold')).place(x=xx+400, y=yy-43)


# Python program to create a table


# def connect():
#     con1 = sqlite3.connect()
#     cur1 = con1.cursor()
#     cur1.execute(
#         "CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
#     con1.commit()
#     con1.close()


# def View():
#     con1 = sqlite3.connect("<path/database_name>")
#     cur1 = con1.cursor()
#     cur1.execute("SELECT * FROM <table_name>")
#     rows = cur1.fetchall()
#     for row in rows:
#         print(row)
#         tree.insert("", tk.END, values=row)
#     con1.close()


# # connect to the database

# connect()

# root = tk.Tk()

# tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

# tree.column("#1", anchor=tk.CENTER)
# tree.heading("#1", text="ID")
# tree.column("#2", anchor=tk.CENTER)
# tree.heading("#2", text="FNAME")
# tree.column("#3", anchor=tk.CENTER)
# tree.heading("#3", text="LNAME")
# tree.pack()

# button1 = tk.Button(text="Display data", command=View)
# button1.pack(pady=10)

root.mainloop()
