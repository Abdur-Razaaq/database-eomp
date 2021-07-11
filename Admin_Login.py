from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage


root = Tk()
root.title("Admin Login")
root.geometry("500x500")
root.config(bg="light green")
root.resizable(False, False)

# Image
img = PhotoImage(file="lcpic.png")
img = img.subsample(4)
bg_img_lbl = Label(root, image=img)
bg_img_lbl.place(x=130, y=0)


def admin_rights():
    if user_ent.get() != "admin":
        messagebox.showerror(message="Please enter correct Admin details")
    elif pass_ent.get() != "admin1234":
        messagebox.showerror(message="Please enter correct Admin password")

    else:
        if user_ent.get() == "admin" and pass_ent.get() == "admin1234":
            messagebox.showinfo("Access Granted", "Welcome Admin")
            root.destroy()
            import Admin

        else:
            pass


user_lbl = Label(text="Username:")
user_lbl.config(font="arial 13 bold underline", bg="light green", fg="blue")
user_lbl.place(x=50, y=175)

user_ent = Entry()
user_ent.config(font="arial 13 bold", bg="light green", fg='blue', highlightthickness=0)
user_ent.place(x=225, y=175)

pass_lbl = Label(text="Password:")
pass_lbl.config(font="arial 13 bold underline", bg="light green", fg="blue")
pass_lbl.place(x=50, y=275)

pass_ent = Entry()
pass_ent.config(font="arial 13 bold", bg="light green", fg='blue', highlightthickness=0)
pass_ent.place(x=225, y=275)

ad_login = Button(text="LOGIN", command=admin_rights)
ad_login.config(font="arial 13 bold underline", bg="black", fg="light green", width=15)
ad_login.place(x=160, y=400)

root.mainloop()
