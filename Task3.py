import pyshorteners
from tkinter import *

win=Tk()
win.geometry("400x270")
win.configure(bg="pink")
#button function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)
#Label for entering used url
Label(win,text="Enter Your URL Link",font="impack 14 italic",bg="black",fg="white").pack(fill="x")
#Entry Box 
entry1=Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)
#Button
Button(win,text="Click Here",font="impack 12  italic",bg="black" ,fg="white" ,width="14",command=short).pack()
#Entry
entry2 = Entry(win ,font="impack 16 bold" ,bg="white" ,width=24,bd=0)
entry2.pack(pady=30)
mainloop()
