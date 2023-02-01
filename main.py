from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
from functools import partial

from tkinter import *
import mysql.connector
from tkinter import messagebox

connection =  mysql.connector.connect(host='localhost',user='root',password="root")
cursor = connection.cursor()
cursor.execute("use csproject")
app = Tk()
app.title("School Database")
ExcelFrame = Frame(app)
ExcelFrame.pack()
ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)
Header = ["admno","name","class","disability","edit",]
HomeLabel = Label(ExcelFrame,font=("Arial", 30),text="School's Special Children Database",bd=2,background="lightgreen")
HomeLabel.pack()
HomeLabel.grid(row=4, column=1,pady=2)


def Search():
    query = searchInput.get()
    filter = variable.get()
    if filter == "name":
        d = f"select * from students where name = '{query}'"
    elif filter == "class":
        d = f"select * from students where class = '{query}'"
    elif filter == "addmission no.":
        d = f"select * from students where admno = '{query}'"
    elif filter == "disability":
        d = f"select * from students where disability = '{query}'"
    cursor.execute(d)
    result = cursor.fetchall()
    global ExcelFrame
    if(ExcelFrame.winfo_exists() == 1) :
        ExcelFrame.destroy()
    ExcelFrame = Frame(app)
    ExcelFrame.pack()
    ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)
    showTable(ExcelFrame, result)

def Add():

    def AddIntoDataBse():
        name = namenput.get()
        admno = admnnput.get()
        class_ = classnput.get() 
        dis = disnput.get() 
        query=f"insert into students values({admno},'{name}','{class_}','{dis}')"
        try : 
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Success", "student added succesfully")
            ExcelFrame.destroy()
        except : 
            messagebox.showerror("error", "some error occured pls check if every field is correctly filled")
        


    global ExcelFrame
    if(ExcelFrame.winfo_exists() == 1) :
        ExcelFrame.destroy()
    ExcelFrame = Frame(app)
    ExcelFrame.pack()
    ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)

    admnLabel = Label(ExcelFrame,font=("Arial", 16),text="adm no.",bd=5,justify=LEFT)
    admnLabel.grid(row=0, column=0)
    admnnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=int,bd=1,relief="solid",)
    admnnput.grid(row=0, column=1,pady=2)

    nameLabel = Label(ExcelFrame,font=("Arial", 16),text="Name",bd=5,justify=LEFT)
    nameLabel.grid(row=1, column=0)
    namenput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    namenput.grid(row=1, column=1,pady=2)

    classLabel = Label(ExcelFrame,font=("Arial", 16),text="class",bd=5,justify=LEFT)
    classLabel.grid(row=2, column=0)
    classnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    classnput.grid(row=2, column=1,pady=2)

    disLabel = Label(ExcelFrame,font=("Arial", 16),text="disability",bd=5,justify=LEFT)
    disLabel.grid(row=3, column=0)
    disnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    disnput.grid(row=3, column=1,pady=2)

    addbtn = Button(ExcelFrame,font=("Arial", 16),bd=4,text="Add student",relief="ridge",command=AddIntoDataBse,width="30",background="lightgreen")
    addbtn.grid(row=7,columnspan=2,column=0,pady=10)
  
def Update(student):


    def updatestudentInfo():
        query=f"update students set name='{namenput.get()}',class='{classnput.get()}',disability='{disnput.get()}' where admno = '{student[0]}'"
        try : 
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Success", "student updated succesfully")
            ExcelFrame.destroy()
        except : 
            messagebox.showerror("error", "some error occured")

    def deleteStudent():
        query=f"delete from students where admno = '{student[0]}'"
        try : 
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Success", "student deleted succesfully")
            ExcelFrame.destroy()
        except : 
            messagebox.showerror("error", "some error occured")


    global ExcelFrame
    if(ExcelFrame.winfo_exists() == 1) :
        ExcelFrame.destroy()
    ExcelFrame = Frame(app)
    ExcelFrame.pack()
    ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)

    admnLabel = Label(ExcelFrame,font=("Arial", 16),text="adm no.",bd=5,justify=LEFT)
    admnLabel.grid(row=0, column=0)
    admn_int = StringVar()
    admn_int.set(student[0])
    admnnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=admn_int,bd=1,relief="solid",state=DISABLED)
    admnnput.grid(row=0, column=1,pady=2)

    nameLabel = Label(ExcelFrame,font=("Arial", 16),text="Name",bd=5,justify=LEFT)
    nameLabel.grid(row=1, column=0)
    namenput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    namenput.insert(0,student[1])
    namenput.grid(row=1, column=1,pady=2)

    classLabel = Label(ExcelFrame,font=("Arial", 16),text="class",bd=5,justify=LEFT)
    classLabel.grid(row=2, column=0)
    classnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    classnput.insert(0,student[2])
    classnput.grid(row=2, column=1,pady=2)

    disLabel = Label(ExcelFrame,font=("Arial", 16),text="disability",bd=5,justify=LEFT)
    disLabel.grid(row=3, column=0)
    disnput = Entry(ExcelFrame,font=("Arial", 16),textvariable=Text,bd=1,relief="solid",)
    disnput.insert(0,student[3])
    disnput.grid(row=3, column=1,pady=2)

    addbtn = Button(ExcelFrame,font=("Arial", 16),bd=2,text="Update student info",relief="solid",width="30",background="blue",fg="white",command=updatestudentInfo)
    addbtn.grid(row=5,columnspan=2,column=0,pady=20)

    delbtn = Button(ExcelFrame,font=("Arial", 16),bd=2,text="Delete Student",relief="solid",width="30",background="red",fg="white",command=deleteStudent)
    delbtn.grid(row=6,columnspan=2,column=0,pady=5)

def ShowAll():
    global ExcelFrame
    if(ExcelFrame.winfo_exists() == 1) :
        ExcelFrame.destroy()
    ExcelFrame = Frame(app)
    ExcelFrame.pack()
    ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)
    d = f"select * from students"
    cursor.execute(d)
    result = cursor.fetchall()
    showTable(ExcelFrame, result)
    
def showTable(ExcelFrame,result):
    for k in range(len(Header)):
        e = Label(ExcelFrame,width=10, text=Header[k],bd=1,relief="solid",font=("Arial",15),)
        e.grid(row=0, column=k) 
    i = 1
    for student in result: 
        editBtn = Button(ExcelFrame,text="edit",width=10,bd=1,relief="solid",font=("Arial",12),background="grey", command=partial(Update,student),pady=0,padx=0,fg="white")
        editBtn.grid(row=i,column=len(student))
        

        for j in range(len(student)):
            e = Label(ExcelFrame,width=10, text=student[j],bd=1,relief="solid",font=("Arial",15)) 
            e.grid(row=i, column=j) 
            
            #e.insert(END, student[j])
        i=i+1    


searchInput = Entry(app,bd=5,font=("Arial", 15),textvariable=Text,)
searchInput.insert(0, 'text here')
searchInput.pack()
searchInput.place(bordermode=OUTSIDE, x=20, y=20,width=400,height=60)

searchBtn = Button(app,font=("Arial", 15),command=Search,text="🔍",bd=5,relief="ridge")
searchBtn.pack()
searchBtn.place(bordermode=OUTSIDE, x=420, y=20,height=60)


optionsLabel = Label(app,font=("Arial", 10),text="search by",relief="solid",bd=1)
optionsLabel.pack()
optionsLabel.place(bordermode=OUTSIDE, x=20, y=80,width=200,height=50)
choices = ['name', 'addmission no.', 'class','disability']
variable = StringVar(app)
variable.set('name')
searchOptn = OptionMenu(app, variable, *choices,)
searchOptn.pack();
searchOptn.place(bordermode=OUTSIDE, x=220, y=80,height=50)


addBtn = Button(app,font=("Arial", 15),command=Add,text="Add",bd=5,relief="ridge",activebackground='#00ff00',background="#4e4ef0",fg="white")
addBtn.pack()
addBtn.place(bordermode=OUTSIDE, x=720, y=20,height=60)

showAllBtn = Button(app,font=("Arial", 15),command=ShowAll,text="Show All",bd=5,relief="ridge",bg="#4e4ef0",fg="white",activebackground='#00ff00')
showAllBtn.pack()
showAllBtn.place(bordermode=OUTSIDE, x=850, y=20,height=60)


# Run the application
app.mainloop()