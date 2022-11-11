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


# root window is the parent window
fram = Frame(root)
xx = 200
yy = 200
# adding label to search box
Label(fram, text='Text to find:').pack(side=LEFT)
Frame(root, bg="#bbf0f1", bd=400, height=250, width=500,
      cursor="target").place(x=xx-50, y=yy-100)
name_label = Label(root, text='Search',  fg="#105c66",
                   bg="#bbf0f1", font=(
                       'calibre', 14, 'bold')).place(x=xx, y=yy-50)
# adding of single line text box
edit = Entry(fram)

# positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

# setting focus
edit.focus_set()

# adding of search button
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

# text box in root window
text = Text(root)

# text input area at index 1 in text window
text.insert('1.0', '''Type your text here''')
text.pack(side=BOTTOM)


# function to search string in text
def find():

    # remove tag 'found' from index 1 to END
    text.tag_remove('found', '1.0', END)

    # returns to widget currently in focus
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            # searches for desired string from index 1
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx:
                break

            # last index sum of current index and
            # length of text
            lastidx = '%s+%dc' % (idx, len(s))

            # overwrite 'Found' at idx
            text.tag_add('found', idx, lastidx)
            idx = lastidx

        # mark located string as red
        text.tag_config('found', foreground='red')
    edit.focus_set()


butt.config(command=find)

# mainloop function calls the endless loop of the window,
# so the window will wait for any
# user interaction till we close it
root.mainloop()
