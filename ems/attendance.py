from tkinter import*
from tkinter import messagebox
from functools import partial
import dbase as dbs
import datetime
import employee as emp

getemplist=emp.allemployee()
empdc={}
for val in getemplist:
    empdc.update({val[1]:val[0]})

#print(empdc)

def viewAttendance():
    dbs.cur.execute("select *from attendance")
    data=dbs.cur.fetchall()
    attendancedc={}
    
    def showattendance(event):
        getdt=datelist.get(datelist.curselection())
        emplist.delete(0,END)
        getpresent=attendancedc[getdt].split(',')
        getpresent.pop()
        for val in empdc:
            nam=''
            if str(empdc[val]) in getpresent:
                nam=val+" (P)"
            else:
                nam=val+" (A)"
            emplist.insert(END,nam)
        
    rptview=Tk()
    rptview.geometry("366x368+500+200")
    rptview.title("View Attendance")
    rptview.resizable(0,0)
    
    frame1=Frame(rptview,bd=1, relief=SUNKEN, width=150)
    frame1.pack(side=LEFT, fill=Y)
    lbl=Label(frame1,text="Select a Date", font='arial 10 bold', bg='black',fg='white')
    lbl.pack(side=TOP, fill=X)
    datelist=Listbox(frame1)
    vscroll1=Scrollbar(frame1,orient=VERTICAL,command=datelist.yview)
    vscroll1.pack(side=RIGHT, fill=Y)
    for val in data:
        datelist.insert(END,val[1])
        attendancedc.update({val[1]:val[2]})
    datelist.pack(side=LEFT,fill=Y)
    datelist.config(yscrollcommand=vscroll1.set)
    datelist.bind("<<ListboxSelect>>",showattendance)
    
    frame2=Frame(rptview,bd=1, relief=SUNKEN, width=216)
    frame2.pack(side=RIGHT,fill=Y)
    emplist=Listbox(frame2)
    vscroll2=Scrollbar(frame2,orient=VERTICAL,command=datelist.yview)
    vscroll2.pack(side=RIGHT, fill=Y)
    emplist.pack(side=LEFT,fill=Y)
    emplist.config(yscrollcommand=vscroll2.set)
    rptview.mainloop()
    
#viewAttendance()

def createEmployeelist():
    def markAttendance():
        p=''
        for  v in varlist:
            p+=str(v.get())+","
        d=datetime.datetime.today().strftime("%d-%m-%y")
        dbs.cur.execute("insert into attendance(adate,eid) values('"+ str(d) +"','"+ p +"')")
        dbs.db.commit()
        messagebox.showinfo("Success","Attendance marked!")
    atnview=Tk()
    atnview.geometry("366x368+500+200")
    atnview.title("Mark Attendance")
    atnview.resizable(0,0)

    mainframe=Frame(atnview, width=300, height=200)
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
    lbl=Label(subframe,text='Status',font='arial 11 bold')
    lbl.grid(row=0,column=2,padx=5,pady=5)
    r=1
    varlist=[]
    for val in empdc:
        var="sts_"+str(r)
        var=IntVar(atnview)
        varlist.append(var)
        lbl=Label(subframe,text=r)
        lbl.grid(row=r,column=0)

        lbl=Label(subframe,text=val)
        lbl.grid(row=r,column=1,sticky=W,padx=5,pady=5)

        chk=Checkbutton(subframe,onvalue=empdc[val],offvalue=0, variable=var)
        chk.grid(row=r,column=2,sticky=W,padx=5,pady=5)
        r+=1
    btn=Button(subframe, text="Submit", font='arial 11 bold', command=markAttendance)
    btn.grid(row=r, column=2, sticky=E, padx=5, pady=5)
#createEmployeelist()
