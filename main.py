from tkinter import *

root = Tk()
root.title("Login Page")
root.geometry("600x500")
root.config(bg="yellow")

u_name = Label(text="Enter Fullname: ")
u_name.config(bg="yellow", font="roboto 12 bold")
u_name.place(x=50, y=50)

u_name_entry = Entry(text="Enter Fullname: ")
u_name_entry.config(bg="white", font="roboto 12 bold")
u_name_entry.place(x=300, y=50)

password = Label(text="Enter ID Number: ")
password.config(bg="yellow", font="roboto 12 bold")
password.place(x=50, y=150)

password_entry = Entry(text="Enter ID Number: ")
password_entry.config(bg="white", font="roboto 12 bold")
password_entry.place(x=300, y=150)

login_btn = Button(text="Login", command="")
login_btn.config(bg="white", font="roboto 12 bold", highlightthickness="0")
login_btn.place(x=150, y=350)

register_btn = Button(text="Register New User", command="")
register_btn.config(bg="white", font="roboto 12 bold", highlightthickness="0")
register_btn.place(x=300, y=350)

root.mainloop()
