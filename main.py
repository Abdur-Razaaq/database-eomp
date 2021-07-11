# IMPORTS
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# INITIALISING AND CONFIGURING WINDOW
root = Tk()
root.title("User Login")
root.geometry("1000x800")
root.resizable(False, False)
root.config(bg="black")

# ADDING AND PLACING IMAGE
img = PhotoImage(file="lcpic2.png")
Label(root, image=img).place(x=350, y=50)

# DATE AND TIME
now = datetime.now()
print(now)

# LOGIN FUNCTION
def login():
    try:  # ERROR CATCHING WITH TRY EXPECTCONNECTING TO DATABASE
        #
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if u_name_entry.get() == "" or id_entry.get() == "":  # FIELDS CANNOT BE EMPTY
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
        else:
            mycursor.execute('SELECT * FROM User_Info where Name=%s and ID_Number=%s',
                             (u_name_entry.get(), id_entry.get()))  # COMPARING DETAILS TO THE DETAILS IN MYSQL

            row = mycursor.fetchone()
            if row is None:  # IF USER IS NEW ALLOWS THEM TO REGISTER
                messagebox.showerror("USER DOES NOT EXIST", "PLEASE REGISTER DETAILS")
                msg = messagebox.askquestion("REGISTER", "WOULD YOU LIKE TO GO TO REGISTER WINDOW ?")
                if msg == "yes":
                    root.destroy()
                    import registration
            else:
                messagebox.showinfo(message="Login Successful! Enjoy Your Day!")
                message = messagebox.showinfo("Time In", "You Signed In At: " + str(now))
                if message == "ok":
                    root.destroy()
                    import Sign_out

    except ValueError:
        messagebox.showerror("OOPS", "INVALID NAME OR ID")
        u_name_entry.delete(0, END)
        id_entry.delete(0, END)
        u_name_entry.focus()


def register():  # REGISTER FUNCTION
    root.destroy()
    import registration


def admin():  # ADMIN FUNCTION
    root.destroy()
    import Admin_Login


# frame
login_frame = Frame(width=800, height=400, bg="grey")
login_frame.place(x=100, y=200)
# LABEL
log_label = Label(login_frame, text="LOGIN")
log_label.config(fg="blue",font="roboto 20 bold underline", bg="grey")
log_label.place(x=350, y=10)

# LABELS AND ENTRIES... PLACING AND CONFIGURING
u_name = Label(text="Enter Name:")
u_name.config(bg="green", font="roboto 12 bold underline", fg="black")
u_name.place(x=200, y=250)

u_name_entry = Entry()
u_name_entry.config(bg="Green", font="roboto 12 bold", highlightthickness="0")
u_name_entry.place(x=600, y=250)

id_lbl = Label(text="Enter ID Number:")
id_lbl.config(bg="green", font="roboto 12 bold underline", fg="black")
id_lbl.place(x=200, y=350)

id_entry = Entry()
id_entry.config(bg="Green", font="roboto 12 bold", highlightthickness="0")
id_entry.place(x=600, y=350)

# BUTTONS. CONFIGURATION AND PLACEMENT
login_btn = Button(text="Login", command=login)
login_btn.config(bg="green", font="roboto 12 bold", highlightthickness="0", width=15)
login_btn.place(x=250, y=500)

admin_btn = Button(text="ADMIN", command=admin)
admin_btn.config(bg="green", font="roboto 12 bold", highlightthickness="0", width=5)
admin_btn.place(x=900, y=30)

register_btn = Button(text="Register New User", command=register)
register_btn.config(bg="green", font="roboto 12 bold", highlightthickness="0", width=15)
register_btn.place(x=550, y=500)


def close():
    msg = messagebox.askquestion("EXIT?", "ARE YOU SURE YOU WANT TO EXIT?")
    if msg == "yes":
        root.destroy()


exit_btn = Button(text="Exit", command=close)
exit_btn.config(font="roboto 12 bold", bg="green", fg="black", width=15)
exit_btn.place(x=400, y=700)

root.mainloop()
