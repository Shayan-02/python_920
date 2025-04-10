from tkinter import *


def new_tab():
    window = Tk()
    root.geometry("400x400")
    window.config(bg="pink")
    window.mainloop()


root = Tk()
root.geometry("300x300")

new_tab_btn = Button(root, text="کلیک کنید", command=new_tab)
new_tab_btn.pack()

root.mainloop()
