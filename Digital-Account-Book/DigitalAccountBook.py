from tkinter import *
# from tkinter.ttk import *
import sqlite3
import SignUp
import AccountBook
from tkinter import messagebox


db = sqlite3.connect("users.db")
cur = db.cursor()
cur.execute("create table if not exists users(name varchar(30), email varchar(30) unique, password varchar(30))")
db.commit()

root = Tk()
root.title("Login")
root.geometry("400x400")
root.iconbitmap("icon.ico")
root.resizable(False, False)
# ------------------------------------------ Centering the app --------------------------------------------------
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - 1.5 * windowWidth )
positionDown = int(root.winfo_screenheight() / 2 - 1.5 * windowHeight )
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# root.eval('tk::PlaceWindow . above')
canvas = Canvas(root, bg='steel blue')
canvas.pack(fill='both', expand='yes')

canvas.create_text((210, 20), anchor='n', text="Member Login", font=('Arial', 20, 'bold'), fill="misty rose")


def clear1(event):
    e1.delete(0, END)
    e1.unbind('<Button>')
    e1.configure(bg='white', fg='black')


def clear2(event):
    e2.delete(0, END)
    e2.unbind('<Button>')
    e2.configure(bg='white', fg='black', show='*')


e1 = Entry(canvas, width=30, bg="lavender", fg='thistle4')
e1.place(relx=.3, rely=.3, height=35)
e1.insert(0, "username")
e1.bind('<Button>', clear1)

e2 = Entry(canvas, width=30, bg="lavender", fg='thistle4')
e2.place(relx=.3, rely=.4, height=35)
e2.insert(0, "password")
e2.bind('<Button>', clear2)




def login(event):
    v1 = e1.get()
    v2 = e2.get()
    if v1 == '' or v2 == '':
        messagebox.showerror("Login Error", "Cannot have an empty field")
    else:
        cur.execute("select * from users")
        res = cur.fetchall()
        # db.close()
        k = True
        for row in res:
            if v1 == row[1] and v2 == row[2]:
                k = False
                temp=row[0]
                root.destroy()
                AccountBook.main(temp)

        if k:
            messagebox.showinfo("Not a user", "Invalid login credentials")



e2.bind("<Return>",login)

def login():
    v1 = e1.get()
    v2 = e2.get()
    if v1 == '' or v2 == '':
        messagebox.showerror("Login Error", "Cannot have an empty field")
    else:
        cur.execute("select * from users")
        res = cur.fetchall()
        # db.close()
        k = True
        for row in res:
            if v1 == row[1] and v2 == row[2]:
                k = False
                temp=row[0]
                root.destroy()
                AccountBook.main(temp)

        if k:
            messagebox.showinfo("Not a user", "Invalid login credentials")


def signup():
    SignUp.register()


btn = Button(root, text='Login', command=login, width=25, bg='Sea green3', height=2, fg='white')
btn.place(relx=.3, rely=.5)

btn = Button(root, text='Sign up', command=signup, width=25, fg='white', activebackground="steel blue",
             bg='steel blue', relief='flat', height=2)
btn.place(relx=.3, rely=.7)

root.mainloop()