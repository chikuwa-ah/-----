import sys
import tkinter

root = tkinter.Tk()

root.title("素因数分解")
root.geometry("500x400")

text = tkinter.Text(width="15", height="1.5")
text.pack()

button = tkinter.Button(text="決定", command=lambda: click())
button.pack()


def click():
    print("button click")


root.mainloop()
