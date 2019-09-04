from tkinter import*
from tkinter import messagebox
from functools import partial
import dbase as dbs

def alldept():
    dbs.cur.execute("select *from department")
    return dbs.cur.fetchall()

def viewdepartment(did):
    dbs.cur.execute("select *from department where id='"+ str(did) +"'")
    data=dbs.cur.fetchone()

    def updatedept():
        if dept.get()=='' or email.get()=='':
            messagebox.showwarning("Warning","Department or email can't be blank")
        else:
            dbs.cur.execute("update department set name='"+ dept.get() +"', email='"+ email.get() +"' where id='"+ str(did) +"'")
            dbs.db.commit()
            messagebox.showinfo("Success","Department has been updated")
            editdept.destroy()
            
    def deletedept():
        dbs.cur.execute("delete from department where id='"+ str(did) +"'")
        dbs.db.commit()
        messagebox.showinfo("Success","Department has been deleted")
        editdept.destroy()
    
    editdept=Tk()
    editdept.geometry("366x268+500+250")
    editdept.title("New Department")
    editdept.resizable(0,0)
    #tkinter variable initialization
    dept=StringVar(editdept)
    email=StringVar(editdept)

    #set value to fields
    dept.set(data[1])
    email.set(data[2])

    #widgets initialization
    lbl=Label(editdept,text='Department', font='arial 11 bold')
    text1=Entry(editdept,textvariable=dept,bd=2)
    lbl.grid(row=0, column=0, sticky=W, padx=5,pady=5)
    text1.grid(row=0, column=1, sticky=W, padx=5,pady=5)

    lbl=Label(editdept,text='Dept. Email', font='arial 11 bold')
    text2=Entry(editdept,textvariable=email,bd=2)
    lbl.grid(row=1, column=0, sticky=W, padx=5,pady=5)
    text2.grid(row=1, column=1, sticky=W, padx=5,pady=5)

    btn1=Button(editdept,text='Update',font='arial 11 bold',command=updatedept)
    btn2=Button(editdept,text='Delete',font='arial 11 bold',command=deletedept)
    btn1.grid(row=2, column=1, sticky=W, padx=5,pady=5)
    btn2.grid(row=2, column=1, sticky=E, padx=5,pady=5)
    editdept.mainloop()
    


def viewalldept():
    getdept=alldept()

    vewdept=Tk()
    vewdept.geometry("366x268+500+250")
    vewdept.title("All Department")
    vewdept.resizable(0,0)

    mainframe=Frame(vewdept, width=300, height=200)
    mainframe.pack(fill=BOTH)
    datacanvas=Canvas(mainframe)
    subframe=Frame(datacanvas)
    subframe.pack(fill=BOTH)
    vscrollbar=Scrollbar(mainframe, orient='vertical',command=datacanvas.yview)
    vscrollbar.pack(side=RIGHT,fill=Y)
    hscrollbar=Scrollbar(mainframe, orient='horizontal', command=datacanvas.xview)
    hscrollbar.pack(side=BOTTOM,fill=X)
    datacanvas.pack(side=LEFT)
    datacanvas.configure(yscrollcommand=vscrollbar.set)
    datacanvas.configure(xscrollcommand=hscrollbar.set)

    def myfunction(event):
        datacanvas.configure(scrollregion=datacanvas.bbox("all"),width=340,height=300)

    datacanvas.create_window((0,0),window=subframe,anchor='nw')
    subframe.bind("<Configure>",myfunction)

    lbl=Label(subframe,text='Sr',font='arial 11 bold')
    lbl.grid(row=0,column=0,padx=5,pady=5)
    lbl=Label(subframe,text='Department',font='arial 11 bold')
    lbl.grid(row=0,column=1,padx=5,pady=5)
    lbl=Label(subframe,text='Email',font='arial 11 bold')
    lbl.grid(row=0,column=2,padx=5,pady=5)
    r=1
    for val in getdept:
        lbl=Label(subframe,text=r)
        lbl.grid(row=r,column=0)
        for i in range(1,len(val)):
             lbl=Label(subframe,text=val[i])
             lbl.grid(row=r,column=i,sticky=W,padx=5,pady=5)
        btn=Button(subframe,text="View",font='arial 11 bold',command=partial(viewdepartment,val[0]))
        btn.grid(row=r,column=i+1, padx=5, pady=5)
        r+=1
    
    

def newdepartment():
    def savedept():
        if dept.get()=='' or email.get()=='':
            messagebox.showwarning("Warning","Department name or email can't be blank")
        else:
            dbs.cur.execute("insert into department(name, email) values('"+ dept.get()+"','"+ email.get() +"')")
            dbs.db.commit()
            dept.set('')
            email.set('')
            text1.focus_set()
        
    newdept=Tk()
    newdept.geometry("366x268+500+250")
    newdept.title("New Department")
    newdept.resizable(0,0)
    #tkinter variable initialization
    dept=StringVar(newdept)
    email=StringVar(newdept)

    #widgets initialization
    lbl=Label(newdept,text='Department', font='arial 11 bold')
    text1=Entry(newdept,textvariable=dept,bd=2)
    lbl.grid(row=0, column=0, sticky=W, padx=5,pady=5)
    text1.grid(row=0, column=1, sticky=W, padx=5,pady=5)

    lbl=Label(newdept,text='Dept. Email', font='arial 11 bold')
    text2=Entry(newdept,textvariable=email,bd=2)
    lbl.grid(row=1, column=0, sticky=W, padx=5,pady=5)
    text2.grid(row=1, column=1, sticky=W, padx=5,pady=5)

    btn1=Button(newdept,text='Save',font='arial 11 bold',command=savedept)
    btn2=Button(newdept,text='View',font='arial 11 bold',command=viewalldept)
    btn1.grid(row=2, column=1, sticky=W, padx=5,pady=5)
    btn2.grid(row=2, column=1, sticky=E, padx=5,pady=5)
    newdept.mainloop()

#newdepartment()
    
    
