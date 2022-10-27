from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector as sq
    
con=sq.connect(host="localhost",user="root",password="alanwalker")
cur=con.cursor()
cur=con.cursor(buffered=True)
cur.execute("create database if not exists hello")
cur.execute("use hello")
cur.execute("create table if not exists doctor"
            "("
            "doc_id varchar(12) primary key,"
            "doc_name varchar(20) not null,"
            "sex varchar(10) not null,"
            "age int(10) not null,"
            "type varchar(20) not null,"
            "salary int(10) not null,"
            "exp int(3) not null,"
            "contact_no bigint(15) not null,"
            "email varchar(40) not null)")

#PATIENT FORM    
class Doctor:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.doc_ID=StringVar()
        self.doc_name=StringVar()
        self.doc_sex=StringVar()
        self.doc_age=IntVar()
        self.doc_type=StringVar()
        self.doc_salary=IntVar()
        self.doc_exp=IntVar()
        self.doc_email=StringVar()
        self.doc_phno=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "DOCTOR REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lbldocid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldocid.grid(row=0,column=0)
        self.lbldocid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_ID)
        self.lbldocid.grid(row=0,column=1)
        
        self.lbldocname = Label(self.LoginFrame,text="DOCTOR NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldocname.grid(row=1,column=0)
        self.lbldocname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_name)
        self.lbldocname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_sex)
        self.etype1.grid(row=2,column=1)
        

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="SPECIALIZATION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_salary)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="EXPERIENCE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_exp)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_phno)
        self.lbleid.grid(row=2,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=3,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_email)
        self.lbleid.grid(row=3,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_doc)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=3)

    def Exit(self):            
        self.master.destroy()
        
    def INSERT_doc(self):
        global e1,e2,e3,e4,e5,e6,e7,e8,e9
        e1=(self.doc_ID.get())
        e2=(self.doc_name.get())
        e3=(self.doc_sex.get())
        e4=(self.doc_age.get())
        e5=(self.doc_type.get())
        e6=(self.doc_salary.get())
        e7=(self.doc_exp.get())
        e8=(self.doc_email.get())
        e9=(self.doc_phno.get())
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("use hello")   
        p =[]
        cur.execute("SELECT * FROM doctor  WHERE doc_ID =%s",(e1,))
        for i in cur:
            p.append(i)
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "DOCTOR ID ALREADY EXISTS")     
        else:
            cur.execute("INSERT INTO doctor VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,e7,e9,e8,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA ADDED")
            con.commit()
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_doc(self.newWindow)

class D_doc:
    def __init__(self,master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_doc=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE DOCTOR WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER DOCTOR ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_doc)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_doc)
        self.DeleteB.grid(row=3,column=1)
        
    def DELETE_doc(self):        
        global inp_d
        inp_d = str(self.de1_doc.get())
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("use hello") 
        p = []
        cur.execute("select * from doctor where doc_ID=%s", (inp_d,))
        for i in cur:
            p.append(i)
        if (len(p) != 0):
            cur.execute("DELETE from doctor where doc_ID=%s", (inp_d,))
            dme = tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA DELETED")
            con.commit()
        else:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA DOESN'T EXIST")   