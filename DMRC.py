from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
import random
from datetime import datetime
import time
import pyqrcode

# Main window
root = Tk()
root.title('Online Metro Ticket')
root.iconbitmap('metro_logo.ico')
w = 900
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)
background = ImageTk.PhotoImage(file='dmrc_images/DMRC_bg.jpg')
label_bg = Label(root, image=background)
label_bg.grid(row=0, column=0)

# image for buttons
logo = ImageTk.PhotoImage(file='dmrc_images/metro_logo.png')
receipt_green = ImageTk.PhotoImage(file='dmrc_images/dmrc_receipt.png')
confirm = ImageTk.PhotoImage(file='dmrc_images/dmrc_confirm.png')


global_total_fare = 0


def calculate():
    global global_total_fare

    if From.get() == '' or To.get() == '' or person.get() == '' or person.get() < 1 or person.get() > 30:
        messagebox.showwarning('INVALID STATIONS OR PASSENGERS!!!','Either station\'s name or number'
                                '\nof passengers are invalid. ')
    elif (From.get()).lower() == (To.get()).lower():
        messagebox.showerror('SAME STATIONS!!!', 'Fare can\'t be calculated for the same\nstation'
                                                 ' please retype stations.')
    else:
        try:
            connect = sqlite3.connect('Fare_of_stations/fares.db')
            stationid = ()
            for id in connect.execute(f'SELECT station_id from tbl_stations where'
                        f' station_name in("{(From.get()).lower()}","{(To.get()).lower()}")'):
                stationid += id
            id1 = int(stationid[0])
            id2 = int(stationid[1])

            for fare in connect.execute(f'select fare{id1} from tbl_fare where station_id = {id2}'):
                global_total_fare = int(fare[0])*person.get()
                label_fare.config(text=f'Total fare is {fare[0]}x{person.get()} = {global_total_fare}')
                label_fare.place(x=320, y=230)
            button_receipt.config(state=NORMAL)
            frame.place_forget()
        except:
            messagebox.showwarning('INVALID STATIONS!!!', '\tRoute maybe under development otherwise\n\tPlease Check spelling of the Station\n'
                '\tretype the stations name\n\tto avoid Error use the name from suggestion menu')

# creating receipt of the payment


frame = Frame(root, width=220, height=380, relief=GROOVE, borderwidth=5, bg='white')

def receipt():
    label_update = Label(frame, width=29, height=8, bg='white')
    label_update.place(x=0, y=200) # Fixing overlaping of Labels

    frame.place(x=675, y=50)

    label_logo = Label(frame, image=logo, bd=0)
    label_logo.place(x=75, y=0)

    label_qr = Label(frame, bd=0)
    label_qr.place(x=65, y=90)


    label_head = Label(frame, text='Delhi Metro Rail Corporation', bg='white', font='lucida 12', fg='#3663a5')
    label_head.place(x=2, y=50)

    label_time = Label(frame, bg='white', text=f'Date/Time\t{(datetime.now()).strftime("%d/%m/%y %H:%M:%S")}')
    label_time.place(x=0, y=200)

    transaction = ''
    for i in range(13):
        transaction += random.choice('AaBbCcDdMmRrCc0123456789')
    label_tran = Label(frame, text=f'Transaction ID\t{transaction}', bg='white')
    label_tran.place(x=0, y=220)
    qrgen = pyqrcode.create(transaction)
    qrgen.png('Qr.png', scale=3)
    QrCode = ImageTk.PhotoImage(file='Qr.png')
    label_qr.config(image=QrCode)
    label_qr.image = QrCode


# Fixing the station's name from going out of the receipt
    if len(From.get()) > 20:
        label_from = Label(frame, text=f'From \t\t{(From.get())[0:16]}...', bg='white')
        label_from.place(x=0, y=240)
    else:
        label_from = Label(frame, text=f'From\t\t{From.get()}', bg='white')
        label_from.place(x=0, y=240)

    if len(To.get()) > 20:
        label_to = Label(frame, text=f'To \t\t{(To.get())[0:16]}...', bg='white')
        label_to.place(x=0, y=260)
    else:
        label_to = Label(frame, text=f'To\t\t{To.get()}', bg='white')
        label_to.place(x=0, y=260)

    label_fare = Label(frame, bg='white', text=f'Fare\t\tINR:{global_total_fare} & Person{person.get()}')
    label_fare.place(x=0, y=280)

    label_valid = Label(frame, text='----------------------------------------\nValid for today'
                        '\n----------------------------------------', bg='white')
    label_valid.place(x=0, y=315)
    button_receipt.config(state=DISABLED)

    button_info.place(x=385, y=338)  # button for info of project



def show_info():
    frame.place_forget()
    button_info.place_forget()

    txt = Text(root, width=92, height=18, fg='black', bg='#33c0ee', font='Arial 13 italic')
    txt.place(x=35, y=80)  # Text Field

    def exit_info(a,b): # Exit on click
        a.place_forget()
        b.place_forget()

    button_exit = Button(root, text='Exit Info',bg='#36bef0',width=10,
                         activebackground='#42b2f4', font='Arial 10 italic bold')
    button_exit['command'] = lambda a=txt,b=button_exit: exit_info(a,b)
    button_exit.place(x=400, y=450)

    try:
        with open('info.txt','r') as f:
            line = f.read()
        for ch in line:
            time.sleep(0.04)
            txt.insert(END,ch)
            txt.update()

    except:
        pass



# Main window

From = StringVar(value='Saket')
To = StringVar(value='adarsh nagar')
person = IntVar(value=1)
label_top = Label(root, text='Welcome to booking', font='baskerville 25 bold italic', bg='#42b2f4')
label_top.place(x=310, y=5)

lbl_From = Label(root, text='From', bg='#33c0ee', font='baskerville 15 bold italic')
lbl_From.place(x=85, y=80)
combo1 = ttk.Combobox(root, width=30, height=24, textvariable=From)
combo1['values'] = (open('Fare_of_stations/stations_name.txt', 'r').read()).split('\n')
combo1.place(x=150, y=84)

lbl_To = Label(root, text='To', bg='#42b1f6', font='baskerville 15 bold italic')
lbl_To.place(x=410, y=80)
combo2 = ttk.Combobox(root, width=30, height=24, textvariable=To)
combo2['value'] = (open('Fare_of_stations/stations_name.txt', 'r').read()).split('\n')
combo2.place(x=450, y=83)

lbl_no = Label(root, text='number of passengers', bg='#39baf3', font='baskerville 15 bold italic')
lbl_no.place(x=175, y=155)
combo3 = ttk.Combobox(root, width=5, height=10, textvariable=person)
combo3['values'] = list(range(1, 21))
combo3.place(x=395, y=160)

label_fare = Label(root, text=f'Total fare is {global_total_fare}', bg='#3bb9f3',
                   font='baskerville 20 bold italic')


button_confirm = Button(root, image=confirm, command=calculate,
                        activebackground='#36bef0', bg='#36bef0', bd=0)
button_confirm.place(x=200, y=300)

button_receipt = Button(root, command=receipt, bg='#42b2f4', image=receipt_green,
                        activebackground='#42b2f4', bd=0, state=DISABLED)
button_receipt.place(x=450, y=300)

button_info= Button(root, text='info', bg='#42b2f4', command=show_info, width=8,
                    activebackground='#36bef0', font='Arial 10 italic bold')
root.mainloop()
