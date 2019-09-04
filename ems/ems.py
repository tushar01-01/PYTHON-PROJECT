from tkinter import*
from tkinter import messagebox
import dashboard
import dbase as dbs
mainscreen=Tk()
mainscreen.geometry("366x268+500+250")
mainscreen.title("Login Form")
mainscreen.config(bg='yellow')
uname=StringVar(mainscreen)
upass=StringVar(mainscreen)

def close():
    exit()
def login():
    if uname.get()=="" or upass.get()=="":
        messagebox.showwarning("Warning","User name or password can't be blank")
    else:
        u=uname.get()
        p=upass.get()
        dbs.cur.execute("select *from admin where email='"+ u +"' and password='"+ p +"'")
        try:
            if len(dbs.cur.fetchone())>0:
                dashboard.createDashboard()
        except:
            messagebox.showerror("Error","Invalid Login detail")
        
        
lbl1=Label(mainscreen,text="User name", font='Arial 12 bold', bg='yellow',fg='red')
lbl2=Label(mainscreen,text="Password", font='Arial 12 bold', bg='yellow',fg='red')
txt1=Entry(mainscreen,bd=2, width=40,textvariable=uname)
txt2=Entry(mainscreen,bd=2, width=40,textvariable=upass,show='*')
btn=Button(mainscreen,text='Login',bg="green",fg="white",font='Arial 12 bold',activebackground='blue',command=login)
btn2=Button(mainscreen,text='Close',bg="Blue",fg="white",font='Arial 12 bold',activebackground='blue',command=close)
lbl1.place(x=10,y=10)
lbl2.place(x=10,y=50)
txt1.place(x=100,y=10)
txt2.place(x=100,y=50)
btn.place(x=100,y=90)
btn2.place(x=170,y=90)
