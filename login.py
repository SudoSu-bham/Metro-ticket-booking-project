try:
    from tkinter import *
    from PIL import ImageTk
    import pickle
    import random
    from tkinter import messagebox
    import lamda
except:
    print('Welcome to our Python project please note that this project require special libraries\n',
        'In order to run this project download "Pillow" library(type in cmd "pip3 install pillow")')
#Basic Structure of window
login = Tk()
login.title('Login to DMRC')
login.iconbitmap('metro_logo.ico')
w =1200
h =623
ws= login.winfo_screenwidth()
hs= login.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2.3) - (h / 2)
login.geometry('%dx%d+%d+%d' % (w, h, x, y))

login.resizable(width=False, height=False)
# rgb=['#c45e56', '#de8983', '#f0b3af', '#d1996f', '#e3985f', '#e3b771', '#b8bf54', '#92bf54', '#76bf54',
#      '#599c3a', '#3d7537' , '#37754b', '#235433', '#3f8a5e', '#3f8a6a', '#3f8a76', '#3f8a7f', '#60b5a9',
#      '#51929c', '#396d75', '#4d869e', '#3b687a', '#2f7996', '#2f6d96', '#2f5f96', '#426ea1']
#
effect = '#27ccea'


baground = ImageTk.PhotoImage(file='metro_bg.jpg')
bg_label = Label(login, image=baground).grid(row=0, column=0)
log_logo = ImageTk.PhotoImage(file='circle-cropped.png')

#opening registered credential
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

# checking if username and password is valid
def check():
    global data
    if entry1.get() == '' or entry2.get() == '':
        messagebox.showerror('Field Empty!!!','Every field is Required')
    elif len(entry1.get()) < 3:
        messagebox.showwarning("Too short Username", "Please enter a valid username")
    elif len(entry2.get()) < 8:
        messagebox.showwarning("Too short password","Please enter password of atleast 8 digits")
        entry2.delete(0, END)
    elif entry1.get() != '' and entry2.get() != '':
        msg.place(x=440, y=520)
        try:
            if data[(entry1.get()).lower()] == entry2.get():
                login.destroy()
                import DMRC
            elif entry1.get() in data.keys():
                msg.config(text="Incorrect Password {~_~}")
        except:
            msg.config(text='Try to Register (•◡•)')
def reg():
    login.destroy()
    import Registration

def hid(event):
    msg.place_forget()

State = 0
def protection(event):
    global State
    if State == 0:
        entry2.config(show='')
        label2_part.config(text='hide')
        State = 1
    elif State == 1:
        entry2.config(show='*')
        label2_part.config(text='show')
        State = 0


username=StringVar(value='admin')
password=StringVar(value='admin123')


# creating login window
frame = Frame(login, bg=effect, borderwidth=7, relief=RAISED,width=400,height=450)
frame.place(x=400, y=50)
welcome=Label(frame,text='Welcome to Metro login', font='corbel 20 bold',bg=effect,fg='#303175')
welcome.place(x=47,y=0)

canvas=Canvas(frame,width=150,bg=effect,height=150,bd=0, highlightthickness=0)
canvas.place(x=120, y=33)
canvas.create_image(0,0,image=log_logo,anchor=NW)

label1=Label(frame, text='Username', font='lucida 20', bg=effect)
label1.place(x=5, y=200)
entry1=Entry(frame,textvariable=username,width=33)
entry1.place(x=150, y=210)
entry1.bind('<Button-1>',hid)


label2 = Label(frame, text='Password', font='lucida 20', bg=effect)
label2.place(x=5, y=250)
entry2 = Entry(frame, textvariable=password, width=35, show='*')
entry2.place(x=150, y=260)
entry2.bind('<Button-1>',hid)

label2_part = Label(frame, text='show', bg=effect)
label2_part.place(x=352, y=260)
label2_part.bind('<Button-1>', protection)


msg=Label(login, bg='#fa203a', fg='black', font='comic 20')

log_in = ImageTk.PhotoImage(file='login_button.png')
button=Button(frame,image=log_in,command=check,bd=0,bg=effect)
button.place(x=40, y=330)

quit_icon = ImageTk.PhotoImage(file='Quit_button.png')
button1=Button(frame, image=quit_icon, command=lambda: login.destroy(),bd=0, bg=effect)
button1.place(x=200, y=330)

regbtn=ImageTk.PhotoImage(file='createAccount_button.png')
register=Button(login, image=regbtn, command=reg, bg=effect,bd=0, font='comic 10 bold')
register.place(x=500,y=440)


login.mainloop()