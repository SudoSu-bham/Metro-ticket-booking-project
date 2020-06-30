from tkinter import *
import time
from PIL import ImageTk

root = Tk()
root.title('Online Metro Ticket')
root.iconbitmap('metro_logo.ico')
w = 1150
h = 610
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)

background = ImageTk.PhotoImage(file='DMRC_bg.jpg')
label_bg = Label(root, image=background)
label_bg.grid(row=0, column=0)
















# lable = Label(root)
# lable.pack()
# def cl():
#     for i in range(41):
#         time.sleep(0.03)
#         no=str(i)+'%'
#         lable.config(text=no)
#         lable.update()
#
#
# cl()
#
# lb=Label(root,text='Under development thankyou for helping me in testing',bg='Green')
# lb.place(x=100,y=100)

root.mainloop()
