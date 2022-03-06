import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import scrolledtext
from PIL import ImageTk,Image

global score
score = 0
global prev_ans

admin_login = False

con = sqlite3.connect('data.db')
cursor = con.cursor()
global login_status
login_status = False
global ans
page = tk.Tk()
page.geometry("10000x10000")
page.title("EXAM READERS")
tk.Label(page, text="Exam Readers",
         fg="black",bg="white",font="Gabriola 45 bold").pack()
tk.Label(page,bg="white",text="'Redefining online exams'",
         fg="black", font="Gabriola 23").pack()
page.configure(bg="white")

## All the images we used are copyright free images downloaded from pexels.com
 #image1
    
image=Image.open("pic-e.jpg")
image=image.resize((400,700),Image.ANTIALIAS)
img=ImageTk.PhotoImage(image)
lab=tk.Label(image=img)

    #image2

image=Image.open("pic-b.jpg")
image=image.resize((500,600),Image.ANTIALIAS)
imge=ImageTk.PhotoImage(image)
lab2=tk.Label(image=imge)

    #image3



image=Image.open("pic-f.jpg")
image=image.resize((400,700),Image.ANTIALIAS)
imgee=ImageTk.PhotoImage(image)
lab3=tk.Label(image=imgee)
 
 
lab.place(x=0,y=0)
lab2.place(x=400,y=180)
lab3.place(x=870,y=0)

global que_count
que_count = 0


def exam():
    for widget in page.winfo_children():
       widget.destroy()
    query1 = "select * from questions"
    cursor.execute(query1)
    res = cursor.fetchall()

    def take_exam():
       global ans
       global score 
       global que_count
       global prev_ans
       if que_count > 0:
            prev_ans = ans.get()
            if prev_ans == res[que_count-1][5]:
                score = score + 1
       for widget in page.winfo_children():
            widget.destroy()
       
       
       #res contains a list of tuples. Each tuple is of the form (question,option1,option2,option3,option4)
       tk.Label(page, text="Question: "+res[que_count][0], font="Constantia 20 ").place(x=130, y=210)
       tk.Label(page, text="Option A: "+res[que_count][1], font="Constantia 20 ").place(x=130, y=290)
       tk.Label(page, text="Option B: "+res[que_count][2], font="Constantia 20 ").place(x=130, y=370)
       tk.Label(page, text="Option C: "+res[que_count][3], font="Constantia 20 ").place(x=130, y=450)
       tk.Label(page, text="Option D: "+res[que_count][4], font="Constantia 20 ").place(x=130, y=530)
       tk.Label(page, text="Answer(A-D): ", font="Constantia 20 ").place(x=130, y=610)
       ans=tk.StringVar(page)
       e6 = tk.Entry(page, textvariable=ans).place(
                x=280, y=610, width=300, height=30)
       
       que_count = que_count+1


       if que_count == 9:
           for widget in page.winfo_children():
                widget.destroy()
           tk.Label(page, text="Your Score: "+str(score), font="Constantia 20 ").place(x=130, y=370)

           
       else:
           tk.Button(page, text="Next", command=take_exam).place(
                x=280, y=690, width=250, height=40)

       
            

    tk.Button(page, text="Take Exam", command=take_exam).place(
    x=250, y=300, width=250, height=40)

    def add_question():

        for widget in page.winfo_children():
            widget.destroy()
            tk.Label(page, text="Question:", font="Constantia 20 ").place(x=130, y=210)
            tk.Label(page, text="Option A:", font="Constantia 20 ").place(x=130, y=290)
            tk.Label(page, text="Option B:", font="Constantia 20 ").place(x=130, y=370)
            tk.Label(page, text="Option C:", font="Constantia 20 ").place(x=130, y=450)
            tk.Label(page, text="Option D:", font="Constantia 20 ").place(x=130, y=530)
            tk.Label(page, text="Answer:", font="Constantia 20 ").place(x=130, y=610)
            que= tk.StringVar(page)
            opt1= tk.StringVar(page)
            opt2= tk.StringVar(page)
            opt3= tk.StringVar(page)
            opt4 = tk.StringVar(page)
            ans=tk.StringVar(page)




            e1 = tk.Entry(page, textvariable=que).place(
                x=280, y=210, width=300, height=30)
            e2 = tk.Entry(page, textvariable=opt1).place(
                x=280, y=290, width=300, height=30)
            e3 = tk.Entry(page, textvariable=opt2).place(
                x=280, y=370, width=300, height=30)
            e4 = tk.Entry(page, textvariable=opt3).place(
                x=280, y=450, width=300, height=30)
            e5 = tk.Entry(page, textvariable=opt4).place(
                x=280, y=530, width=300, height=30)
            e6 = tk.Entry(page, textvariable=ans).place(
                x=280, y=610, width=300, height=30)
            

            def insert_que():
                query="insert into questions values('{0}','{1}','{2}','{3}','{4}','{5}')".format(que.get(),opt1.get(),opt2.get(),opt3.get(),opt4.get(),ans.get())
                cursor.execute(query)
                con.commit()
                mb.showinfo("Success","Question added")
            tk.Button(page, text="Submit", command=insert_que).place(
                x=280, y=690, width=250, height=40)

    if admin_login is True:
        tk.Button(page, text="Add Questions", command=add_question).place(
        x=250, y=360, width=250, height=40)



def open_reg():
        for widget in page.winfo_children():
            widget.destroy()
        page.title("User Login")
        tk.Label(page, text="USER LOGIN", fg="Black",
             font="Gabriola 45 bold",bg="turquoise").pack()
        tk.Label(page, text="UserName:", font="Constantia 20 ",bg="turquoise",fg="black").place(x=500,y=200)
        tk.Label(page, text="login ID:", font="Constantia 20 ",bg="turquoise",fg="black").place(x=500,y=260)
        name = tk.StringVar(page)
        ID = tk.StringVar(page)
        e1 = tk.Entry(page, textvariable=name).place(
        x=700, y=200, width=300, height=30)
        e2 = tk.Entry(page, textvariable=ID).place(
        x=700, y=260, width=300, height=30)
         
        def register():
            user_already_exists = False
            a = name.get()
            b = ID.get()
            query_login = "select * from users"
            cursor.execute(query_login)
            users = cursor.fetchall()
            for i in users:
                if i[0] == a and i[1] == b:
                    user_already_exists = True
                    mb.showerror("Error","User already exists, Logging in now")
                    exam()
                    break
                else:
                    continue
            if user_already_exists is False:
                query2 = "insert into users values ('{0}','{1}')".format(a,b)
                cursor.execute(query2)
                con.commit()
                mb.showinfo("Success","User Registered!!")
                global login_status
                login_status = True
                exam()

        tk.Button(page, text="REGISTER", command=register,bg="turquoise",fg="black").place(
    x=600, y=350, width=150, height=40)
   
    

def open_login():
    for widget in page.winfo_children():
       widget.destroy()
    page.title("User Login")
    tk.Label(page, text="USER LOGIN", fg="Black",
             font="Gabriola 45 bold",bg="turquoise").pack()
    tk.Label(page, text="UserName:", font="Constantia 20 ",bg="turquoise",fg="black").place(x=500, y=200)
    tk.Label(page, text="login ID:", font="Constantia 20 ",bg="turquoise",fg="black").place(x=500, y=260)
    name = tk.StringVar(page)
    ID = tk.StringVar(page)
    e1 = tk.Entry(page, textvariable=name).place(
        x=700, y=200, width=300, height=30)
    e2 = tk.Entry(page, textvariable=ID).place(
        x=700, y=260, width=300, height=30)
    
    def login():
        a = name.get()
        b = ID.get()
        query_login = "select * from users"
        cursor.execute(query_login)
        users = cursor.fetchall()
        for i in users:

            if i[0] == a and i[1] == b and i[0] == 'admin':
                global admin_login
                admin_login = True


            if i[0] == a and i[1] == b:
                global login_status
                login_status = True
                mb.showinfo("Info", "Login successful")
                break
        if login_status is True:
            exam()
        else:
            mb.showerror("Error","Invalid credentials!")
    
    tk.Button(page, text="SUBMIT", command=login,bg="turquoise",fg="black").place(
    x=600, y=350, width=150, height=40)

tk.Button(page, text="New User", command=open_reg,font="Constantia 20 ",width=20,height=0,fg="white",bg="black").pack()
 
tk.Button(page, text="Login", command=open_login,font="Constantia 20 ",width=20,height=0,fg="white",bg="black").pack()
     

page.mainloop()
