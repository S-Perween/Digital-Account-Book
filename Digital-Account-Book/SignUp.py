from tkinter import *
import sqlite3
from tkinter import messagebox

def register():
    root=Toplevel()
    root.title("Sign Up")
    root.geometry("400x400")
    root.iconbitmap("icon.ico")

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - 1.5 * windowWidth)
    positionDown = int(root.winfo_screenheight() / 2 - 1.5 * windowHeight)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))


    canvas=Canvas(root, bg='indian red')
    canvas.pack(fill='both', expand='yes')

    canvas.create_text((210,20),anchor='n',text="✉ Sign Up", font=('Arial',20,'bold'), fill="misty rose")


    def clear1(event):
        e1.delete(0, END)
        e1.unbind('<Button>')
        e1.configure(bg='white', fg='black')


    def clear2(event):
        e2.delete(0, END)
        e2.unbind('<Button>')
        e2.configure(bg='white', fg='black')


    def clear3(event):
        e3.delete(0, END)
        e3.unbind('<Button>')
        e3.configure(bg='white', fg='black', show='*')


    e1=Entry(canvas, width=30, bg="lavender", fg='thistle4')
    e1.place(relx=.3, rely=.3, height=35)
    e1.insert(0, "Name")
    e1.bind('<Button>', clear1)


    e2=Entry(canvas, width=30, bg="lavender", fg='thistle4')
    e2.place(relx=.3, rely=.4, height=35)
    e2.insert(0, "E-mail")
    e2.bind('<Button>', clear2)


    e3=Entry(canvas, width=30, bg="lavender", fg='thistle4')
    e3.place(relx=.3, rely=.5, height=35)
    e3.insert(0, "Password")
    e3.bind('<Button>', clear3)


    def signup():
        v1=str(e1.get())
        v2=str(e2.get())
        v3=str(e3.get())

        if(v1=='' or v2=='' or v3==''):
            messagebox.showerror('Error', 'Cannot have an empty field')
            return

        tup=(v1, v2, v3)

        db=sqlite3.connect("users.db")
        cur=db.cursor()
        cur.execute("insert into users values(?,?,?)",tup)
        db.commit()
        db.close()

        messagebox.showinfo("Success", "Account created successfully")
        root.destroy()


    btn=Button(root, text='CREATE ACCOUNT',command=signup, width=25, bg='Sea green3', height=2, fg='white')
    btn.place(relx=.3, rely=.6)



    root.mainloop()