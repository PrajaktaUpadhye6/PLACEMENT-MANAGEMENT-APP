import tkinter
from tkinter import *
from tkinter import ttk
from subprocess import call
from PIL import ImageTk, Image
import ttkbootstrap as tb
import pandas as pd


root = Tk()
root.title("Candidate Registration")
root.configure(background="white")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
img= Image.open("naseoh logo.jpg")
test=ImageTk.PhotoImage(img)
label=tkinter.Label(image=test)
label.image=test


label.pack()

my_style= tb.Style()
my_style.configure('success.Outline.TButton',font=('Helvetica',18,'bold'),width=50,padx=30,pady=30)

def stu_regis():
    root.destroy()
    call(["python","studentregisteration.py"])

b1 =ttk.Button(text="Registration",command=stu_regis,style="success.Outline.TButton")
# b1.place(x=380, y=140)

def stu_record():
    root.destroy()
    call(["python","searchsturecord.py"])

b2 = ttk.Button(text="Student Records",  bootstyle="success-outline" , command=stu_record)
# b2.place(x=380, y=210)

def searchcompany():
    root.destroy()
    call(["python","searchcompany.py"])

b3 = ttk.Button(text="Company Details", bootstyle="success-outline", command=searchcompany)
# b3.place(x=380, y=280)

def searchvacancy():
    root.destroy()
    call(["python","searchvacancy.py"])

b4 = ttk.Button(text="Current Vacancy", bootstyle="success-outline", command=searchvacancy)
# b4.place(x=380, y=350)

def studenthiring():
    root.destroy()
    call(["python","studenthiring.py"])

b5 = ttk.Button(text="Non Placed Students", bootstyle="success-outline", command=studenthiring)
# b5.place(x=380, y=420)

def searchplacement():
    root.destroy()
    call(["python","searchplacement.py"])

b6 = ttk.Button(text="Placement Details", bootstyle="success-outline", command=searchplacement)
# b6.place(x=380, y=490)

def searchfeedback():
    root.destroy()
    call(["python","searchfeedback.py"])

b7 = ttk.Button(text="Feedback", bootstyle="success-outline", command=searchfeedback)
# b7.place(x=380, y=560)

def searchselfemp():
    root.destroy()
    call(["python","searchselfemp.py"])

b8 = ttk.Button(text="Self Employment ", bootstyle="success-outline", command=searchselfemp)
# b8.place(x=380, y=630)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()


l1=Label(root,text="Developed by VES Institute of Technology",font=("Helvetica",12,'bold'),fg="black").pack(pady=5)
image = Image.open("vesitlogo.png")
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.pack(pady=5)
root.mainloop()