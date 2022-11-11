from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("BUS BOOKING SYSTEM")
root.geometry('900x400')
root['background'] = '#96e6de'

# Functions


def loginSubmit():
    name = name_var.get()
    password = passw_var.get()
    print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")


name_var = StringVar()
passw_var = StringVar()

yy = 190
xx = 200
# login page tabs
Label(root, text="Kways Ticket Booking Login ",
      font=('Helvetica 19 bold'),
      fg="#001117",
      bg="#96e6de").place(x=220, y=30)
Frame(root, bg="#105c66", bd=400, height=250, width=500,
      cursor="target").place(x=xx-50, y=yy-100)
name_label = Label(root, text='Username',  fg="#6edad4",
                   bg="#105c66", font=(
                       'calibre', 14, 'bold')).place(x=xx, y=yy-50)
passw_label = Label(root, text='Password', fg="#6edad4",
                    bg="#105c66", font=(
                        'calibre', 14, 'bold')).place(x=xx, y=yy)
name_entry = Entry(root, textvariable=name_var,
                   font=('calibre', 17, 'normal')).place(x=xx+120, y=yy-50)
passw_entry = Entry(root, textvariable=passw_var,
                    font=('calibre', 17, 'normal'), show='*').place(x=xx+120, y=yy)

Button(root, text="Submit", command=loginSubmit, fg="red",
       font="Times").place(x=xx+150, y=yy+80)
root.mainloop()
