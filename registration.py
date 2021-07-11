import mysql.connector
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

# WINDOW
root = Tk()
root.title("Registration")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
root.config(bg="black")  # WINDOW COLOR

# LIFE CHOICES IMAGE
img = PhotoImage(file="lcpic2.png")
Label(root, image=img).place(x=350, y=50)  # IMAGE / LOGO PLACEMENT

# USER INFO FRAME
frame_left = Frame(root, width=400, height=400, bg="#346ab3")
frame_left.place(x=100, y=200)
log = Label(frame_left, text="YOUR DETAILS", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
log.place(x=100, y=10)

# NAME LABEL AND ENTRY
user = Label(frame_left, text="Name:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
user.place(x=10, y=80)
user_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
user_ent.place(x=210, y=80)

# SURNAME LABEL AND ENTRY
surname = Label(frame_left, text="Surname: ", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
surname.place(x=10, y=140)
surname_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
surname_ent.place(x=210, y=140)  # 210 200

# MOBILE NUMBER LABEL AND ENTRY
phone = Label(frame_left, text="Mobile Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
phone.place(x=10, y=200)
phone_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
phone_ent.place(x=210, y=200)  # 210 140

# ID NUMBER LABEL AND ENTRY
id_num = Label(frame_left, text="ID Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
id_num.place(x=10, y=260)
id_num_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
id_num_ent.place(x=210, y=260)


# CLEAR BUTTON AND FUNCTIONALITY
def wipe():
    user_ent.delete(0, END)
    phone_ent.delete(0, END)
    surname_ent.delete(0, END)
    id_num_ent.delete(0, END)


clean = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=wipe)
clean.place(x=50, y=300)


# SUBMIT BUTTON AND FUNCTIONALITY
def submit():
    name = user_ent.get()
    mobile = phone_ent.get()
    id_number = id_num_ent.get()
    mail = surname_ent.get()
    if name == "" and mobile == "" and id_number == "" and mail == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
    else:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")
        mycursor = mydb.cursor()

        sql = "INSERT INTO User_Info (Name, Cell_Number, Surname, Id_Number) VALUES (%s, %s, %s, %s)"
        val = (user_ent.get(), phone_ent.get(), surname_ent.get(), id_num_ent.get())
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "Details Recorded.")
        mycursor.execute("Select * from User_Info")
        messagebox.showinfo("SUCCESS", "PLEASE ADD NEXT OF KIN DETAILS AS WELL")


enter = Button(frame_left, text="SUBMIT", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=submit)
enter.place(x=255, y=350)

# KIN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=200)
reg = Label(frame_right, text="NEXT OF KIN DETAILS", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
reg.place(x=50, y=10)

# NAME LABEL AND ENTRY
users = Label(frame_right, text="Name: ", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
users.place(x=10, y=100)
users_ent = Entry(frame_right, bg="#346ab3", fg="black")
users_ent.place(x=210, y=100)

# SURNAME LABEL AND ENTRY
Ksurname = Label(frame_right, text="Surname:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
Ksurname.place(x=10, y=155)
Ksurname_ent = Entry(frame_right, bg="#346ab3", fg="black")
Ksurname_ent.place(x=210, y=155)

# MOBILE NUMBER LABEL AND ENTRY
phones = Label(frame_right, text="Mobile Number:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
phones.place(x=10, y=210)
phones_ent = Entry(frame_right, bg="#346ab3", fg="black")
phones_ent.place(x=210, y=210)


# SUBMIT BUTTON AND FUNCTIONALITY
def submit():
    if user_ent.get() == "" and phone_ent.get() == "" and surname_ent.get() == "" and id_num_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
    else:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")
        mycursor = mydb.cursor()

        link = "Select * from User_Info"
        link_id = mycursor.execute(link)
        score_id = 0
        for i in mycursor:
            score_id = i[1]

        sql = "INSERT INTO NextOf_Kin (Name, Surname, Phone_Number) VALUES (%s, %s, %s)"
        val = (users_ent.get(), Ksurname_ent.get(), phones_ent.get(), score_id)
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "Details Recorded.")
        mycursor.execute("Select * from NextOf_Kin")
        messagebox.showinfo("SUCCESS", "DETAILS RECORDED, PLEASE SIGN IN")
        root.destroy()
        import main


enters = Button(frame_right, text="SUBMIT", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=submit)
enters.place(x=50, y=350)


# CLEAR BUTTON AND FUNCTIONALITY
def wipes():
    users_ent.delete(0, END)
    phones_ent.delete(0, END)


cleans = Button(frame_right, text="CLEAR", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=wipes)
cleans.place(x=260, y=300)


# EXIT BUTTON AND FUNCTIONALITY
def close():
    msg = messagebox.askquestion("EXIT?", "ARE YOU SURE YOU WANT TO EXIT?")
    if msg == "yes":
        root.destroy()


exit_btn = Button(text="Exit", command=close)
exit_btn.config(font="roboto 12 bold", bg="green", fg="black", width=15)
exit_btn.place(x=400, y=700)

# RUN CODE
root.mainloop()
