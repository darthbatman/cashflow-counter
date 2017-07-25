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
    global calculated_rate
    cashflow += calculated_rate
    text.configure(text=("$" + str(round(cashflow, 2))))
    root.after(100, Refresher)

def __main__(time_passed, rate):
    global root
    global cashflow
    global calculated_rate
    calculated_rate = float(rate) / float(60) / float(60) / float(10)
    cashflow = float(time_passed) * (float(20) / float(60))
    root=tk.Tk()
    root.minsize(width=100,height=40)
    root.wm_title("Cashflow Counter")
    Draw()
    Refresher()
    root.mainloop()

if __name__ == '__main__':
    from sys import argv
    tp = 0
    r = 20
    if '-tp' in argv:
        tp = argv[argv.index('-tp') + 1]
    if '-r' in argv:
        r = argv[argv.index('-r') + 1]
    __main__(tp, r)
