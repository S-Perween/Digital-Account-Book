from tkinter import *
import sqlite3
from tkinter import messagebox


def main(username):
    mydb=sqlite3.connect("{}accounts.db".format(username))
    cur=mydb.cursor()
    cur.execute("create table if not exists accounts(title varchar(30), email varchar(30), password varchar(30), detail varchar(50))")

    root = Tk()
    root.title("Digital Account Book")
    w=int(root.winfo_screenwidth())
    h=int(root.winfo_screenheight())
    root.geometry("1200x600")
    root.configure(bg='ivory2')
    # root.eval('tk::PlaceWindow . top')

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - 2.5 * windowWidth)
    positionDown = int(root.winfo_screenheight() / 2 - 1.5 * windowHeight)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    root.configure(background="lavender")
    # root.resizable(False, False)
    root.iconbitmap("icon.ico")
    header1="          Welcome {}         ".format(username)
    sec1=LabelFrame(root,text=header1, labelanchor='n', background="cyan3", height=300, fg='indian red', font=(20))
    sec1.pack(fill='both', expand='yes')


    canvas1=Canvas(sec1, bg='steel blue')
    canvas1.pack(fill='both', expand='yes')

    # ------------------------------------------------------------------------------------------------------------
    # OliveDrab1
    header2="          Accounts            "
    sec2 = LabelFrame(root, text=header2, labelanchor='n', background='ivory2', font=(18), fg='indian red')
    sec2.pack(fill='both', expand='yes')
    canvas2 = Canvas(sec2, bg='ivory2')
    canvas2.pack(side='left', expand='yes', fill='x')
    yscroll = Scrollbar(sec2, orient='vertical', command=canvas2.yview, width=20)
    yscroll.pack(side='right', fill='y')
    canvas2.configure(yscrollcommand=yscroll.set)
    canvas2.bind('<Configure>', lambda event : canvas2.configure(scrollregion=canvas2.bbox('all')))


    myframe= Frame(canvas2, height=1000)
    canvas2.create_window((0, 0), window=myframe, anchor='nw')

    # ----------------------------------------------------- Show ---------------------------------------------------

    def show():
        cur = mydb.cursor()
        cur.execute("select * from accounts")
        res = cur.fetchall()
        i=1
        Label(myframe, text="Title", font=(18), width='20', bg='ivory2', fg='seashell4', height='2').grid(row=0, column=0)
        Label(myframe, text="Email", font=(18), width='40', bg='ivory2', fg='seashell4', height='2').grid(row=0, column=1)
        Label(myframe, text="Password", font=(18), width='30', bg='ivory2', fg='seashell4', height='2').grid(row=0, column=2)
        Label(myframe, text="Details", font=(18), width='40', bg='ivory2', fg='seashell4', height='2').grid(row=0, column=3)
        for row in res:
            e1=Entry(myframe, font=(16), width='20', fg='indian red', bg='ivory2', relief="flat", justify='center')
            e1.grid(row=i, column=0)
            e2=Entry(myframe, font=(16), width='40', fg='indian red', bg='ivory2', relief="flat", justify='center')
            e2.grid(row=i, column=1)
            e3=Entry(myframe, font=(16), width='30', fg='indian red', bg='ivory2', relief="flat", justify='center')
            e3.grid(row=i, column=2)
            e4=Entry(myframe, font=(16), width='40', fg='indian red', bg='ivory2', relief="flat", justify='center')
            e4.grid(row=i, column=3)
            e1.insert(0,str(row[0]))
            e2.insert(0, str(row[1]))
            e3.insert(0, str(row[2]))
            e4.insert(0, str(row[3]))
            i=i+1


    # ------------------------------------------------ Insert ----------------------------------------------------


    def insert():
        e1 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e1.place(relx=.1, rely=.4, height=35)

        e2 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e2.place(relx=.5, rely=.4, height=35)

        e3 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e3.place(relx=.1, rely=.6, height=35)

        e4 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e4.place(relx=.5, rely=.6, height=35)

        def clear1(event):
            e1.delete(0, END)
            e1.unbind("<Button>")

        def clear2(event):
            e2.delete(0, END)
            e2.unbind("<Button>")

        def clear3(event):
            e3.delete(0, END)
            e3.unbind("<Button>")

        def clear4(event):
            e4.delete(0, END)
            e4.unbind("<Button>")

        e1.insert(0, "Title")
        e1.bind("<Button>", clear1)

        e2.insert(0, "Details")
        e2.bind("<Button>", clear2)

        e3.insert(0, "Username")
        e3.bind("<Button>", clear3)

        e4.insert(0, "Password")
        e4.bind("<Button>", clear4)

        def push():
            tup=(str(e1.get()),str(e3.get()),str(e4.get()),str(e2.get()))
            cur = mydb.cursor()
            cur.execute("insert into accounts values(?,?,?,?)",tup)
            mydb.commit()
            messagebox.showinfo("Success", "Record inserted successfully")
            show()
            closeall()


        def closeall():
            e1.destroy()
            e2.destroy()
            e3.destroy()
            e4.destroy()
            btninsert.destroy()
            btnclose.destroy()


        btninsert = Button(canvas1, text='Sumbit', command=push, width=10)
        btninsert.place(relx=.1, rely=.8)

        btnclose = Button(canvas1, text='Close', command=closeall, width=10)
        btnclose.place(relx=.3, rely=.8)


    # ---------------------------------------------------- Delete ---------------------------------------------------

    def delete():
        e1 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e1.place(relx=.1, rely=.4, height=35)


        def clear1(event):
            e1.delete(0, END)
            e1.unbind("<Button>")

        e1.insert(0, "Enter the title to delete")
        e1.bind("<Button>", clear1)

        def deleterec():
            cur=mydb.cursor()
            cur.execute("select * from accounts")
            res=cur.fetchall()
            d=True
            for row in res:
                if row[0] == str(e1.get()):
                    n=str(e1.get())
                    query="delete from accounts where title='{}'".format(n)
                    cur = mydb.cursor()
                    cur.execute(query)
                    mydb.commit()
                    messagebox.showinfo("Success","Record deleted succesfully")
                    d=False
                    root.destroy()
                    main(username)
                    break;
            if d:
                messagebox.showerror("Not Found", "Record not found")


        def closeall():
            e1.destroy()
            btn.destroy()
            btnclose.destroy()

        btn = Button(canvas1, text='Delete Record', command=deleterec, width=15)
        btn.place(relx=.1, rely=.6)

        btnclose = Button(canvas1, text='Close', command=closeall, width=10)
        btnclose.place(relx=.3, rely=.6)

    # ------------------------------------------------------- Modify ----------------------------------------------------

    def modify():
        e0 = Entry(canvas1, width=50, bg="lavender", fg='black')
        e0.place(relx=.1, rely=.3, height=35)

        e1 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e1.place(relx=.1, rely=.5, height=35)

        e2 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e2.place(relx=.5, rely=.5, height=35)

        e3 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e3.place(relx=.1, rely=.7, height=35)

        e4 = Entry(canvas1, width=30, bg="lavender", fg='black')
        e4.place(relx=.5, rely=.7, height=35)

        def clear1(event):
            e0.delete(0, END)
            e0.unbind("<Button>")

        e0.insert(0, "Enter the title of record to change")
        e0.bind("<Button>", clear1)

        def search():

            cur = mydb.cursor()
            cur.execute("select * from accounts")
            res = cur.fetchall()


            k=True
            title=str(e0.get())
            for row in res:
                if row[0] == title:
                    e1.insert(0, row[0])
                    e2.insert(0, row[1])
                    e3.insert(0, row[2])
                    e4.insert(0, row[3])
                    k=False
                    break;

            if k:
                messagebox.showerror("Error", "No such record present")


        def modifyrec():
            temp= str(e0.get())
            query = "update accounts set title='{}', email='{}', password='{}', detail='{}' where title='{}'".format(str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),temp)
            cur.execute(query)
            messagebox.showinfo("Success","Record modified succesfully")
            mydb.commit()
            show()
            closeall()


        def closeall():
            e0.destroy()
            e1.destroy()
            e2.destroy()
            e3.destroy()
            e4.destroy()
            btn.destroy()
            btnclose.destroy()
            searchbtn.destroy()

        searchbtn=Button(canvas1, text='Search', command=search, width=15)
        searchbtn.place(relx=.4, rely=.3)

        btn = Button(canvas1, text='Modify Record', command=modifyrec, width=15)
        btn.place(relx=.1, rely=.85)

        btnclose = Button(canvas1, text='Close', command=closeall, width=10)
        btnclose.place(relx=.3, rely=.85)


    newrecord=Button(canvas1, text='Create Record', command=insert, width=15)
    newrecord.place(relx=.1, rely=.1)

    showall=Button(canvas1, text='Show all', command=show, width=15)
    showall.place(relx=.3, rely=.1)

    delbtn=Button(canvas1, text='Delete', command=delete, width=15)
    delbtn.place(relx=.5, rely=.1)

    modbtn=Button(canvas1, text='Modify', command=modify, width=15)
    modbtn.place(relx=.7, rely=.1)

    # --------------------------------------------- End ----------------------------------------------------------
    mydb.commit()
    root.mainloop()

