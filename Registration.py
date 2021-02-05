from tkinter import *
import pickle
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import ImageTk
import time
from datetime import datetime
import sqlite3

root = Tk()
root.title('Registration for DMRC')
root.iconbitmap('metro_logo.ico')
w = 1000
h = 562
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2.5) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)

# hidig label on event


def hid_label_message(event):
    label_message.place_forget()

# Password hide/view effect


State = 0


def protection(event):

    global State
    if State == 0:
        entry2.config(show='')
        entry2_retype.config(show='')
        lbl_pass_part.config(text='hide')
        State = 1
    elif State == 1:
        entry2.config(show='*')
        entry2_retype.config(show='*')
        lbl_pass_part.config(text='show')
        State = 0

# Checking for Errors in provided field


def checking():
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    label_message.place_forget()
    user = (entry1.get()).lower()
    passwrd = entry2.get()
    dob = entry3.get()
    mobile = entry4.get()
    email_id = (entry5.get()).lower()

    prbar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
    prbar.place(x=250, y=485)       # Progress bar
    prbar['maximum'] = 15
    for i in range(30):
        time.sleep(0.01)
        prbar['value'] = i
        prbar.update()
        prbar['value'] = 0

        if user in data.keys():      # checking valid entries
            label_message.place(x=265, y=96)
            label_message.config(text=f"'{entry1.get()}' already exist", fg='green',font='Arial 12 bold')
        elif len(user) < 3:
            label_message.place(x=315, y=96)
            label_message.config(text='username too short', fg='red')

        elif len(passwrd) < 8:
            label_message.place(x=317, y=120)
            label_message.config(text='invalid password', fg='red')

        elif passwrd != entry2_retype.get():
            label_message.place(x=317, y=158)
            label_message.config(text="Password don't match", fg='red',font='consolas 11 bold italic')


        elif len(dob) != 10 or int(datetime.now().strftime("%Y")) - int(dob[-4:]) < 18:
            label_message.place(x=315, y=180)
            label_message.config(text='invalid  D.O.B. ', fg='red')

        elif len(mobile) != 10:
            label_message.place(x=315, y=212)
            label_message.config(text='invalid Mobile no.', fg='red')

        elif (len(email_id) < 7) or ('@' not in email_id) or ('.' not in email_id) or (' ' in email_id):
            label_message.place(x=315, y=240)
            label_message.config(text='invalid Email ID', fg='red')

        # Saving the data of new user in sql and pickle file
        else:
            if (user not in data.keys()):
                data[user] = str(entry2_retype.get())
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                f.close()
                conn = sqlite3.connect('Users_data.db')
                conn.execute('''Insert into CREDENTIAL values(?,?,?,?,?)''',
                             (user, passwrd, dob, mobile, email_id))
                conn.commit()
                conn.close()
                prbar.place_forget()
                messagebox.showinfo('Registartion successful', 'Congratulation you can now book'
                        ' Metro tickets through this software')
                return
    prbar.destroy()

# changing background colour of buttons


def red(event):
    button_quit.config(bg='#d04f5e')


def blue(event):
    button_submit.config(bg='#436a95')


def normal(event):
    button_submit.config(bg='#30c3ee')
    button_quit.config(bg='#30c3ee')


date = StringVar(value='Example 26/05/2000')
user_n= StringVar(value='eg: Anith')

quit_icon = ImageTk.PhotoImage(file='reg_images/quit_registartion.png')
submit_icon = ImageTk.PhotoImage(file='reg_images/Submit_button.png')
background = ImageTk.PhotoImage(file='reg_images/bg.jpg')
label_bg_win = Label(root, image=background)
label_bg_win.grid(row=0, column=0)

account = ImageTk.PhotoImage(file='reg_images/man_logo.png')
frame = Frame(root, borderwidth=5, bg='#30c3ee', height=330, width=505, relief=GROOVE)
frame.place(x=250, y=150)
label = Label(root, text='Welcome to Registration', font='baskerville 20 bold italic', bg='#46aef7', fg='#324e73')
label.place(x=330, y=30)
label_bg = Label(root, image=account, bd=0)
label_bg.place(x=430, y=83)


# Labels and Entries in Frame
lbl_user = Label(frame, text='Username', font='times 15 bold italic', bg='#30c3ee').place(x=0, y=95)
entry1 = Entry(frame, bg='#30c3ee', width=35, textvariable=user_n)
entry1.place(x=99, y=101)
entry1.bind('<Button-1>', hid_label_message)

lbl_pass = Label(frame, text='Password', font='times 15 bold italic', bg='#30c3ee').place(x=0, y=125)
entry2 = Entry(frame, width=35, bg='#30c3ee', show='*')
entry2.place(x=99, y=130)
entry2.bind('<Button-1>', hid_label_message)
lbl_pass_retype = Label(frame, text='Retype pass.', font='times 14 bold italic', bg='#30c3ee')
lbl_pass_retype.place(x=0, y=151)
entry2_retype = Entry(frame, width=35, bg='#30c3ee', show='*')
entry2_retype.place(x=99, y=156)
entry2_retype.bind('<Button-1>', hid_label_message)

# Password protection
lbl_pass_part = Label(frame, text='show', font='Arial 10', bg='#30c3ee')
lbl_pass_part.place(x=313, y=140)
lbl_pass_part.bind('<Button-1>', protection)


lbl_dob = Label(frame, text='D.O.B.', font='times 15 bold italic', bg='#30c3ee').place(x=0, y=182)
entry3 = Entry(frame, textvariable=date, bg='#30c3ee', width=35)
entry3.place(x=99, y=186)
lbl_dob_part = Label(frame, text='DD/MM/YYYY', font='Arial 13 bold', fg='#158a45', bg='#30c3ee')
lbl_dob_part.place(x=316, y=182)
entry3.bind('<Button-1>', hid_label_message)
lbl_dob_part2=Label(frame, text='Above 18', font='Arial 7 bold',fg='#158a45', bg='#30c3ee')
lbl_dob_part2.place(x=422, y=182)

lbl_mob = Label(frame, text='Mobile no-', font='times 14 bold italic', bg='#30c3ee').place(x=0, y=212)
entry4 = Entry(frame, bg='#30c3ee',width=35)
entry4.place(x=99, y=215)
entry4.bind('<Button-1>', hid_label_message)

lbl_id = Label(frame, text='Email ID', font='times 14 bold italic', bg='#30c3ee').place(x=0, y=240)
entry5 = Entry(frame, bg='#30c3ee', width=35)
entry5.place(x=99, y=244)

label_message = Label(frame, font='consolas 12 bold italic', bg='#30c3ee')
button_submit = Button(frame, image=submit_icon, command=checking, width=200, height=39, bd=0,
                       activebackground='#30c3ee', bg='#30c3ee')
button_submit.place(x=20, y=276)
button_submit.bind('<Enter>', blue)
button_submit.bind('<Leave>', normal)
entry5.bind('<Button-1>', hid_label_message)

button_quit = Button(frame, image=quit_icon, width=200, bg='#30c3ee', height=39, bd=0,
                     activebackground='#30c3ee', command=lambda: root.destroy())
button_quit.bind('<Enter>', red)
button_quit.bind('<Leave>', normal)
button_quit.place(x=250, y=276)


root.mainloop()
