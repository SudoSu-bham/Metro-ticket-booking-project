from tkinter import *
import DMRC
from PIL import ImageTk
import random
from tkinter import messagebox

#Basic Structure of window
root=Tk()
root.title('Login to DMRC')
root.iconbitmap('metro_logo.ico')
root.geometry('1200x623')
root.configure(bg='SlateGray2')
root.resizable(width=False, height=False)
rgb=['#c45e56', '#de8983', '#f0b3af', '#d1996f', '#e3985f', '#e3b771', '#b8bf54', '#92bf54', '#76bf54',
     '#599c3a', '#3d7537','#37754b', '#235433', '#3f8a5e', '#3f8a6a', '#3f8a76', '#3f8a7f', '#60b5a9',
     '#51929c', '#396d75', '#4d869e', '#3b687a', '#2f7996', '#2f6d96', '#2f5f96', '#426ea1']
effect=random.choice(rgb)


baground=ImageTk.PhotoImage(file='metro_bg.jpg')
bg_label=Label(root,image=baground).grid(row=0,column=0)

def check():
    if entry1.get()=='' or entry2.get()=='':
        messagebox.showwarning('Field Empty!!!','Every field is Required')



def quit():
    root.destroy()

username=StringVar()
password=StringVar()

frame=Frame(root,bg=effect,borderwidth=10,relief=RAISED)
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



button=Button(frame,text='Sign in',command=check,width=15,bg='#279c5f')
button.grid(row=3,column=1,pady=25)

button1=Button(frame,text='Quit',command=quit,width=15,bg='#bf2828')
button1.grid(row=3,column=0,padx=5,pady=25)




root.mainloop()