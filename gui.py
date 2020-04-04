import os
from tkinter import *

from PIL import ImageTk, Image


def python():
    os.system('python python.py')


def main():
    root = Tk()
    root.title("Record Attendance")
    root.geometry("852x480")
    root.minsize(height=480, width=852)
    root.maxsize(height=480, width=852)
    root.configure(background="grey")

    C = Canvas(root, bg="blue")
    filename = ImageTk.PhotoImage(Image.open("3.jpg"))
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.pack()

    button = Button(root, text='Start Recording', command=python, justify=CENTER)
    button.config(relief=RAISED, fg="red1", width=13, height=2)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
