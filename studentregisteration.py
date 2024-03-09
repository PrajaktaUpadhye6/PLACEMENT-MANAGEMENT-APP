from tkinter import *
from tkinter import filedialog
import fpdf
import sqlite3
from tkinter import messagebox
from tkcalendar import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Candidate Registration")
root.configure(background="white")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
image = Image.open("naseoh logo.jpg")
resize_image = image.resize((480,100))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.grid(row=0,column=1)

def submit():
    cid = cid_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    # gender = gender_dropdown.get()
    gender = selected_option.get()
    age = age_entry.get()
    ic = selected_ic.get()
    iccourse = selected_iccourse.get()
    contact = contact_entry.get()
    address = address_entry.get()
    disability = selected_disab.get()
    disabtype = disabtype_entry.get()
    quali = quali_entry.get()
    camp = selected_camp.get()
    remarks = remarks_entry.get()
    placement = selected_placement.get()
    camploc = camploc_entry.get()
    date = date_entry.get()

    print("ID " + cid)
    print("NAME " + name)
    print("EMAIL" + email)
    print("GENDER " + gender)
    print("Contact" + contact)
    print("Address" + address)
    print("disability" + disability)
    print("type" + disabtype)
    print("qualification" + quali)
    print("Internal Candidate" + ic)
    print("age" + age)
    print("Internal Candidate Course" + iccourse)
    print("Camp" + camp)
    print("Camp Loc" + camploc)
    print("Remark" + remarks)
    print("placement" + placement)
    print("date" + date)

    conn = sqlite3.connect("NASEOH.db")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * from registration WHERE cid='" + cid + "'")
        if cursor.fetchone():

            global result
            result = 1

        else:
            result = 0

        if (result == 0):
            cursor = conn.cursor()

            query = "INSERT OR REPLACE INTO registration (name,email,gender,cid,age,contact,address,disability,disabtype,quali,ic,iccourse,camp,camploc,remarks,placement,date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            cursor.execute(query, (
                name, email, gender, cid, age, contact, address, disability, disabtype, quali, ic, iccourse, camp,
                camploc, remarks,
                placement, date))
            messagebox.showinfo("showinfo", "Registration Sucessfull")
            conn.commit()
        else:
            messagebox.showinfo("Error", "Candidate ID already exists")
    except:
        return True


def pick_date(event):
    global cal, date_window

    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Choose Date')
    date_window.geometry('250x250')
    cal = Calendar(date_window, selectmode='day', date_pattern='dd/mm/y')
    cal.place(x=0, y=0)

    sub_btn = Button(date_window, text='Submit', command=grab_date)
    sub_btn.place(x=80, y=190)


def grab_date():
    date_entry.delete(0, END)
    date_entry.insert(0, cal.get_date())
    date_window.destroy()


def convert_to_pdf():
    cid = cid_entry.get()
    name = name_entry.get()
    gender = selected_option.get()
    age = age_entry.get()
    email = email_entry.get()
    ic = selected_ic.get()
    iccourse = selected_iccourse.get()
    contact = contact_entry.get()
    address = address_entry.get()
    disability = selected_disab.get()
    disabtype = disabtype_entry.get()
    quali = quali_entry.get()
    camp = selected_camp.get()
    remarks = remarks_entry.get()
    placement = selected_placement.get()
    camploc = camploc_entry.get()
    date = date_entry.get()

    print("NAME " + name)
    print("ID " + cid)
    print("GENDER " + gender)
    print("age" + age)
    print("EMAIL" + email)
    print("Contact" + contact)
    print("Location" + address)
    print("qualification" + quali)
    print("disability" + disability)
    print("type" + disabtype)
    print("Internal Candidate" + ic)
    print("Internal Candidate Course" + iccourse)
    print("Camp" + camp)
    print("Camp Loc" + camploc)
    print("Remark" + remarks)
    print("placement" + placement)
    print("date" + date)


    pdf = fpdf.FPDF()

    # Add a page
    pdf.add_page()

    pdf.image("naseoh logo.jpg", 18, 10, w=200)

    pdf.set_font('Arial', size=20)
    pdf.text(62, 55, txt="Candidate Registration Form")

    pdf.set_font("Arial", size=12)

    pdf.text(30, 80, txt="Candidate ID:")
    pdf.text(60, 80, txt=cid)

    pdf.text(110, 80, txt="Date:")
    pdf.text(130, 80, txt=date)

    pdf.text(30, 90, txt="Candidate Name:")
    pdf.text(68, 90, txt=name)

    pdf.text(30, 100, txt="Address:")
    pdf.text(50, 100, txt=address)

    pdf.text(30, 120, txt="Email:")
    pdf.text(50, 120, txt=email)

    pdf.text(30, 130, txt="Gender:")
    pdf.text(50, 130, txt=gender)

    pdf.text(110, 130, txt="Age:")
    pdf.text(130, 130, txt=age)

    pdf.text(30, 140, txt="Contact:")
    pdf.text(50, 140, txt=contact)

    pdf.text(110, 140, txt="Qualification:")
    pdf.text(142, 140, txt=quali)

    pdf.text(30, 150, txt="Disability Type:")
    pdf.text(63, 150, txt=disabtype)

    pdf.text(110, 150, txt="Disability:")
    pdf.text(138, 150, txt=disability)

    pdf.text(30, 160, txt="Internal Candidate:")
    pdf.text(70, 160, txt=ic)

    pdf.text(110, 160, txt="Internal Candidate Course:")
    pdf.text(165, 160, txt=iccourse)

    pdf.text(30, 170, txt="Camp:")
    pdf.text(50, 170, txt=camp)

    pdf.text(110, 170, txt="Camp Location:")
    pdf.text(147, 170, txt=camploc)

    pdf.text(30, 180, txt="Remarks:")
    pdf.text(55, 180, txt=remarks)

    pdf.text(110, 180, txt="Placement:")
    pdf.text(140, 180, txt=placement)

    pdf.set_font("Arial", size=10)
    pdf.text(60, 280, txt="Developed by VES Institute of Technology ")
    pdf.image("vesitlogo.png", 129, 272, w=10, h=10)

    filepath = filedialog.asksaveasfilename(defaultextension=".pdf")
    pdf.output(filepath)

style = ttk.Style()
style.theme_use('alt')
style.configure("TCombobox", fieldbackground= "white", background= "white")



cid_label = Label(root, text='Candidate ID',font=(5),background="white")
cid_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cid_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(5))
cid_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")



name_label = Label(root, text='Candidate Name',font=(9),background="white")
name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
name_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(9))
name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

selected_option = StringVar(root, value="select gender")
options_label = Label(root, text="Gender",font=(11),background="white")
options_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

options = StringVar(root)
options = ['Male', 'Female', 'Others']
option_menu = OptionMenu(root, selected_option, *options)
option_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(11))
option_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")

age_label = Label(root, text='Age',font=(11),background="white")
age_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
age_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(11))
age_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

email_label = Label(root, text='Candidate E-mail',font=(11),background="white")
email_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
email_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(11))
email_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

contact_label = Label(root, text='Contact',font=(13),background="white")
contact_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
contact_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
contact_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

address_label = Label(root, text='Location',font=(13),background="white")
address_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
address_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
address_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

quali_label = Label(root, text='Qualification',font=(13),background="white")
quali_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
quali_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
quali_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

selected_disab = StringVar(root, value="select type")
disab_label = Label(root, text="Disability Type",font=(13),background="white")
disab_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")
disab = StringVar(root)
disab = ['OH', 'VI', 'ID', 'HI', 'SHI', 'MR', 'CP', 'OTHERS']
disab_menu = OptionMenu(root, selected_disab, *disab)
disab_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(6))
disab_menu.grid(row=1, column=4, padx=5, pady=5, sticky="w")

disabtype_label = Label(root, text='Disability ',font=(13),background="white")
disabtype_label.grid(row=2, column=3, padx=5, pady=5, sticky="w")
disabtype_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
disabtype_entry.grid(row=2, column=4, padx=5, pady=5, sticky="w")

selected_ic = StringVar(root, value="select type")
ic_label = Label(root, text="Internal Candidate",font=(13),background="white")
ic_label.grid(row=3, column=3, padx=5, pady=5, sticky="w")
ic = StringVar(root)
ic = ['Yes', 'No']
ic_menu = OptionMenu(root, selected_ic, *ic)
ic_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(13))
ic_menu.grid(row=3, column=4, padx=5, pady=5, sticky="w")

selected_iccourse = StringVar(root, value="select courses")
iccourse_label = Label(root, text="Internal Candidate-Course",font=(13),background="white")
iccourse_label.grid(row=4, column=3, padx=5, pady=5, sticky="w")
iccourse = StringVar(root)
iccourse = ['Baking', 'Gardening', 'Pottery', 'Welding', 'Assembly', 'Tailoring', 'Computer Skills', 'Data Processing',
            'None']
iccourse_menu = OptionMenu(root, selected_iccourse, *iccourse)
iccourse_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(6))
iccourse_menu.grid(row=4, column=4, padx=5, pady=5, sticky="w")
#
selected_camp = StringVar(root, value="select type")
camp_label = Label(root, text="Camp",font=(13),background="white")
camp_label.grid(row=5, column=3, padx=5, pady=5, sticky="w")
camp = StringVar(root)
camp = ['Yes', 'No']
camp_menu = OptionMenu(root, selected_camp, *camp)
camp_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(6))
camp_menu.grid(row=5, column=4, padx=5, pady=5, sticky="w")

camploc_label = Label(root, text='Camp Location ',font=(13),background="white")
camploc_label.grid(row=6, column=3, padx=5, pady=5, sticky="w")
camploc_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
camploc_entry.grid(row=6, column=4, padx=5, pady=5, sticky="w")
#
remarks_label = Label(root, text='Remarks ',font=(13),background="white")
remarks_label.grid(row=7, column=3, padx=5, pady=5, sticky="w")
remarks_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
remarks_entry.grid(row=7, column=4, padx=5, pady=5, sticky="w")

selected_placement = StringVar(root, value="select type")
placement_label = Label(root, text="Placement",font=(13),background="white")
placement_label.grid(row=8, column=3, padx=5, pady=5, sticky="w")
placement = StringVar(root)
placement = ['Placed', 'Not Placed', 'Others']
placement_menu = OptionMenu(root, selected_placement, *placement)
placement_menu.configure(highlightthickness=1,highlightbackground="black",highlightcolor="black",width=17,font=(6))
placement_menu.grid(row=8, column=4, padx=5, pady=5, sticky="w")






def reset():
    for widget in root.winfo_children():
        if isinstance(widget,Entry):
            widget.delete(0,'end')
        if isinstance(widget,OptionMenu):
            # widget.delete(0, 'end')
            widget.place_forget()

            selected_option = StringVar(root, value="select gender")
            option_menu = OptionMenu(root, selected_option, *options)
            option_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black", width=17,font=(11))
            option_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")
            #
            selected_disab = StringVar(root, value="select type")
            disab_menu = OptionMenu(root, selected_disab, *disab)
            disab_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black", width=17,font=(6))
            disab_menu.grid(row=1, column=4, padx=5, pady=5, sticky="w")
            #
            selected_ic = StringVar(root, value="select type")
            ic_menu = OptionMenu(root, selected_ic, *ic)
            ic_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black", width=17, font=(13))
            ic_menu.grid(row=3, column=4, padx=5, pady=5, sticky="w")
            #
            selected_iccourse = StringVar(root, value="select courses")
            iccourse_menu = OptionMenu(root, selected_iccourse, *iccourse)
            iccourse_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black", width=17,font=(6))
            iccourse_menu.grid(row=4, column=4, padx=5, pady=5, sticky="w")
            #
            selected_camp = StringVar(root, value="select type")
            camp_menu = OptionMenu(root, selected_camp, *camp)
            camp_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black", width=17,
                                font=(6))
            camp_menu.grid(row=5, column=4, padx=5, pady=5, sticky="w")
            #
            selected_placement = StringVar(root, value="select type")
            placement_menu = OptionMenu(root, selected_placement, *placement)
            placement_menu.configure(highlightthickness=1, highlightbackground="black", highlightcolor="black",width=17, font=(6))
            placement_menu.grid(row=8, column=4, padx=5, pady=5, sticky="w")




date_label = Label(root, text='Date',font=(13),background="white")
date_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
date_entry = Entry(root,highlightthickness=1,highlightbackground="black",highlightcolor="black",width=20,font=(13))
date_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")
date_entry.insert(0, "dd/mm/yyyy")
date_entry.bind("<1>", pick_date)

def prevPage():
    root.destroy()
    import home


back_button = Button(text="Back",font=("bold"), width=6,height=1, bg="gray", command=prevPage)
back_button.grid(row=0,column=0,sticky="nw",)


rst_button=Button(root,text="Reset",font=("bold"),command=reset,width=10,height=1,bg="gray")
rst_button.grid(row=10,column=0,sticky=W,pady=5)

Button(root, text='SUBMIT', bg="gray", command=submit ,font=("bold"), width=10,height=1).grid(row=11,column=0,sticky=W,pady=5)

button = Button(root, text="Convert PDF",font=("bold"), width=10,height=1,bg="gray", command=convert_to_pdf)
button.grid(row=12,column=0,sticky=W,pady=5)

# Run the main loop
root.mainloop()