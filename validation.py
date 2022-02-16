from tkinter import *
from tkinter import messagebox

special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
              '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']


def validation():
    password = pwd.get()
    msg = "Turn off validation"

    if len(password) == 0:
        msg = 'Password can\'t be empty'
    else:
        try:
            if not any(ch in special_ch for ch in password):
                msg = 'Atleast 1 special character required!'
            elif not any(ch.isupper() for ch in password):
                msg = 'Atleast 1 uppercase character required!'
            elif not any(ch.islower() for ch in password):
                msg = 'Atleast 1 lowercase character required!'
            elif not any(ch.isdigit() for ch in password):
                msg = 'Atleast 1 number required!'
            elif len(password) < 8:
                msg = 'Password must be minimum of 8 characters!'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
    messagebox.showinfo('message', msg)


ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x200')
ws.config(bg='#DDF2AE')

frame = Frame(
    ws,
    bg='#8C8C8B',
    padx=10,
    pady=10
)
frame.pack(pady=30)

Label(
    frame,
    bg='#8C8C8B',
    text='Password',
    font=('sans-serif', 14)
).grid(row=0, column=0, padx=(0, 10))

pwd = Entry(
    frame,
    font=('sans-serif', 14),
    show='*'
)
pwd.grid(row=0, column=1)

submit = Button(
    frame,
    text='Submit',
    width=20,
    font=('sans-serif', 12),
    command=validation,
    pady=10
)
submit.grid(row=1, columnspan=2, pady=20)

ws.mainloop()