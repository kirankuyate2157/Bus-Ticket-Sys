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
fram = Frame(root)
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

root.mainloop()
