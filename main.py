from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

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
Header = ["admno","name","class"]


def Search():
    query = searchInput.get()
    d = f"select * from students where name = '{query}'"
    cursor.execute(d)
    result = cursor.fetchall()
    print(result)
    print(query)
    global ExcelFrame
    if(ExcelFrame.winfo_exists() == 1) :
        ExcelFrame.destroy()
    ExcelFrame = Frame(app)
    ExcelFrame.pack()
    ExcelFrame.place(bordermode=OUTSIDE, x=20, y=250)
    for k in range(len(Header)):
        e = Label(ExcelFrame,width=10, text=Header[k],bd=1,relief="solid")
        e.grid(row=0, column=k) 
    i = 1
    for student in result: 
        editBtn = Button(ExcelFrame,text="edit",bd=1,relief="solid",pady=0,font=("Arial",8))
        editBtn.grid(row=i,column=len(student)+1)
        for j in range(len(student)):
            e = Label(ExcelFrame,width=10, text=student[j],bd=1,relief="solid") 
            e.grid(row=i, column=j) 
        i=i+1


def Add():

    def AddIntoDataBse():
        name = namenput.get()
        admno = admnnput.get()
        class_ = classnput.get() 
        query=f"insert into students values({admno},'{name}','{class_}')"
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

    admnLabel = Label(ExcelFrame,font=("Arial", 18),text="adm no.",bd=5,relief="ridge")
    admnLabel.grid(row=0, column=0)
    admnnput = Entry(ExcelFrame,font=("Arial", 18),textvariable=int,bd=5,relief="ridge",)
    admnnput.grid(row=0, column=1)

    nameLabel = Label(ExcelFrame,font=("Arial", 18),text="Name",bd=5,relief="ridge")
    nameLabel.grid(row=1, column=0)
    namenput = Entry(ExcelFrame,font=("Arial", 18),textvariable=Text,bd=5,relief="ridge",)
    namenput.grid(row=1, column=1)

    classLabel = Label(ExcelFrame,font=("Arial", 18),text="class",bd=5,relief="ridge")
    classLabel.grid(row=2, column=0)
    classnput = Entry(ExcelFrame,font=("Arial", 18),textvariable=Text,bd=5,relief="ridge",)
    classnput.grid(row=2, column=1)

    addbtn = Button(ExcelFrame,font=("Arial", 18),bd=2,text="Add",relief="ridge",command=AddIntoDataBse)
    addbtn.grid(row=5,column=1)

    


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
    print(result)
    for k in range(len(Header)):
        e = Label(ExcelFrame,width=10, text=Header[k],bd=1,relief="solid")
        e.grid(row=0, column=k) 
    i = 1
    for student in result: 
        editBtn = Button(ExcelFrame,text="edit",bd=1,relief="solid",pady=0,font=("Arial",8))
        editBtn.grid(row=i,column=len(student)+1)
        for j in range(len(student)):
            e = Label(ExcelFrame,width=10, text=student[j],bd=1,relief="solid") 
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


optionsLabel = Label(app,font=("Arial", 10),text="search by",relief="raised")
optionsLabel.pack()
optionsLabel.place(bordermode=OUTSIDE, x=20, y=80,width=200,height=50)
choices = ['name', 'addmission no.', 'class']
variable = StringVar(app)
variable.set('name')
searchOptn = OptionMenu(app, variable, *choices)
searchOptn.pack();
searchOptn.place(bordermode=OUTSIDE, x=220, y=80,height=50)



addBtn = Button(app,font=("Arial", 15),command=Add,text="Add",bd=5,relief="ridge")
addBtn.pack()
addBtn.place(bordermode=OUTSIDE, x=720, y=20,height=60)

showAllBtn = Button(app,font=("Arial", 15),command=ShowAll,text="Show All",bd=5,relief="ridge")
showAllBtn.pack()
showAllBtn.place(bordermode=OUTSIDE, x=850, y=20,height=60)





# Run the application
app.mainloop()