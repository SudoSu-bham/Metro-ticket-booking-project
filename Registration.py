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
    #hidig label on event
    def hid_label_message (event):
        label_message.place_forget()
    def hid_label_pass(event):
        label_pass.place_forget()





    def checking():
        user=(entry1.get()).lower()
        passwrd=entry2.get()
        dob=entry3.get()
        mobile=entry4.get()
        email=entry5.get()

        prbar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
        prbar.place(x=250, y=470)
        prbar['maximum']=15
        for i in range(30):
            time.sleep(0.01)
            prbar['value']=i
            prbar.update()
            prbar['value']=0
        with open('data.pkl','rb') as f:
            data=pickle.load(f)
            if user in data.keys():
                label_message.place(x=265, y=96)
                label_message.config(text=f'"{entry1.get()}" already exist',fg='green')
            elif len(passwrd) < 8:
                print(len(passwrd))
                label_pass.place(x=300,y=127)
                label_pass.config(text='Password is not valid')






        prbar.destroy()
    #changing background colour of buttons
    def red(event):
        button2.config(bg='red')
    def blue(event):
        button.config(bg='blue')
    def normal(event):
        button.config(bg='white')
        button2.config(bg='white')

    username=StringVar(value='admin')
    password=StringVar(value='admin3')
    date=StringVar(value='01052020')
    number=StringVar(value='1122334455')
    email=StringVar()

    quit_icon=ImageTk.PhotoImage(file='quiticon.png')
    register_icon=ImageTk.PhotoImage(file='Registericon.png')
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
    entry1=Entry(frame,textvariable=username,width=35)
    entry1.place(x=95,y=101)
    entry1.bind('<Button-1>',hid_label_message)
    label_message=Label(frame,font='consolas 12 bold italic')

    label2=Label(frame,text='Password',font='times 15 bold italic').place(x=0,y=125)
    entry2=Entry(frame,textvariable=password,width=35,show='*')
    entry2.place(x=95,y=130)
    label_pass=Label(frame,font='consolas 12 bold italic',fg='red')
    entry2.bind('<Button-1>',hid_label_pass)

    label3=Label(frame,text='D.O.B.',font='times 15 bold italic').place(x=0,y=155)
    entry3=Entry(frame,textvariable=date,width=35)
    entry3.place(x=95,y=160)
    label3_part=Label(frame,text='DDMMYYYY',font='lucida 13 bold',fg='#158a45').place(x=312,y=155)

    label4=Label(frame,text='Mobile no-',font='times 14 bold italic').place(x=0,y=185)
    entry4=Entry(frame,textvariable=number,width=35)
    entry4.place(x=95,y=189)

    label5=Label(frame,text='Email ID',font='times 14 bold italic').place(x=0,y=215)
    entry5=Entry(frame,textvariable=email,width=35)
    entry5.place(x=95,y=218)

    button=Button(frame,image=register_icon,command=checking,width=200,height=39,bd=0)
    button.place(x=20,y=250)
    button.bind('<Enter>', blue)
    button.bind('<Leave>', normal)

    button2=Button(frame,image=quit_icon,width=200,height=39,bd=0,command=lambda : root.destroy())
    button2.bind('<Enter>', red)
    button2.bind('<Leave>', normal)
    button2.place(x=250,y=250)


    root.mainloop()
reg()