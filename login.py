from tkinter import *
import DMRC
from PIL import ImageTk
import pickle
import random
import Registration

from tkinter import messagebox

#Basic Structure of window
login=Tk()
login.title('Login to DMRC')
login.iconbitmap('metro_logo.ico')
login.geometry('1200x623')
login.resizable(width=False, height=False)
rgb=['#c45e56', '#de8983', '#f0b3af', '#d1996f', '#e3985f', '#e3b771', '#b8bf54', '#92bf54', '#76bf54',
     '#599c3a', '#3d7537' , '#37754b', '#235433', '#3f8a5e', '#3f8a6a', '#3f8a76', '#3f8a7f', '#60b5a9',
     '#51929c', '#396d75', '#4d869e', '#3b687a', '#2f7996', '#2f6d96', '#2f5f96', '#426ea1']
effect=random.choice(rgb)


baground=ImageTk.PhotoImage(file='metro_bg.jpg')
bg_label=Label(login,image=baground).grid(row=0,column=0)

#opening registered credential
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

#checking if username and password is valid
def check():
    global data
    if entry1.get()=='' or entry2.get()=='':
        messagebox.showerror('Field Empty!!!','Every field is Required')
    elif len(entry2.get()) <8:
        messagebox.showwarning("Too short password","Please enter password of atleast 8 digits")
        entry2.delete(0,END)
    elif entry1.get()!='' and entry2.get()!='':
        try:
            if data[(entry1.get()).lower()]==entry2.get():
                login.destroy()
                DMRC.book()
            elif entry1.get() in data.keys():
                msg.config(text="Password is wrong ⚠️")
        except:
            msg.config(text='Try to Register :P')
def reg():
    login.destroy()
    Registration.reg()
username=StringVar(value='admin')
password=StringVar(value='admin123')

#creating login window
frame=Frame(login,bg=effect,borderwidth=10,relief=RAISED)
frame.grid(row=0,column=0)
welcome=Label(frame,text='Welcome to Metro login',font= 'UbuntuMono 20 bold',bg=effect,fg='#303175')
welcome.grid(row=0,column=0,pady=10,columnspan=3)


label1=Label(frame,text='Username',font='lucida 15 bold',bg='SlateGray1',fg='Sea Green',relief=GROOVE)
label1.grid(row=1,column=0,pady=10,sticky=NW)
entry1=Entry(frame,textvariable=username,width=35)
entry1.grid(row=1,column=1,pady=10,sticky=NW)


label2=Label(frame,text='Password',font='lucida 15 bold',bg='SlateGray1',fg='Sea Green',relief=GROOVE)
label2.grid(row=2,column=0,sticky=NW)
entry2=Entry(frame,textvariable=password,width=35)
entry2.grid(row=2,column=1,pady=10,sticky=NW)

msg=Label(login,bg='#fa203a',fg='black',font='comic 20')
msg.place(x=440,y=450)


button=Button(frame,text='Log in',command=check,width=15,bg='#279c5f')
button.grid(row=3,column=1,pady=25)

button1=Button(frame,text='Quit',command=lambda : login.destroy(),width=15,bg='#bf2828')
button1.grid(row=3,column=0,padx=5,pady=25)
frame_size=Label(frame,bg=effect).grid(row=4,column=1)

register=Button(login,text='Register Instead',command=reg,width=25,bg='#1764bd',font='comic 10 bold')
register.place(x=500,y=400)


login.mainloop()