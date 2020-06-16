try:
    from tkinter import *
    from PIL import ImageTk
    import pickle
    from tkinter import messagebox
    import sqlite3
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
effect = '#27ccea'

# Image of various buttons and baground
baground = ImageTk.PhotoImage(file='metro_bg.jpg')
bg_label = Label(login, image=baground).grid(row=0, column=0)
log_logo = ImageTk.PhotoImage(file='circle-cropped.png')
validate_button= ImageTk.PhotoImage(file='validate.png')
quit_icon = ImageTk.PhotoImage(file='Quit_button.png')
regbtn = ImageTk.PhotoImage(file='createAccount_button.png')
log_in = ImageTk.PhotoImage(file='login_button.png')
frg_submit = ImageTk.PhotoImage(file='forget_submit.png')
cancel = ImageTk.PhotoImage(file='Cancel.png')

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

# Forget password GUI
def forget(event):
    conn = sqlite3.connect('users_data.db') # Opening the sql database
    username = StringVar(value='Sumukh')
    email = StringVar(value='contact_me@sumukh.com')
    mobl = StringVar(value='9999888822')
    def back():  # back to login portal
        frame_fgt.place_forget()
        frame.place(x=400, y=50)
    def validate():  # checking if credential is valid
        def new_pass_validation():  # validating new password
            if len(entry_newpass.get()) < 8:
                messagebox.showerror('Too short password', 'Please enter password greater '
                                        'than or equal to 8 digits')
            elif entry_newpass.get() != entry_reenter.get():
                messagebox.showerror('Password do not match', 'Retyped password'
                                            ' should be same as the one entered above')
            else:
                with open('data.pkl', 'rb') as f:
                    data = pickle.load(f)
                    data[(entry2_frg.get()).lower()] = entry_newpass.get()
                    with open('data.pkl', 'wb') as f:
                        pickle.dump(data,f)
                query_update = f'update credential SET password="{entry_newpass.get()}"' \
                               f' where Username="{(entry2_frg.get()).lower()}";'
                conn.execute(query_update)
                conn.commit()
                ans = messagebox.showinfo('Password changed','Congratulation password has been changed'
                                    '\nClick "OK" to get back to login')
                if ans=='ok':
                    back()

        query = f'Select mobile_number,Email_id from credential' \
               f' where username="{(entry2_frg.get()).lower()}"'
        userexist ='no'
        for rows in conn.execute(query):
            userexist='yes'
            if str(rows[0]) == entry3_frg.get() and rows[1]== entry4_frg.get():
                valid_button.place_forget()
                cancel_btn.place(x=430, y=350)
                submit_btn = Button(frame_fgt, image=frg_submit, bg='#2bc7ed',
                                    bd=0, command=new_pass_validation)
                submit_btn.place(x=200, y=350)

                entry2_frg.config(state='disabled', disabledbackground='#2bc7ed')
                entry3_frg.config(state='disabled', disabledbackground='#2bc7ed')
                entry4_frg.config(state='disabled', disabledbackground='#2bc7ed')

                label_newpass = Label(frame_fgt, text='New password', bg='#2bc7ed', font='10')
                label_newpass.place(x=177, y=230)
                entry_newpass = Entry(frame_fgt, bg=effect, width=35, bd=2)
                entry_newpass.place(x=285, y=230)

                label_reenter = Label(frame_fgt, text='Retype', bg='#2bc7ed', font='10')
                label_reenter.place(x=198, y=270)
                entry_reenter = Entry(frame_fgt, bg=effect, width=35, bd=2)
                entry_reenter.place(x=285, y=270)
            else:
                messagebox.showerror('Not valid', 'One or more details are wrong please correct them')

        if entry2_frg.get()=='' or entry3_frg.get()=='' or entry4_frg.get()=='':
            messagebox.showerror('Empty Field Error!!','One or more fields are empty please fill all')
        elif userexist == 'no':
            messagebox.showerror('User not found!!', f'There is no user'
                f' name "{entry2_frg.get()}" use the registered account name')
    frame.place_forget()
    frame_fgt = Frame(login, height=450, width=800, bg='#2bc7ed', relief=GROOVE, bd=7)
    frame_fgt.place(x=300, y=50)
    label1_frg = Label(frame_fgt, text='Change password', font='times 25', bg='#2bc7ed')
    label1_frg.place(x=20, y=20)

    label2_frg = Label(frame_fgt, text='Username',bg='#2bc7ed', font='10')
    label2_frg.place(x=200, y=120)
    entry2_frg = Entry(frame_fgt, bg=effect, width=35,bd=2, textvariable=username)
    entry2_frg.place(x=285, y=120)

    label3_frg = Label(frame_fgt, text='Mobile no-', bg='#2bc7ed', font='10')
    label3_frg.place(x=200, y=150)
    entry3_frg = Entry(frame_fgt, bg=effect, width=35, bd=2, textvariable=mobl)
    entry3_frg.place(x=285, y=150)

    label4_frg = Label(frame_fgt, text='Email id', bg='#2bc7ed', font='10')
    label4_frg.place(x=200, y=180)
    entry4_frg = Entry(frame_fgt, bg=effect, width=35, bd=2, textvariable=email)
    entry4_frg.place(x=285, y=180)

    valid_button=Button(frame_fgt, image=validate_button, bg='#2bc7ed', bd=0, command=validate)
    valid_button.place(x=260, y=230)

    cancel_btn = Button(frame_fgt, image=cancel, command=back, bg='#2bc7ed',bd=0)
    cancel_btn.place(x=280, y=350)


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

button=Button(frame,image=log_in,command=check,bd=0,bg=effect)
button.place(x=40, y=310)

label_forget=Label(frame,text='Forgot password?', bg=effect, fg='blue',font='times 10')
label_forget.place(x=155, y=355)
label_forget.bind('<Button-1>',forget)

button1=Button(frame, image=quit_icon, command=lambda: login.destroy(),bd=0, bg=effect)
button1.place(x=210, y=310)

register=Button(frame, image=regbtn, command=reg, bg=effect,bd=0, font='comic 10 bold')
register.place(x=90, y=380)


login.mainloop()