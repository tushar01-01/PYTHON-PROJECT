from tkinter import*
from tkinter import messagebox
from functools import partial
import dbase as dbs
import department as dp
import datetime

getdept=dp.alldept()
deptlist=[]
deptdc={}
for val in getdept:
    deptlist.append(val[1])
    deptdc.update({val[1]:val[0]})

def allemployee():
    dbs.cur.execute("select e.id, e.name, e.dob, e.contact, e.email, e.address, e.profile, e.salary,\
    d.name as dname from employee e inner join department d on e.department=d.id")
    return dbs.cur.fetchall()

def employeeData(eid):
    dbs.cur.execute("select *from employee where id='"+ str(eid) +"'")
    data=dbs.cur.fetchone()
    empform=Tk()
    empform.geometry("366x368+500+200")
    empform.title("Employee Detail")

    dbdept=''
    for val in deptdc:
        if deptdc[val]==data[7]:
            dbdept=val
            break
    n=0
    for val in deptlist:
        if val==dbdept:
            break
        n+=1

    def deleteEmployee():
        dbs.cur.execute("delete from employee where id='"+ str(eid)+"'")
        dbs.db.commit()
        messagebox.showinfo("Success","Record has been removed!")
        empform.destroy()

    def updateEmployee():
        if name.get()=='' or dob.get()=='' or contact.get()=='' or email.get()=='' or address.get()=='' or profile.get()=='' or salary.get()=='':
            messagebox.showwarning("Warning","All field are mandatory!")
        else:
            dpid=deptdc[dept.get()]
            dbs.cur.execute("update employee set name='"+ name.get() +"', dob='"+ dob.get() +"', contact='"+ contact.get() +"',\
            email='"+ email.get() +"', address='"+ address.get() +"', profile='"+ profile.get() +"', department='"+ str(dpid) +"', \
            salary='"+ str(salary.get()) +"' where id='"+ str(eid) +"'")
            dbs.db.commit()
            messagebox.showinfo("Success","Employee record has been updated successfully!")
            empform.destroy()
        
    
    #variable initialization
    name=StringVar(empform)
    name.set(data[1])
    dob=StringVar(empform)
    dob.set(data[2])
    contact=StringVar(empform)
    contact.set(data[3])
    email=StringVar(empform)
    email.set(data[4])
    address=StringVar(empform)
    address.set(data[5])
    profile=StringVar(empform)
    profile.set(data[6])
    dept=StringVar(empform)
    salary=StringVar(empform)
    salary.set(data[8])

    #widgets
    lbl=Label(empform,text="Name",font='arial 11 bold')
    text1=Entry(empform,textvariable=name, bd=2)
    lbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    text1.grid(row=0, column=1, padx=5, pady=5)

    lbl=Label(empform,text="Birth Date",font='arial 11 bold')
    text2=Entry(empform,textvariable=dob, bd=2)
    lbl.grid(row=1, column=0, padx=5, pady=5,sticky=W)
    text2.grid(row=1, column=1, padx=5, pady=5)

    lbl=Label(empform,text="Contact",font='arial 11 bold')
    text3=Entry(empform,textvariable=contact, bd=2)
    lbl.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    text3.grid(row=2, column=1, padx=5, pady=5)

    lbl=Label(empform,text="Email",font='arial 11 bold')
    text4=Entry(empform,textvariable=email, bd=2)
    lbl.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    text4.grid(row=3, column=1, padx=5, pady=5)

    lbl=Label(empform,text="Address",font='arial 11 bold')
    text5=Entry(empform,textvariable=address, bd=2)
    lbl.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    text5.grid(row=4, column=1, padx=5, pady=5)

    lbl=Label(empform,text="Profile",font='arial 11 bold')
    text6=Entry(empform,textvariable=profile, bd=2)
    lbl.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    text6.grid(row=5, column=1, padx=5, pady=5)
    
    dept.set(deptlist[n])
    lbl=Label(empform,text="Department",font='arial 11 bold')
    dropdown=OptionMenu(empform,dept, *deptlist)
    lbl.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    dropdown.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    lbl=Label(empform,text="Salary",font='arial 11 bold')
    text7=Entry(empform,textvariable=salary, bd=2)
    lbl.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    text7.grid(row=7, column=1, padx=5, pady=5)

    btn1=Button(empform,text="Update",font='arial 11 bold', command=updateEmployee)
    btn2=Button(empform,text="Delete",font='arial 11 bold', command=deleteEmployee)
    btn1.grid(row=8, column=1, padx=5, pady=5, sticky=W)
    btn2.grid(row=8, column=1, padx=5, pady=5, sticky=E)
    
def viewemployee():
    getempdata=allemployee()

    vewemp=Tk()
    vewemp.geometry("366x268+500+250")
    vewemp.title("All Employee")
    vewemp.resizable(0,0)

    mainframe=Frame(vewemp, width=300, height=200)
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
    lbl=Label(subframe,text='Name',font='arial 11 bold')
    lbl.grid(row=0,column=1,padx=5,pady=5)
    lbl=Label(subframe,text='Profile',font='arial 11 bold')
    lbl.grid(row=0,column=2,padx=5,pady=5)
    lbl=Label(subframe,text='Department',font='arial 11 bold')
    lbl.grid(row=0,column=3,padx=5,pady=5)
    r=1
    for val in getempdata:
        lbl=Label(subframe,text=r)
        lbl.grid(row=r,column=0)
        lbl=Label(subframe,text=val[1])
        lbl.grid(row=r,column=1,sticky=W,padx=5,pady=5)
        lbl=Label(subframe,text=val[6])
        lbl.grid(row=r,column=2,sticky=W,padx=5,pady=5)
        lbl=Label(subframe,text=val[8])
        lbl.grid(row=r,column=3,sticky=W,padx=5,pady=5)
        btn=Button(subframe,text="View",font='arial 11 bold', command=partial(employeeData,val[0]))
        btn.grid(row=r,column=4, padx=5, pady=5)
        r+=1
    

def backup():
    getempdata=allemployee()
    fname='emp_backup_'+str(datetime.datetime.now().strftime('%d_%m_%y_%I_%M_%S'))+".xls"
    fobj=open(fname,'w')
    header='Sr\tName\tBirth Date\tContact\tEmail\tAddress\tProfile\tSalary\tDepartment\n'
    fobj.write(header)
    sr=1
    for val in getempdata:
        data=str(sr)+"\t"+val[1]+"\t"+val[2]+"\t"+str(val[3])+"\t"+val[4]+"\t"+val[5]+"\t"+val[6]+"\t"+str(val[7])+"\t"+val[8]+"\n"
        fobj.write(data)
        sr+=1
    fobj.close()
    messagebox.showwarning("Success","Backup file has been created!")
        
def createemployee():
    def saveEmployee():
        if name.get()=='' or dob.get()=='' or contact.get()=='' or email.get()=='' or address.get()=='' or profile.get()=='' or salary.get()=='':
            messagebox.showwarning("Warning","All field are mandatory!")
        else:
            dpid=deptdc[dept.get()]
            dbs.cur.execute("insert into employee(name, dob, contact, email, address, profile, department, salary)\
            values('"+ name.get() +"','"+ dob.get() +"','"+ contact.get() +"','"+ email.get() +"','"+ address.get() +"',\
            '"+ profile.get() +"','"+ str(dpid) +"','"+ str(salary.get()) +"')")
            dbs.db.commit()
            messagebox.showinfo("Success","Employee record save successfully!")
            name.set("")
            dob.set("")
            contact.set("")
            email.set("")
            address.set("")
            profile.set("")
            dept.set(deptlist[0])
            salary.set("")
            text1.focus_set()
    regform=Tk()
    regform.geometry("366x368+500+200")
    regform.title("New Employee")

    #variable initialization
    name=StringVar(regform)
    dob=StringVar(regform)
    contact=StringVar(regform)
    email=StringVar(regform)
    address=StringVar(regform)
    profile=StringVar(regform)
    dept=StringVar(regform)
    salary=StringVar(regform)

    #widgets
    lbl=Label(regform,text="Name",font='arial 11 bold')
    text1=Entry(regform,textvariable=name, bd=2)
    lbl.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    text1.grid(row=0, column=1, padx=5, pady=5)

    lbl=Label(regform,text="Birth Date",font='arial 11 bold')
    text2=Entry(regform,textvariable=dob, bd=2)
    lbl.grid(row=1, column=0, padx=5, pady=5,sticky=W)
    text2.grid(row=1, column=1, padx=5, pady=5)

    lbl=Label(regform,text="Contact",font='arial 11 bold')
    text3=Entry(regform,textvariable=contact, bd=2)
    lbl.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    text3.grid(row=2, column=1, padx=5, pady=5)

    lbl=Label(regform,text="Email",font='arial 11 bold')
    text4=Entry(regform,textvariable=email, bd=2)
    lbl.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    text4.grid(row=3, column=1, padx=5, pady=5)

    lbl=Label(regform,text="Address",font='arial 11 bold')
    text5=Entry(regform,textvariable=address, bd=2)
    lbl.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    text5.grid(row=4, column=1, padx=5, pady=5)

    lbl=Label(regform,text="Profile",font='arial 11 bold')
    text6=Entry(regform,textvariable=profile, bd=2)
    lbl.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    text6.grid(row=5, column=1, padx=5, pady=5)

    dept.set(deptlist[0])
    lbl=Label(regform,text="Department",font='arial 11 bold')
    dropdown=OptionMenu(regform,dept, *deptlist)
    lbl.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    dropdown.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    lbl=Label(regform,text="Salary",font='arial 11 bold')
    text7=Entry(regform,textvariable=salary, bd=2)
    lbl.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    text7.grid(row=7, column=1, padx=5, pady=5)

    btn1=Button(regform,text="Save",font='arial 11 bold',command=saveEmployee)
    btn2=Button(regform,text="View",font='arial 11 bold',command=viewemployee)
    btn3=Button(regform,text="Backup", font='arial 11 bold', command=backup)
    btn1.grid(row=8, column=1, padx=5, pady=5, sticky=W)
    btn2.grid(row=8, column=1, padx=5, pady=5, sticky=E)
    btn3.grid(row=8, column=0, padx=5, pady=5, sticky=W)
    

#createemployee()
