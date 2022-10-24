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
cur.execute("create table if not exists apt"
            "("
            "pat_id bigint(12) not null,"
            "doc_id varchar(12) not null,"
            "apt_no varchar(15) primary key,"
            "apt_time time not null,"
            "apt_date date not null,"
            "des char(100) not null)")
  
class Appointment:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_id=IntVar()
        self.doc_id=StringVar()
        self.apt_no=StringVar()
        self.apt_time=StringVar()
        self.apt_date=StringVar()
        self.des=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_id)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.doc_id )
        self.lbldid.grid(row=1,column=1)

    
        self.lblap = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=2,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.apt_no )
        self.lblap.grid(row=2,column=1)
            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.apt_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.apt_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=2)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=3)
        

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
        
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)

    def Exit(self):            
        self.master.destroy()
        
    def INSERT_AP(self):
        global e1,e2,e3,e4,e5,e6
        e1=(self.pat_id.get())
        e2=(self.doc_id.get())
        e3=(self.apt_no.get())
        e4=(self.apt_time.get())
        e5=(self.apt_date.get())
        e6=(self.des.get())
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("use hello")
        p=[]
        cur.execute("SELECT * FROM APT WHERE APT_NO=%s",(e3,))
        for i in cur:
            p.append(i)
        l=len(p)
        if l==0:
            cur.execute("insert into apt values(%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APT SET SUCCSESSFULLY")
            con.commit()
        else:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "APT ALREADY EXISTS")
       
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)
    def S_AP_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           
     
class DEL_AP:
    def __init__(self,master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de=StringVar()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENT NO TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)
        
    def DELETE_AP(self):        
        global inp_d
        inp_d = self.de1_ap.get()
        con=sq.connect(host="localhost",user="root",password="alanwalker")
        cur=con.cursor()
        cur=con.cursor(buffered=True)
        cur.execute("use hello")
        v=[]
        cur.execute("select * from apt where apt_no=%s",(inp_d,))
        for j in cur:
            v.append(j)
        l1=len(v)
        if l1==0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT apt NOT FIXED")
        else:
            cur.execute('DELETE FROM apt where apt_no=%s', (inp_d ,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
            con.commit()
        
class SEA_AP:
    def __init__(self,master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.entry=StringVar()
        self.entry1=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lbldate = Label(self.LoginFrame,text="ENTER THE APPOINTMENT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldate.grid(row=0,column=0)
        self.lbldate= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lbldate.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_AP)
        self.SearchB.grid(row=0,column=1)    

    def SEARCH_AP(self):
        global t,i,l1,ap
        cur=con.cursor()
        ap=(self.entry.get())
        cur.execute("use hello")
        p=[]
        cur.execute("select * from apt where apt_no=%s",(ap,))
        for i in cur:
            p.append(i)
        l1=len(p)
        if l1==0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","NO APPOINTMENT FOR TODAY")
        else:
            t=[]
            cur.execute("SELECT PAT_ID,NAME,APT_NO,DOC_ID,APT_DATE,APT_TIME FROM PAT NATURAL JOIN apt where APT_NO=%s",(ap,))
            for j in cur:
                t.append(j)     
            for i in t:
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)                        
                self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=3,column=0)
                self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis3.grid(row=3,column=1)

                self.l4 = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=4,column=0)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis4.grid(row=4,column=1)
                        
                self.l5 = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l5.grid(row=5,column=0)
                self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
                self.dis5.grid(row=5,column=1)