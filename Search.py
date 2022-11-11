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

    # remove tag 'found' from index 1 to END
    text.tag_remove('found', '1.0', END)
    # returns to widget currently in focus
    s = search_var
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
    # edit.focus_set()


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
# adding of single line text box
# edit = Entry(fram)

# # positioning of text box
# edit.pack(side=LEFT, fill=BOTH, expand=1)

# # setting focus
# edit.focus_set()

# # adding of search button
# butt = Button(fram, text='Find')
# butt.pack(side=RIGHT)
# fram.pack(side=TOP)

# text box in root window
text = Text(root)

# text input area at index 1 in text window
text.insert('1.0', '''Type your text here''')
text.pack(side=BOTTOM)

# mainloop function calls the endless loop of the window,
# so the window will wait for any
# user interaction till we close it
root.mainloop()
