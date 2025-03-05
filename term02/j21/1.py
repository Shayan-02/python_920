from tkinter import *


def showFullName():
    fullname = f"نام کامل شما {fname_ent.get()} {lname_ent.get()} است."
    fullname_lbl.config(text=fullname)

artin = Tk()
artin.title("fullname app")
artin.geometry("300x400")
artin.resizable(0, 0)

fname_lbl = Label(artin, text="نام", font=(("vazir", 16, "bold"))).pack(pady=10)
fname_ent = Entry(artin, font=(("vazir", 14, "bold")), justify="right")
fname_ent.pack()
fname_lbl = Label(artin, text="نام خانوادگی", font=(("vazir", 16, "bold"))).pack(pady=10)
lname_ent = Entry(artin, font=(("vazir", 14, "bold")), justify="right")
lname_ent.pack()
fullname_btn = Button(artin, text="نام کامل", font=(("vazir", 16, "bold")), bg="lightgreen", command=showFullName).pack(pady=20)
fullname_lbl = Label(artin, text="", font=(("vazir", 16, "bold")))
fullname_lbl.pack()

artin.mainloop()