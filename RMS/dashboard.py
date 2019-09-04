from tkinter import*
from tkinter import messagebox
import dbase as dbs
from functools import partial
def menudetail(itemid):
    def delete():
        dbs.cur.execute("delete from menulist where id='"+str(itemid)+"'")
        dbs.db.commit()
        messagebox.showinfo("Success","Record has been removed!")
        itemview.destroy()

    def update():
        if item.get()=='' or price.get()=='':
            messagebox.showwarning("Warning","All fields are mandatory!")
        else:
            dbs.cur.execute("update menulist set itemname='"+item.get()+"',\
            price='"+ str(price.get())+"' where id='"+str(itemid)+"'")
            dbs.db.commit()
            messagebox.showinfo("Success","Record has been updated!")
            itemview.destroy()
    
    itemview=Tk()
    itemview.title("Item Detail")
    itemview.geometry("300x500+433+134")
    itemview.resizable(0,0)
    dbs.cur.execute("select *from menulist where id='"+str(itemid)+"'")
    data=dbs.cur.fetchone()

    item=StringVar(itemview)
    price=StringVar(itemview)

    item.set(data[1])
    price.set(data[2])
    
    lbl=Label(itemview,text="Item Name")
    lbl.grid(row=0,column=0, padx=5, pady=10, sticky=W)
    txt1=Entry(itemview,textvariable=item,bd=2)
    txt1.grid(row=0,column=1, padx=5,pady=10, sticky=W)
    lbl=Label(itemview,text="Item Price")
    lbl.grid(row=1,column=0, padx=5, pady=10, sticky=W)
    txt2=Entry(itemview,textvariable=price,bd=2)
    txt2.grid(row=1,column=1, padx=5,pady=10, sticky=W)
    btn=Button(itemview,text="Update",command=update)
    btn.grid(row=2,column=0, padx=5,pady=10, sticky=W)
    btn=Button(itemview,text="Delete",command=delete)
    btn.grid(row=2,column=1, padx=5,pady=10, sticky=E)

    
def createMainWindow():
    menuscreen=Tk()
    menuscreen.title("RMS")
    menuscreen.geometry("600x500+383+134")
    menuscreen.resizable(0,0)
    getmenu=menulist()
    itemdc={}
    def showmenu():
        getmenu=menulist()
        r=1
        for val in getmenu:
            lbl=Label(frame2,text=r)
            lbl.grid(row=r,column=0, padx=5, pady=10, sticky=W)
            c=1
            for x in range(1,len(val)):
                lbl=Label(frame2,text=val[x])
                lbl.grid(row=r,column=c, padx=5, pady=10, sticky=W)
                c+=1
            btn=Button(frame2,text="Edit/Delete",command=partial(menudetail,val[0]))
            btn.grid(row=r, column=c, padx=5, pady=10, sticky=W)
            r+=1
    def createinvoice():
        if name.get()=='' or name.get().isspace()or mobile.get()=='' or mobile.get().isspace()or qty.get()=='' or qty.get().isspace():
            messagebox.showwarning("Warning","All fields are mandatory!")
        else:
            getitems=list1.curselection()
            getqty=list(qty.get())
            if len(getitems)==len(getqty):
                n=0
                items=''
                price=''
                sm=0
                for i in getitems:
                    itm=list1.get(i)
                    items+=itm+","
                    price+=str(itemdc[itm])+","
                    sm+=int(getqty[n])*itemdc[itm]
                    n+=1
                dbs.cur.execute("insert into invoices(name, mobile,items, price,total)\
                values('"+name.get()+"','"+mobile.get()+"','"+ items +"',\
                '"+price+"','"+ str(sm) +"')")
                dbs.db.commit()
                messagebox.showinfo("Success","Thanks for shopping:)!")
            else:
                messagebox.showwarning("Warning","Quantity Does not match!")
                
    def invoicelist():
        dbs.cur.execute("select *from invoices")
        getallinvoice=dbs.cur.fetchall()
        inview=Tk()
        inview.geometry("566x368+400+200")
        inview.title("All Invoices")
        inview.resizable(0,0)
        def myfunction(event):
            datacanvas.configure(scrollregion=datacanvas.bbox("all"),width=540,height=320)
        
        datacanvas=Canvas(inview)
        subframe=Frame(datacanvas)
        vscrollbar=Scrollbar(inview,orient="vertical",command=datacanvas.yview)
        hscrollbar=Scrollbar(inview,orient="horizontal",command=datacanvas.xview)
        datacanvas.configure(yscrollcommand=vscrollbar.set)
        datacanvas.configure(xscrollcommand=hscrollbar.set)
        vscrollbar.pack(side="right",fill="y")
        hscrollbar.pack(side="bottom",fill="x")
        datacanvas.pack(side="left")
        datacanvas.create_window((0,0),window=subframe,anchor='nw')
        subframe.bind("<Configure>",myfunction)
        lbl1=Label(subframe,text='Sr', font='Arial 11 bold')
        lbl1.grid(row=0,column=0,sticky=W, padx=2,pady=2)
        lbl1=Label(subframe,text='Name', font='Arial 11 bold')
        lbl1.grid(row=0,column=1,sticky=W, padx=2,pady=2)
        lbl1=Label(subframe,text='Mobile', font='Arial 11 bold')
        lbl1.grid(row=0,column=2,sticky=W, padx=2,pady=2)
        lbl1=Label(subframe,text='Items', font='Arial 11 bold')
        lbl1.grid(row=0,column=3,sticky=W, padx=2,pady=2)
        lbl1=Label(subframe,text='Price', font='Arial 11 bold')
        lbl1.grid(row=0,column=4,sticky=W, padx=2,pady=2)
        lbl1=Label(subframe,text='Total', font='Arial 11 bold')
        lbl1.grid(row=0,column=5,sticky=W, padx=2,pady=2)
        r=1
        for row in getallinvoice:
            invid=row[0]
            rclabel=Label(subframe,text=r,anchor=W,  font='arial 11')
            rclabel.grid(row=r,column=0,sticky=W, padx=2,pady=2)
            for column in range(1,len(row)):
                rclabel=Label(subframe,text=row[column],anchor=W,  font='arial 11')
                rclabel.grid(row=r,column=column,sticky=W, padx=2,pady=2)
            r+=1
        
    def save():
        if item.get()=='' or price.get()=='':
            messagebox.showwarning("Warning","All fields are mandatory!")
        else:
            dbs.cur.execute("insert into menulist(itemname,price) \
            values('"+item.get()+"','"+ str(price.get())+"')")
            dbs.db.commit()
            messagebox.showinfo("Success","Record has been stored!")
            item.set("")
            price.set("")
            txt1.focus_set()
            showmenu()
    item=StringVar(menuscreen)
    price=StringVar(menuscreen)
    name=StringVar(menuscreen)
    mobile=StringVar(menuscreen)
    qty=StringVar(menuscreen)
    frame1=Frame(menuscreen,bd=1, relief=SUNKEN)
    frame1.pack(side=TOP, fill=X)
    lbl=Label(frame1,text="Item Name")
    lbl.grid(row=0,column=0, padx=5, pady=10, sticky=W)
    txt1=Entry(frame1,textvariable=item,bd=2)
    txt1.grid(row=0,column=1, padx=5,pady=10, sticky=W)
    lbl=Label(frame1,text="Item Price")
    lbl.grid(row=0,column=2, padx=5, pady=10, sticky=W)
    txt2=Entry(frame1,textvariable=price,bd=2)
    txt2.grid(row=0,column=3, padx=5,pady=10, sticky=W)
    btn=Button(frame1,text="Save",command=save)
    btn.grid(row=0,column=4, padx=5,pady=10, sticky=W)

    frame2=Frame(menuscreen,bd=1,width=500, relief=GROOVE)
    frame2.pack(side=LEFT, fill=Y)
    lbl=Label(frame2,text="Sr", font='Arial 11 bold')
    lbl.grid(row=0,column=0, padx=5, pady=10, sticky=W)
    lbl=Label(frame2,text="Item",font='Arial 11 bold')
    lbl.grid(row=0,column=1, padx=5, pady=10, sticky=W)
    lbl=Label(frame2,text="Price",font='Arial 11 bold')
    lbl.grid(row=0,column=2, padx=5, pady=10, sticky=W)
    refresh=PhotoImage(file="refresh.png")
    btn=Button(frame2,text="Referesh",image=refresh,command=showmenu)
    btn.grid(row=0,column=3,padx=5, pady=10)

    frame3=Frame(menuscreen,bd=1,width=750, relief=GROOVE)
    frame3.pack(side=RIGHT,fill=Y)
    lbl=Label(frame3,text="Name")
    lbl.grid(row=0,column=0, padx=5, pady=2, sticky=W)
    txt3=Entry(frame3,textvariable=name,bd=2)
    txt3.grid(row=0,column=1, padx=5,pady=2, sticky=W)
    lbl=Label(frame3,text="Mobile")
    lbl.grid(row=1,column=0, padx=5, pady=2, sticky=W)
    txt4=Entry(frame3,textvariable=mobile,bd=2)
    txt4.grid(row=1,column=1, padx=5,pady=2, sticky=W)
    lbl=Label(frame3,text="Qty")
    lbl.grid(row=2,column=1, padx=5, pady=2, sticky=W)
    txt5=Entry(frame3,textvariable=qty,bd=2)
    txt5.grid(row=3,column=1, padx=5,pady=2, sticky=NW)

    lbl=Label(frame3,text="Item List")
    lbl.grid(row=2,column=0, padx=5, pady=2, sticky=W)
    list1=Listbox(frame3,selectmode=MULTIPLE)
    for val in getmenu:
        list1.insert(END,val[1])
        itemdc.update({val[1]:val[2]})
    
    list1.grid(row=3,column=0, padx=5,pady=2, sticky=W)

    btn=Button(frame3,text="Submit",command=createinvoice)
    btn.grid(row=3,column=1, padx=5,pady=2, sticky=SW)
    btn=Button(frame3,text="View",command=invoicelist)
    btn.grid(row=3,column=1, padx=5,pady=2, sticky=SE)
    
    showmenu()
    menuscreen.mainloop()

def menulist():
    dbs.cur.execute("select *from menulist")
    data=dbs.cur.fetchall()
    return data

createMainWindow()

