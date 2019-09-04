from tkinter import*
import department
import employee
import empbargraph
import attendance
def createDashboard():
    def close():
        exit()

    dashboard=Tk()
    dashboard.geometry("366x268+500+250")
    dashboard.title("Dashboard")
    dashboard.resizable(0,0)
    dashboard.config(bg='light green')
    regbtn=Button(dashboard,text='Add Department',bg='Red', fg='White',font='Arial 12 bold',command=department.newdepartment)
    regbtn.pack(fill=X,pady=5,padx=5)
    crsbtn=Button(dashboard,text='Add Employee',bg='Red', fg='White',font='Arial 12 bold',command=employee.createemployee)
    crsbtn.pack(fill=X,pady=5,padx=5)
    '''rptbtn=Button(dashboard,text='Create Report',bg='Red', fg='White',font='Arial 12 bold')
    rptbtn.pack(fill=X,pady=5,padx=5)'''
    graphbtn=Button(dashboard,text='Graph Report',bg='Red', fg='White',font='Arial 12 bold',command=empbargraph.createDepartmentGraph)
    graphbtn.pack(fill=X,pady=5,padx=5)
    graphbtn=Button(dashboard,text='Mark Attendance',bg='Red', fg='White',font='Arial 12 bold',command=attendance.createEmployeelist)
    graphbtn.pack(fill=X,pady=5,padx=5)
    graphbtn=Button(dashboard,text='View Attendance',bg='Red', fg='White',font='Arial 12 bold',command=attendance.viewAttendance)
    graphbtn.pack(fill=X,pady=5,padx=5)
    exitbtn=Button(dashboard,text='Close Application',bg='Red', fg='White',font='Arial 12 bold', command=close)
    exitbtn.pack(fill=X,pady=5,padx=5)
    dashboard.mainloop()
    
createDashboard()


