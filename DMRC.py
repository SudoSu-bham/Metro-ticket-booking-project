from tkinter import *
import time

def book():
    root=Tk()
    root.title('Online Metro Ticket')
    root.iconbitmap('metro_logo.ico')
        #root.geometry('500x500')
    w = 500
    h = 550
    ws= root.winfo_screenwidth()
    hs= root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    lable = Label(root)
    lable.pack()
    def cl():
        for i in range(101):
            time.sleep(0.01)
            no=str(i)+'%'
            lable.config(text=no)
            lable.update()


    cl()



    root.mainloop()
