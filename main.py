import tkinter as tk
from PIL import Image, ImageTk
import tkinter
import time
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from PIL import ImageTk, Image
from sqlite3 import *
import sqlite3
import Login
from tabs import *

con = sqlite3.Connection('191B052_DATABASE')
root = Tk()
root.title("BUS BOOKING SYSTEM")
root.geometry('1500x700')

root['background'] = '#96e6de'
character = Image.open("Bus2.png")
character = ImageTk.PhotoImage(character)
L1 = Label(root, image=character, borderwidth=0)
L1.place(x=800, y=10)

# Create a label


def show_search_result(li, f, t):
    global root3
    root3 = Tk()
    root3.title("BUS BOOKING SYSTEM")
    root.geometry('1500x700')

    root['background'] = '#96e6de'
    character = Image.open("Bus2.png")
    character = ImageTk.PhotoImage(character)
    L1 = Label(root, image=character, borderwidth=0)
    L1.place(x=800, y=10)
    Brand(root3)
    character = Image.open("Bus2.png")
    character = ImageTk.PhotoImage(character)
    L1 = Label(root3, image=character, borderwidth=0)
    L1.place(x=800, y=60)

    Label(root3, text="BUS ID", font="Arial 15 bold ").place(x=20+40, y=430)
    Label(root3, text="OPERATOR", font="Arial 13 bold ").place(x=233-50, y=430)
    Label(root3, text="TYPE", font="Arial 14 bold ").place(x=316+30, y=430)
    Label(root3, text="FROM", font="Arial 13 bold").place(x=439+40, y=430)
    Label(root3, text="TO", font="Arial 13 bold").place(x=566+20, y=430)
    Label(root3, text="DATE(YYYY/MM/DD)",
          font="Arial 12 bold").place(x=625+30, y=430)
    Label(root3, text="DEPT. TIME", font="Arial 13 bold").place(x=808+30, y=430)
    Label(root3, text="ARR. TIME", font="Arial 13 bold").place(x=931+25, y=430)
    Label(root3, text="SEATS", font="Arial 13 bold").place(x=1054+20, y=430)
    Label(root3, text="FARE(₹) ", font="Arial 13 bold").place(x=1177-20, y=430)
    Label(root3, text="SELECT", font="Arial 13 bold").place(x=1300-40, y=430)

    y = 430
    global i
    # displaying matched records details
    v = IntVar()
    for i in range(0, len(li)):
        y = y+30
        Label(root3, text=li[i][0], font="Arial 15 bold").place(x=130-50, y=y)
        Label(root3, text=li[i][1], font="Arial 15 bold").place(x=220-50, y=y)
        Label(root3, text=li[i][2], font="Arial 15 bold").place(x=350-50, y=y)
        Label(root3, text=li[i][3], font="Arial 15 bold").place(x=530-50, y=y)
        Label(root3, text=li[i][4], font="Arial 15 bold").place(x=630-50, y=y)
        Label(root3, text=li[i][5], font="Arial 15 bold").place(x=740-50, y=y)
        Label(root3, text=li[i][6], font="Arial 15 bold").place(x=910-50, y=y)
        Label(root3, text=li[i][7], font="Arial 15 bold").place(x=1020-50, y=y)
        Label(root3, text=li[i][8], font="Arial 15 bold").place(x=1140-50, y=y)
        Label(root3, text=li[i][9], font="Arial 15 bold").place(x=1222-50, y=y)
        Radiobutton(root3, variable=v, value=1+int(i)).place(x=1290, y=y)

    for i in range(0, len(li)):
        if(v.get()):

            break

    def book_seats(a, y):
        for i in range(0, len(li)):
            if(a.get()):

                break

        bus_id = a.get()-1

        seats = li[bus_id][8]
        seat_list = [0]*int(seats)

        j = 0
        Label(root3, text="Seats Selected").place(x=1000, y=y-400)
        total_seats = Entry(root3)
        total_seats.place(x=1100, y=y-400)

        def add_passenger_details(ts, bus_no, y):

            ts = total_seats.get()

            root3.destroy()
            i = int(int(bus_no.get())-1)

            global root4
            root4 = Tk()
            root4.geometry('430x300')
            Brand(root4)

            Label(root4, text="Passenger Details",
                  font="Arial 17 bold underline").place(x=110, y=1)
            Label(root4, text="Name", font="Arial 12 bold").place(x=85, y=35)
            name = Entry(root4)
            name.place(x=175, y=35)
            Label(root4, text="Age", font="Arial 12 bold").place(x=85, y=70)
            age = Entry(root4)
            age.place(x=175, y=70)
            Label(root4, text="Gender", font="Arial 12 bold").place(x=85, y=105)
            gender = Combobox(root4, height=5, width=17, values=[
                              "Male", "Female", "Others"])
            gender.place(x=175, y=105)
            Label(root4, text="Phone_No", font="Arial 12 bold").place(x=85, y=140)
            phone = Entry(root4)
            phone.place(x=175, y=140)
            Label(root4, text="Email_ID", font="Arial 12 bold").place(x=85, y=175)
            email = Entry(root4)
            email.place(x=175, y=175)

            def confirm_passenger_info(ts):

                a = name.get()
                b = age.get()
                c = gender.get()
                contact = phone.get()
                mail = email.get()
                d = f
                e = t

                date = li[i][4]
                price = li[i][9]
                time = li[i][5]
                left = int(li[i][8])-int(ts)

                x = (i+1, a, b, c, contact, mail, d, e, date, time, price)

                cur = con.cursor()

                if(a == '' or b == '' or c == ''):
                    Label(root4, "OOPS you can't leave any field empty").pack(
                        x=800, y=800)
                else:
                    if(e != d):
                        cur.execute("create table if not exists passenger_details(Bus_Number integer,Booking_Id integer primary key,Passenger_Name varchar(20),Age int(3),Gender varchar(8),Contact_Number int(10),Email_Id varchar(40),From_City char(20),To_City char(20),Date char(12),Time char(7),Price int(100000))")
                        cur.execute(
                            "update bus_records set Number_Of_Seats=? where bus_id=?", (left, li[i][0]))
                        cur.execute(
                            "insert into passenger_details(bus_number,Passenger_Name,Age,Gender,Contact_Number,Email_Id,From_City ,To_City,Date,Time,Price) values(?,?,?,?,?,?,?,?,?,?,?)", x)

                        cur.execute(
                            "select * from passenger_details where Passenger_Name=? and Contact_Number=? and Age=?", (a, contact, b))
                        Label(root4, text="Congrats!!,your seat has been booked",
                              font="Arial 15 ").place(x=10, y=270)
                        con.commit()
                        cur.fetchall()
                        cur.execute(
                            "update bus_records set number_of_seats=? where bus_id=?", (left, i+1))
                        # root4.destroy()
                root4.mainloop()

            Button(root4, text="Cancel",
                   command=lambda: root4.destroy()).place(x=50, y=230)
            Button(root4, text="Book Seat", command=lambda: confirm_passenger_info(
                ts)).place(x=220, y=230)

        Button(root3, text="Submit and Proceed", command=lambda: add_passenger_details(
            total_seats, a, y)).place(x=600, y=y--200)

    Button(root3, text="BOOK", command=lambda: book_seats(
        v, y)).place(x=1200, y=y+50)
    root3.mainloop()


def add_bus():
    root.destroy()
    root1 = Tk()
    root1.title("BUS BOOKING SYSTEM")
    root1.geometry('1500x700')

    root1['background'] = '#96e6de'
    character = Image.open("Bus2.png")
    character = ImageTk.PhotoImage(character)
    L1 = Label(root1, image=character, borderwidth=0)
    L1.place(x=800, y=10)
    Brand(root1)
    frame1 = tk.Frame(root1, bg="#00323e", bd=400, height=300, width=700,
                      cursor="target").place(x=50, y=280)
    Label(root1, text=" Enter The Details Of Bus Operators",  fg="#defdfd",
          bg="#00323e",
          font="Arial 26 bold underline").place(x=70, y=280)
    Label(root1, text="Full Name",   fg="#defdfd",
          bg="#00323e", font="Arial 13 bold ").place(x=95, y=380)
    name = Entry(root1)
    name.place(x=200, y=380)
    Label(root1, text="Contact",  fg="#defdfd",
          bg="#00323e", font="Arial 13 bold ").place(x=95, y=410)
    contact = Entry(root1)
    contact.place(x=200, y=410)
    Label(root1, text="Address",   fg="#defdfd",
          bg="#00323e", font="Arial 13 bold ").place(x=95, y=440)
    add = Entry(root1)
    add.place(x=200, y=440)

    def add_operator_details():
        adx = 830
        ady = 400
        frame1 = tk.Frame(root1, bg="#00323e", bd=400, height=300, width=650,
                          cursor="target").place(x=adx-30, y=ady)
        Label(root1, text="Agency Name", fg="#defdfd",
              bg="#00323e",
              font="Arial 13 bold ").place(x=adx, y=ady+20)
        agency = Entry(root1)
        agency.place(x=adx+150, y=ady+20)
        Label(root1, text="Bus Type", fg="#defdfd",
              bg="#00323e", font="Arial 13 bold ").place(
            x=adx, y=ady+50)
        bus_type = Combobox(root1, height=5, width=17, values=[
                            'NON A/C Sleeper ', 'NON A/C Seater', 'A/C Sleeper', 'A/C Seater'])
        bus_type.place(x=adx+150, y=ady+50)
        Label(root1, text="From", fg="#defdfd",
              bg="#00323e", font="Arial 11 bold ").place(x=adx, y=ady+80)
        start = Combobox(root1, height=5, width=17, values=[
                         'Delhi', 'Banglore', 'Goa', 'Indore', 'Surat', 'Mumbai', 'Pune'])
        start.place(x=adx+150, y=ady+80)
        Label(root1, text="To", fg="#defdfd",
              bg="#00323e", font="Arial 11 bold ").place(x=adx, y=ady+110)
        stop = Combobox(root1, height=5, width=17, values=[
                        'Delhi', 'Banglore', 'Goa', 'Indore', 'Jhansi', 'Mumbai', 'Pune'])
        stop.place(x=adx+150, y=ady+110)
        Label(root1, text="Date(dd/mm/yyyy)", fg="#defdfd",
              bg="#00323e",
              font="Arial 11 bold ").place(x=adx, y=ady+140)
        date = Entry(root1)
        date.place(x=adx+150, y=ady+140)
        Label(root1, text="Departure-Time", fg="#defdfd",
              bg="#00323e",
              font="Arial 11 bold ").place(x=adx, y=ady+170)
        departure = Entry(root1)
        departure.place(x=adx+150, y=ady+170)
        Label(root1, text="Arrival-Time", fg="#defdfd",
              bg="#00323e",
              font="Arial 11 bold ").place(x=adx, y=ady+200)
        arrival = Entry(root1)
        arrival.place(x=adx+150, y=ady+200)
        Label(root1, text="Seats",  fg="#defdfd",
              bg="#00323e", font="Arial 11 bold ").place(x=adx, y=ady+230)
        seats = Entry(root1)
        seats.place(x=adx+150, y=ady+230)
        Label(root1, text="Fare", fg="#defdfd",
              bg="#00323e", font="Arial 11 bold ").place(x=adx, y=ady+260)
        rates = Entry(root1)
        rates.place(x=adx+150, y=ady+260)

        def submit_details():
            a = agency.get()
            b = bus_type.get()
            c = start.get()
            d = stop.get()
            e = str(date.get())
            f = departure.get()
            g = arrival.get()
            h = (seats.get())
            i = (rates.get())
            x = (a, b, c, d, e, f, g, h, i)
            cur = con.cursor()
            if(c != d):
                cur.execute("create table if not exists bus_records(Bus_id integer primary key,Agency char(20),Bus_Type char(20),From_City char(20),To_City char(20),Date Date,Departure_Time char(5),Arrival_Time char(5),Number_Of_Seats int(100),Ticket_Price int(100000))")
                cur.execute(
                    "insert into bus_records(Agency,Bus_Type,From_City,To_City,Date,Departure_Time,Arrival_Time,Number_Of_Seats,Ticket_Price) values(?,?,?,?,?,?,?,?,?)", x)
                Label(root1, text="Record Inserted").place(x=800, y=800)
                con.commit()
            else:
                root1.destroy()
            root1.destroy()

        Button(root1, text="Save And Continue", fg="#00577c",
               command=submit_details).place(x=1300, y=640)

    Button(root1, text="Add Details", fg="#00577c",
           command=add_operator_details).place(x=490, y=380)
    root1.mainloop()


def search_bus():
    root.destroy()
    global root2
    root2 = Tk()
    root2.title("BUS BOOKING SYSTEM")
    root2.geometry('1500x700')
    root2['background'] = '#96e6de'
    character = Image.open("Bus2.png")
    character = ImageTk.PhotoImage(character)
    L1 = Label(root2, image=character, borderwidth=0)
    L1.place(x=800, y=10)
    Brand(root2)
    frame1 = tk.Frame(root2, bg="#00323e", bd=400, height=250, width=400,
                      cursor="target").place(x=280, y=300)
    tk.Label(root2, text="  Bus Search Menu  ",
             fg="#defdfd",
             bg="#00323e",
             font="Helvetica 17 bold italic").place(x=340, y=325)

    tk.Label(root2, text="Bus Type",
             fg="#defdfd",
             bg="#00323e",
             font="Helvetica 12 bold italic").place(x=310, y=365)
    w3 = Combobox(root2, height=5, width=19, values=[
                  'NON A/C Sleeper ', 'NON A/C Seater ', 'A/C Sleeper ', 'A/C Seater', 'All Types'])
    w3.place(x=485, y=365)

    tk.Label(root2, text="Select Boarding",
             fg="#defdfd",
             bg="#00323e",
             font="Helvetica 12 bold italic").place(x=310, y=400)
    w1 = Combobox(root2, height=5, width=19, values=[
                  'Delhi', 'Gorakhpur', 'Goa', 'Indore', 'Jhansi', 'Mumbai', 'Pune'])
    w1.place(x=485, y=400)

    tk.Label(root2, text="Select Destination",
             fg="#defdfd",
             bg="#00323e",
             font="Helvetica 12 bold italic").place(x=310, y=435)
    w2 = Combobox(root2, height=5, width=19, values=[
                  'Delhi', 'Gorakhpur', 'Goa', 'Indore', 'Jhansi', 'Mumbai', 'Pune'])
    w2.place(x=485, y=435)

    def search():
        a = w1.get()
        b = w2.get()
        c = w3.get()
        cur = con.cursor()
        if a != b:

            cur.execute(
                ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bus_records' ''')

            if(c == 'All Types'):

                cur.execute(
                    "select count(*) from bus_records where From_City =? and To_City=?", (a, b))
                if cur.fetchone()[0] == 0:
                    Label(root2, text="BUS NOT FOUND").place(x=800, y=800)

                else:

                    cur.execute(
                        "select * from bus_records where From_City =? and To_City=? and Bus_Type=?", (a, b, c))
                    con.commit()
                    e = cur.fetchall()
                    root2.destroy()
                    show_search_result(e, a, b)
            else:
                cur.execute(
                    "select count(*) from bus_records where From_City =? and To_City=? and Bus_Type=?", (a, b, c))
                if cur.fetchone()[0] == 0:
                    Label(root2, text="RESULT No,("+c+") Bus Found For Destination-" +
                          a+" To-"+b).place(x=800, y=800)

                else:

                    cur.execute(
                        "select * from bus_records where From_City =? and To_City=? and Bus_Type=?", (a, b, c))
                    con.commit()
                    e = cur.fetchall()
                    root2.destroy()
                    show_search_result(e, a, b)

    Button(root2, text="SEARCH", command=search).place(x=500, y=500)
    Button(root2, text="CLOSE", command=lambda: root2.destroy()).place(x=340, y=500)
    root2.mainloop()


Brand(root)

tk.Label(root,
         text="""
Kways has an edge over the other online bus ticket booking platforms in India as we keep implementing
new features keeping in mind the behaviour of our users and the common bus passenger. From Non-AC 
buses to Volvo AC buses and other luxury buses, you can book all types of bus tickets on this platform.\n
🌟 Free Cancellation\t\t\t\t\t\t
🌟 Instant Refunds\t\t\t\t\t\t\t
🌟 Easy & Quick Bus Booking\t\t\t\t\t
🌟 Exciting Cashback & Bus Offers\t\t\t\t\t
🌟 Best Price Assured\t\t\t\t\t\t
🌟 24/7 Customer Assistance\t\t\t\t\t\t
""",
         bg="#96e6de",
         font="Times").place(x=650, y=400)

tk.Label(root, text="""
         Lots of people want to ride with you in the limo,
         but what you want is someone who will take the bus with you
         when the limo breaks down.""",
         font=('Helvetica 16 bold italic', 17),
         fg="#001117",
         bg="#96e6de").place(x=80, y=100)

frame1 = tk.Frame(root, bg="#00323e", bd=400, height=400, width=500,
                  cursor="target").place(x=100, y=250)
tk.Label(root,
         text="Book Your Seats Now ..,",
         fg="#defdfd",
         bg="#00323e",
         font="Helvetica 17 bold italic").place(x=130, y=270)
tk.Label(root,
         text="""Please click on below buttons for
          more information of booking seats 👇""",
         fg="#defdfd",
         bg="#00323e",
         font="Helvetica 16 bold italic").place(x=130, y=310)

tk.Button(root, text="Add Bus", command=add_bus, fg="red",
          font="Times").place(x=200, y=550)
tk.Button(root, text="Search Bus", command=search_bus, fg="#00577c",
          font="Times").place(x=400, y=550)
root.mainloop()
