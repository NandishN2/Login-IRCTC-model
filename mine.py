from tkinter import *
import random as rn
from tkinter import messagebox
import time as t
new=Tk()
new.title("Welcome to IRCTC")
l1=Label(new,text="INDIAN RAILWAYS",bg="orange",fg="white",width=30,height=2,font=("calibri",14))
l1.pack()
l2=Label(new,text="Welcome to IRCTC",bg="orange",fg="white",width=32,height=1,font=("calibri",13))
l2.place(x=620,y=70)
y=StringVar()
x=StringVar()
l3=Label(new,text="UserName :")
l3.place(x=630,y=120)
E1=Entry(new,bg="blue",fg="white",textvariable=y)
E1.place(x=700,y=120)
l4=Label(new,text="Password :")
l4.place(x=630,y=150)
E2=Entry(new,bg="blue",fg="white",textvariable=x)
E2.place(x=700,y=150)
i1=PhotoImage(file="C:/Users/nandi/OneDrive/Desktop/images.png")
l5=Label(new,image=i1)
l5.place(x=615,y=320)
l6=Label(new,text="https://IndianRailways_Booking_@IRCTC")
l6.place(x=650,y=500)
def name():
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_=?'
    l=[]
    for i in range(6):
         b=rn.choice(a)
         l.append(b)
    c="".join(l)
    return c

l8=Label(new,text="Enter the captcha:",bg='white',fg='black')
l8.place(x=655,y=220)
v=StringVar()
e = name()
l7 = Label(new, text=e, width=10, height=1, bg='white', fg='black')
l7.place(x=630, y=180)


def edit():
    d=v.get()
    file=open(r'C:/Users/nandi/PycharmProjects/pythonProject2/user.text',"r")
    i=file.read().splitlines()
    z=y.get()
    m=x.get()
    if z==''or m=='':
        messagebox.showwarning("provide details","please provide your details")
    elif d=='':
        messagebox.showwarning("enter captcha","enter the captcha")
    elif z not in i or m not in i:
        messagebox.showwarning("invalid ","invalid ussername or password")
    elif d!=e:
        messagebox.showwarning("caution","Entered captcha wrongly")
    elif z in i and d==e and m in i :
        messagebox.showinfo("success", "login is successful ")


B1=Button(new,text="Login",command=edit,width=33,bg="orange",fg="white")
B1.place(x=650,y=260)
B2=Button(new,text="Signup",fg="blue",bd=0)
B2.place(x=800,y=290)
la=Label(new,text="Don't have an account :")
la.place(x=670,y=290)
E3=Entry(new,bg="white",fg="black",textvariable=v)
E3.place(x=765,y=220)

new.mainloop()