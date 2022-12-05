from tkinter import *
from math import *

def addjob():
    s1=float(num1.get())
    s2=float(num2.get())
    equal.configure(text=str(s1+s2))
def subtractjob():
    s1=float(num1.get())
    s2=float(num2.get())
    equal.configure(text=str(s1-s2))
def çarpmajob():
    s1=float(num1.get())
    s2=float(num2.get())
    equal.configure(text=str(s1*s2))
def dividejob():
    s1=float(num1.get())
    s2=float(num2.get())
    equal.configure(text=str(s1/s2))
def üsalma():
    s1=float(num1.get())
    s2=float(num2.get())
    equal.configure(text=str(s1**s2))
def karakök():
    s1=float(num1.get())
    equal.configure(text=str(sqrt(s1)))
def sinal():
    s1=float(num1.get())
    equal.configure(text=str(sin(radians(s1))))
def cosal():
    s1=float(num1.get())
    equal.configure(text=str(cos(radians(s1))))



page=Tk()
page.title("Calculator")
page.geometry("327x276")
page.maxsize(327,276)
page.minsize(327,276)

equal=Label(page,text="EQUAL",font=("Bahnschrift SemiLight SemiConde",8),width=20,bg="#000080",fg="white")
equal.grid(row=1,column=2)

num1=Entry(page,font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#750d02",fg="#699ec3")
num1.grid(row=2,column=2)
num11=Label(page,text="1.num--->",font=("Bahnschrift SemiLight SemiConde",16))
num11.grid(row=2,column=1)

num2=Entry(page,font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#750d02",fg="#699ec3")
num2.grid(row=3,column=2)
num22=Label(page,text="2.num--->",font=("Bahnschrift SemiLight SemiConde",16))
num22.grid(row=3,column=1)

add=Button(page,text="+",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=addjob,relief="groove")
add.grid(row=4,column=1)

subtract=Button(page,text="-",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=subtractjob,relief="groove")
subtract.grid(row=4,column=3)

multiply=Button(page,text="x",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=çarpmajob,relief="groove")
multiply.grid(row=5,column=1)

divide=Button(page,text="÷",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=dividejob,relief="groove")
divide.grid(row=5,column=3)

square=Button(page,text="x^y",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=üsalma,relief="groove")
square.grid(row=6,column=1)

squareroot=Button(page,text="√",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=karakök,relief="groove")
squareroot.grid(row=6,column=3)

sinüsal=Button(page,text="sin(x)",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=sinal,relief="groove")
sinüsal.grid(row=7,column=1)

cosinüsal=Button(page,text="cos(x)",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=cosal,relief="groove")
cosinüsal.grid(row=7,column=3)

page.mainloop()
