import tkinter
from tkinter import ttk
from subprocess import call
import ttkbootstrap as tb
from tkinter import *
from PIL import ImageTk ,Image
import sqlite3


# open databse


# defining login function
def login():
    # getting form data
    uname =username.get()
    pwd =password.get()
    # applying empty validation
    if uname=='' or pwd=='':
        message.set("Fill the empty field!!!")
    else:
        # open database
        conn = sqlite3.connect('NASEOH.db')
        # select query
        cursor = conn.execute('SELECT * from login where USERNAME="%s" and PASSWORD="%s" ' %(uname ,pwd))
        # fetch data
        if cursor.fetchone():
            message.set("Login success")
            login_screen.destroy()
            call(["python","home.py"])
        else:
            message.set("Wrong username or password!!!")


# defining loginform function
def Loginform():

    global login_screen
    login_screen = Tk()
    login_screen.title("LOGIN PAGE")
    login_screen.configure(background="white")
    width = login_screen.winfo_screenwidth()
    height = login_screen.winfo_screenheight()
    login_screen.geometry("%dx%d" % (width, height))
    img = Image.open("naseoh logo.jpg")
    test = ImageTk.PhotoImage(img)
    label = tkinter.Label(image=test)
    label.image = test
    label.pack()


    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message =StringVar()


    my_style = tb.Style()
    my_style.configure('success.Outline.TButton', font=('Helvetica', 18, 'bold'), width=10, padx=30, pady=30)


    #Text(login_screen,highlightcolor='black',highlightbackground='black',highlightthickness=5,width=150,height=30).place(x=300,y=200)
    uname_label = Label(login_screen, text='USERNAME',font=("Arial" ,20 ,"bold"), background="white")
    uname_label.pack()
    uname_entry = Entry(login_screen, textvariable=username ,highlightthickness=2, highlightbackground="green", highlightcolor="black", width=25,font=("Arial" ,15 ,"bold"))
    uname_entry.pack()

    pwd_label = Label(login_screen, text='PASSWORD',font=("Arial" ,20 ,"bold"), background="white")
    pwd_label.pack()
    pwd_entry = Entry(login_screen, textvariable=password ,show='*',highlightthickness=2, highlightbackground="black", highlightcolor="black", width=25,font=("Arial" ,15 ,"bold"))
    pwd_entry.pack()

    Label(login_screen, text="", textvariable=message, fg="#1C2833", bg="white", font=("Arial", 16, "bold")).pack()

   # Button(login_screen, text="LOGIN", width=10, height=1, command=login, bg="#0E6655", fg="black",font=("Arial", 12, "bold"), ).place(x=200, y=350)
    b1 = ttk.Button(text="LOGIN", command=login, style="success.Outline.TButton")
    b1.pack()

    l1 = Label(login_screen, text="Developed by VES Institute of Technology", font=("Helvetica", 12, 'bold'), fg="black").pack()
    image = Image.open("vesitlogo.png")
    resize_image = image.resize((50, 50))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(image=img)
    label1.image = img
    label1.pack()
    login_screen.mainloop()


# calling function Loginform
Loginform()