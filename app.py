import Tkinter as tk
import time

cashflow = 0

def Draw():
    global text
    frame=tk.Frame(root)
    frame.place(x=10,y=10)
    text=tk.Label(frame,text='', font=("Helvetica", 48))
    text.pack()

def Refresher():
    global text
    global cashflow
    cashflow += 0.000005555555556
    text.configure(text=("$" + str(cashflow)))
    root.after(100, Refresher)

root=tk.Tk()
root.minsize(width=480,height=40)
root.wm_title("Cashflow Counter")
Draw()
Refresher()
root.mainloop()