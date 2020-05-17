from tkinter import *
import pickle
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import ImageTk
import time

def reg():
#Basic Structure of window
    root=Tk()
    root.title('Login to DMRC')
    root.iconbitmap('metro_logo.ico')
    root.geometry('1000x562')
    root.resizable(width=False, height=False)

    def already_register():
        root.destroy()
    def checking():
        
        prbar = Progressbar(root, orient=HORIZONTAL, length=200, maximum=100, mode='determinate')
        prbar.place(x=5,y=30)


    username=StringVar(value='admin')
    password=StringVar(value='admin123')
    date=StringVar()
    number=StringVar()
    email=StringVar()



    background=ImageTk.PhotoImage(file='frame_bg.png')
    label_bg_win=Label(root,image=background)
    label_bg_win.grid(row=0,column=0)

    account=ImageTk.PhotoImage(file='fullimage.jpg')
    frame=Frame(root,borderwidth=5,bg='white',height=300,width=500,relief=SUNKEN,)
    frame.place(x=250,y=150)
    label=Label(root,text='Welcome to Registration',font=('baskerville 20 bold italic'),bg='#230646',fg='#a725e8')
    label.place(x=330,y=30)
    label_bg=Label(root,image=account,bg='#230646')
    label_bg.place(x=400,y=83)

    #Coverig frame of manlogo
    lb1=Label(text='|',bg='white',fg='white',height=6).place(x=393,y=155)
    lb2=Label(text='-',bg='white',fg='white',width=22,height=0).place(x=396,y=235.2)
    lb3=Label(text='',bg='white',fg='white',height=6).place(x=552.3,y=155)

# making options in Frame
    label1=Label(frame,text='Username',font='times 15 bold italic').place(x=0,y=95)
    entry1=Entry(frame,textvariable=username,width=35).place(x=95,y=101)

    label2=Label(frame,text='Password',font='times 15 bold italic').place(x=0,y=125)
    entry2=Entry(frame,textvariable=password,width=35).place(x=95,y=130)

    label3=Label(frame,text='D.O.B.',font='times 15 bold italic').place(x=0,y=155)
    entry3=Entry(frame,textvariable=date,width=35).place(x=95,y=160)
    label3_part=Label(frame,text='DDMMYYYY',font='lucida 13 bold',fg='#158a45').place(x=312,y=155)

    label4=Label(frame,text='Mobile no-',font='times 14 bold italic').place(x=0,y=185)
    entry4=Entry(frame,textvariable=number,width=35).place(x=95,y=189)

    label5=Label(frame,text='Email ID',font='times 14 bold italic').place(x=0,y=215)
    entry5=Entry(frame,textvariable=email,width=35).place(x=95,y=218)

    button=Button(frame,text='Register',command=checking,font='comic 14 bold italic',width=15,bg='#1764bd')
    button.place(x=20,y=250)

    button2=Button(frame,text='Already Registered',font='comic 14 bold italic',width=15,bg='#00b01a',
                   command=already_register)
    button2.place(x=240,y=250)


    root.mainloop()
reg()