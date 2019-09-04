import matplotlib.pyplot as plt
import dbase as dbs
def createDepartmentGraph():
    dbs.cur.execute("select count(e.id), d.name from employee e inner join department d \
    on e.department=d.id group by d.name")
    getdata=dbs.cur.fetchall()
    xdst=[]
    ydst=[]
    for val in getdata:
        xdst.append(val[1])
        ydst.append(val[0])

    plt.bar(xdst,ydst, label='Employees',color='r')
    plt.legend()
    plt.xlabel("Department")
    plt.ylabel("No. of Employees")
    plt.title("Employees per Department")
    plt.show()
    
#createDepartmentGraph()
