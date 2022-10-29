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
cur.execute("create table if not exists treat"
            "("
            "pat_id bigint(12) primary key,"
            "TREATMENT varchar(100) not null,"
            "TREATMENT_CODE varchar(30) not null,"
            "T_COST int(20) not null,"
            "FOREIGN KEY(PAT_ID) REFERENCES PAT(PAT_ID))")

cur.execute("create table if not exists meds"
            "("
            "pat_id bigint(12) primary key,"
            "MEDICINE_NAME varchar(100) not null,"
            "M_COST int(20) not null,"
            "M_QTY int(10) not null,"
            "FOREIGN KEY(PAT_ID) REFERENCES PAT(PAT_ID))")
 
class Billing:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.P_id=IntVar()
        self.dd = StringVar()
        self.treat_1=StringVar()
        self.treat_2=StringVar()
        self.cost_t=IntVar()
        self.med=StringVar()
        self.med_q=IntVar()
        self.price=IntVar()
                
        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "BILLING WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.P_id )
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DATE DISCHARGED(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.dd )
        self.lbldid.grid(row=1,column=1)       
        self.button2 = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE",width =25,font="Helvetica 14 bold",bg="cadet blue",command = self.UPDATE_DATE)
        self.button2.grid(row=1,column=3)
        
        self.lbltreat= Label(self.LoginFrame,text="TREATMENT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbltreat.grid(row=2,column=0)
        self.lbltreat  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_1 )
        self.lbltreat.grid(row=2,column=1) 
  
        self.lblcode_t1= Label(self.LoginFrame,text="TREATMENT CODE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblcode_t1.grid(row=3,column=0)
        self.lblcode_t1= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_2)
        self.lblcode_t1.grid(row=3,column=1)

        
        self.lblap = Label(self.LoginFrame,text="TREATMENT COST ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=4,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.cost_t)
        self.lblap.grid(row=4,column=1)
            
        self.lblmed = Label(self.LoginFrame,text="MEDICINE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblmed.grid(row=2,column=2)
        self.lblmed  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med)
        self.lblmed.grid(row=2,column=3)
        
        self.med_t1= Label(self.LoginFrame,text="MEDICINE QUANTITY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.med_t1.grid(row=3,column=2)
        self.med_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med_q)
        self.med_t1.grid(row=3,column=3)
        
        self.lblapd = Label(self.LoginFrame,text="MEDICINE PRICE ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=4,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.price)
        self.lblapd.grid(row=4,column=3)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE DATA",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_DATA)
        self.button3.grid(row=3,column=2)
        
        self.button3 = Button(self.LoginFrame2, text="GENERATE BILL",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.GEN_BILL)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)
        
    def UPDATE_DATE(self):
        global b1,b2
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("create database if not exists hello")
        cur.execute("use hello")
        b1 = (self.P_id.get())
        b2 =(self.dd.get())  
        cur.execute("UPDATE ROOM SET DATE_DISCHARGED=%s where PAT_ID=%s", (b2, b1,))
        con.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
    
    def UPDATE_DATA(self):
        global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("create database if not exists hello")
        cur.execute("use hello")
        b1 = (self.P_id.get())
        b3 = (self.treat_1.get())
        b4 = (self.treat_2.get())
        b5 = (self.cost_t.get())
        b6 = (self.med.get())
        b7 = (self.med_q.get())
        b8 = (self.price.get())   
        p = []
        cur.execute("Select * from TREAT where PAT_ID=%s", (b1,))
        for i in cur:
            p.append(i)
        l=len(p)
        if l!= 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT ID IS ALREADY REGISTERED")
        else:
            cur.execute("INSERT INTO TREAT VALUES(%s,%s,%s,%s)", (b1, b3, b4, b5,))
            cur.execute("INSERT INTO MEDS VALUES(%s,%s,%s,%s)", (b1, b6, b7, b8,))
            con.commit()
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
            
    def GEN_BILL(self):
        global b1
        b1 = (self.P_id.get())
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("create database if not exists hello")
        cur.execute("use hello")
        u=[]
        cur.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREAT natural JOIN MEDS where PAT_ID=%s",(b1,))
        for i in cur:
            u.append(i)
        for ii in u:
            self.pp=Label(self.LoginFrame,text="TOTAL AMOUNT OUTSTANDING",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.pp.grid(row=5,column=0)
            self.uu=Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=ii[0])
            self.uu.grid(row=5,column=1) 

            
    def Exit(self):            
        self.master.destroy()