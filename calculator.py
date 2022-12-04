from tkinter import *
from math import *

def toplaiş():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1+s2))
def çıkartiş():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1-s2))
def çarpmaiş():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1*s2))
def bölmeiş():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1/s2))
def üsalma():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1**s2))
def karakök():
    s1=float(sayi1.get())
    sonuc.configure(text=str(sqrt(s1)))
def sinal():
    s1=float(sayi1.get())
    sonuc.configure(text=str(sin(radians(s1))))
def cosal():
    s1=float(sayi1.get())
    sonuc.configure(text=str(cos(radians(s1))))



sayfa=Tk()
sayfa.title("Hesap Makinesi")
sayfa.geometry("327x276")

sonuc=Label(sayfa,text="SONUÇ",font=("Bahnschrift SemiLight SemiConde",8),width=20,bg="#000080",fg="white")
sonuc.grid(row=1,column=2)

sayi1=Entry(sayfa,font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#750d02",fg="#699ec3")
sayi1.grid(row=2,column=2)
sayi11=Label(sayfa,text="1.SAYI--->",font=("Bahnschrift SemiLight SemiConde",16))
sayi11.grid(row=2,column=1)

sayi2=Entry(sayfa,font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#750d02",fg="#699ec3")
sayi2.grid(row=3,column=2)
sayi22=Label(sayfa,text="2.SAYI--->",font=("Bahnschrift SemiLight SemiConde",16))
sayi22.grid(row=3,column=1)

topla=Button(sayfa,text="+",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=toplaiş,relief="groove")
topla.grid(row=4,column=1)

çıkart=Button(sayfa,text="-",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=çıkartiş,relief="groove")
çıkart.grid(row=4,column=3)

çarpma=Button(sayfa,text="x",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=çarpmaiş,relief="groove")
çarpma.grid(row=5,column=1)

bölme=Button(sayfa,text="÷",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=bölmeiş,relief="groove")
bölme.grid(row=5,column=3)

üstalma=Button(sayfa,text="x^y",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=üsalma,relief="groove")
üstalma.grid(row=6,column=1)

karakökal=Button(sayfa,text="√",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=karakök,relief="groove")
karakökal.grid(row=6,column=3)

sinüsal=Button(sayfa,text="sin(x)",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=sinal,relief="groove")
sinüsal.grid(row=7,column=1)

cosinüsal=Button(sayfa,text="cos(x)",font=("Bahnschrift SemiLight SemiConde",16),width=10,bg="#587F40",command=cosal,relief="groove")
cosinüsal.grid(row=7,column=3)

sayfa.mainloop()
