from tkinter import *
from tkinter import PhotoImage
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title("Sign Out")
root.geometry("1000x500")
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
root.config(bg="black")

img = PhotoImage(file="lcpic.png")
Label(root, image=img).place(x=30, y=10)

now = datetime.now()
print(now)


def sign_out():
    messagebox.showinfo(message="Sign Out Successful! Enjoy Your Day!")
    msg = messagebox.showinfo("Time Out", "You Signed Out At: " + str(now))
    if msg == "ok":
        root.destroy()
        import main


out_btn = Button(text="Sign Out", command=sign_out)
out_btn.config(font="roboto 12 bold", bg="green", fg="black", width=15)
out_btn.place(x=400, y=400)

root.mainloop()
