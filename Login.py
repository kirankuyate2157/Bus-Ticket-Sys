from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

master = Tk()
master.title("BUS BOOKING SYSTEM")
master.geometry('900x400')
master['background'] = '#96e6de'


name_var = StringVar()
passw_var = StringVar()
passw_conf = StringVar()
flg = False
# Functions


def loginSubmit():
    name = name_var.get()
    password = passw_var.get()
    print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")
    flg = True
    master.destroy()


def CreateSubmit():
    name = name_var.get()
    password = passw_var.get()
    password2 = passw_conf.get()
    print("The name is : " + name)
    print("The password is : " + password)
    print("The confirm password is : " + password2)
    if(password != password2):
        messagebox.showerror("showerror", "Error password not match !")
    name_var.set("")
    passw_var.set("")
    passw_conf.set("")
    # root2.destroy()


def createAccount():
    root2 = Tk()
    root2.title("BUS BOOKING SYSTEM")
    root2.geometry('900x400')
    root2['background'] = '#96e6de'

    Frame(root2, bg="#105c66", bd=400, height=250, width=500,
          cursor="target").place(x=xx-50, y=yy-100)
    Label(root2, text='Username',  fg="#6edad4",
          bg="#105c66", font=(
              'calibre', 14, 'bold')).place(x=xx, y=yy-50)
    Label(root2, text='Password', fg="#6edad4",
          bg="#105c66", font=(
              'calibre', 14, 'bold')).place(x=xx, y=yy)
    Label(root2, text='confirm Pass', fg="#6edad4",
          bg="#105c66", font=(
              'calibre', 14, 'bold')).place(x=xx-30, y=yy+50)
    Entry(root2, textvariable=name_var,
          font=('calibre', 17, 'normal')).place(x=xx+120, y=yy-50)
    Entry(root2, textvariable=passw_var,
          font=('calibre', 17, 'normal'), show='*').place(x=xx+120, y=yy)
    Entry(root2, textvariable=passw_conf,
          font=('calibre', 17, 'normal'), show='*').place(x=xx+120, y=yy+50)

    Button(root2, text="create", command=CreateSubmit, fg="red",
           font="Times").place(x=xx+150, y=yy+100)
    master.mainloop()


yy = 190
xx = 200
# login page tabs
Label(master, text="Kways Ticket Booking Login ",
      font=('Helvetica 19 bold'),
      fg="#001117",
      bg="#96e6de").place(x=220, y=30)
Frame(master, bg="#105c66", bd=400, height=250, width=500,
      cursor="target").place(x=xx-50, y=yy-100)
name_label = Label(master, text='Username',  fg="#6edad4",
                   bg="#105c66", font=(
                       'calibre', 14, 'bold')).place(x=xx, y=yy-50)
passw_label = Label(master, text='Password', fg="#6edad4",
                    bg="#105c66", font=(
                        'calibre', 14, 'bold')).place(x=xx, y=yy)
name_entry = Entry(master, textvariable=name_var,
                   font=('calibre', 17, 'normal')).place(x=xx+120, y=yy-50)
passw_entry = Entry(master, textvariable=passw_var,
                    font=('calibre', 17, 'normal'), show='*').place(x=xx+120, y=yy)

Button(master, text="Submit", command=loginSubmit, fg="red",
       font="Times").place(x=xx+230, y=yy+80)
Button(master, text="Create", command=createAccount, fg="red",
       font="Times").place(x=xx+100, y=yy+80)
master.mainloop()
