from tkinter import *
import pickle
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import ImageTk
import time
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
# Password hide view effect
State = 0
def protection(event):

    global State
    if State == 0:
        entry2.config(show='')
        label2_part.config(text='hide')
        State=1
    elif State == 1:
        entry2.config(show='*')
        label2_part.config(text='show')
        State=0






def checking():
    label_message.place_forget()
    user = (entry1.get()).lower()
    passwrd = entry2.get()
    dob = entry3.get()
    mobile = entry4.get()
    email_id = entry5.get()

    # Progress bar with
    prbar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
    prbar.place(x=250, y=470)
    prbar['maximum'] = 15
    for i in range(30):
        time.sleep(0.01)
        prbar['value'] = i
        prbar.update()
        prbar['value'] = 0
    with open('data.pkl', 'rb') as f:
        data=pickle.load(f)
        # checking valid entries
        if user in data.keys():
            label_message.place(x=265, y=96)
            label_message.config(text=f'"{entry1.get()}" already exist', fg='green')
        elif len(user) < 3:
            label_message.place(x=315, y=96)
            label_message.config(text='username too short', fg='red')

        elif len(passwrd) < 8:
            label_message.place(x=345, y=125)
            label_message.config(text='Password invalid', fg='red')

        elif len(dob) != 10 or int(dob[-4:]) > 2002:
            label_message.place(x=315, y=158)
            label_message.config(text='D.O.B. not valid', fg='red')

        elif len(mobile) != 10:
            label_message.place(x=315, y=187)
            label_message.config(text='Mobile no. invalid', fg='red')

        elif (len(email_id) < 7) or ('@' not in email_id) or ('.' not in email_id) or (' ' in email_id):
            label_message.place(x=315, y=215)
            label_message.config(text='Email ID invalid', fg='red')

        # Saving the data of new user in sql and pickle file
        else:
            print('Else is running')
            if (user not in data.keys()):
                credential={user:passwrd}
                with open('data.pkl', 'ab') as f:
                    pickle.dump(credential, f)
                conn = sqlite3.connect('Users_data.db')
                conn.execute('''Insert into CREDENTIAL values(?,?,?,?,?)''',
                             (entry1.get(),passwrd,dob,mobile,email_id))
                conn.commit()
                for rows in conn.execute('''SELECT * FROM credential;'''):
                    print(rows)
                ans=messagebox.showinfo('Registartion successful','Congratulation you can now book'
                                        ' Metro tickets online')
    prbar.destroy()
# changing background colour of buttons

def red(event):
    button2.config(bg='#d04f5e')

def blue(event):
    button.config(bg='#436a95')

def normal(event):
    button.config(bg='white')
    button2.config(bg='white')

username = StringVar(value='admin')
password = StringVar(value='admin123')
date = StringVar(value='01/05/2000')
number = StringVar(value='1122334455')
email = StringVar(value='test@shubham.com')

quit_icon = ImageTk.PhotoImage(file='quit_registartion.png')
submit_icon = ImageTk.PhotoImage(file='Submit_button.png')
background = ImageTk.PhotoImage(file='frame_bg.png')
label_bg_win = Label(root, image=background)
label_bg_win.grid(row=0, column=0)

account = ImageTk.PhotoImage(file='fullimage.jpg')
frame = Frame(root, borderwidth=5, bg='white', height=300, width=500, relief=SUNKEN)
frame.place(x=250, y=150)
label = Label(root, text='Welcome to Registration', font='baskerville 20 bold italic', bg='#230646', fg='#a725e8')
label.place(x=330, y=30)
label_bg = Label(root, image=account, bg='#230646')
label_bg.place(x=400, y=83)


# Coverig frame of manlogo
lb1 = Label(text='|', bg='white', fg='white', height=6).place(x=393, y=155)
lb2 = Label(text='-', bg='white', fg='white', width=22,height=0).place(x=396, y=235.2)
lb3 = Label(text='', bg='white', fg='white', height=6).place(x=552.3, y=155)

# making options in Frame
label1 = Label(frame, text='Username', font='times 15 bold italic', bg='white').place(x=0, y=95)
entry1 = Entry(frame, textvariable=username, width=35)
entry1.place(x=95, y=101)
entry1.bind('<Button-1>', hid_label_message)

label2 = Label(frame, text='Password', font='times 15 bold italic', bg='white').place(x=0, y=125)
entry2 = Entry(frame, textvariable=password, width=35, show='*')
entry2.place(x=95, y=130)
entry2.bind('<Button-1>', hid_label_message)

# Password protection
label2_part = Label(frame, text='show', font='1', bg='white')
label2_part.place(x=302, y=125)
label2_part.bind('<Button-1>', protection)


label3 = Label(frame, text='D.O.B.', font='times 15 bold italic', bg='white').place(x=0, y=155)
entry3 = Entry(frame, textvariable=date, width=35)
entry3.place(x=95, y=160)
label3_part = Label(frame, text='DD/MM/YYYY', font='lucida 13 bold', fg='#158a45', bg='white')
label3_part.place(x=312, y=155)
entry3.bind('<Button-1>', hid_label_message)
label3_part2=Label(frame, text='Above 18', font='lucida 7 bold',fg='#158a45', bg='white')
label3_part2.place(x=418, y=157)
label4 = Label(frame, text='Mobile no-', font='times 14 bold italic', bg='white').place(x=0, y=185)
entry4 = Entry(frame, textvariable=number, width=35)
entry4.place(x=95, y=189)
entry4.bind('<Button-1>', hid_label_message)

label5 = Label(frame, text='Email ID', font='times 14 bold italic', bg='white').place(x=0, y=215)
entry5 = Entry(frame, textvariable=email, width=35)
entry5.place(x=95, y=218)

label_message = Label(frame, font='consolas 12 bold italic', bg='white')
button = Button(frame, image=submit_icon, command=checking, width=200, height=39, bd=0, bg='white')
button.place(x=20, y=250)
button.bind('<Enter>', blue)
button.bind('<Leave>', normal)
entry5.bind('<Button-1>', hid_label_message)

button2 = Button(frame, image=quit_icon, width=200, bg='white', height=39, bd=0, command=lambda: root.destroy())
button2.bind('<Enter>', red)
button2.bind('<Leave>', normal)
button2.place(x=250, y=250)


root.mainloop()