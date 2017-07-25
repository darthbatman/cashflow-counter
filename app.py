import Tkinter as tk
import time

cashflow = 0

def Draw():
    global text
    frame=tk.Frame(root)
    frame.place(x=10,y=60)
    text=tk.Label(frame,text='', font=("Helvetica", 48))
    text.pack()

def Refresher():
    global text
    global cashflow
    cashflow += 0.0005555555556
    text.configure(text=("$" + str(round(cashflow, 2))))
    root.after(100, Refresher)

def __main__(time_passed=0):
    global root
    global cashflow
    cashflow = float(time_passed) * (float(20) / float(60))
    root=tk.Tk()
    root.minsize(width=100,height=40)
    root.wm_title("Cashflow Counter")
    Draw()
    Refresher()
    root.mainloop()

if __name__ == '__main__':
    from sys import argv
    if '-tp' in argv:
        __main__(argv[argv.index('-tp') + 1])
    else:
        __main__()
