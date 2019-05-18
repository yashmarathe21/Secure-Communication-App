from tkinter import *
from tkinter import messagebox
import smtplib
    
def Login():
    e=s5.get()
    if(e=="1"):
        Second_Page()
    else:
        messagebox.showinfo("Invalid User","Incorrect Password")

def encode():
    a=""
    w = s1.get()
    for i in range(0,len(w)):
        c=int((ord(w[i])*2+2)/2)
        a=a+chr(c)+chr(c+4)+chr(c+2)+chr(c+3)
    s2.set(a)

def decode():
    a=""
    w = s3.get()
    for i in range(0,len(w),4):
        d=int((ord(w[i])*2-2)/2)
        a=a+chr(d)
    s4.set(a)

def email():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    a=s6.get()
    b=s7.get()
    c=s8.get()
    msg = s9.get()
    server.login(a,b)
    server.sendmail(a,c,msg)
    server.close()

def mail():
    root2.destroy()
    root4 = Tk()
    root4.title("Send Mail")
    root4.geometry("1150x850")
    C=Canvas(root4, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "lock.gif")
    background_label = Label(root4, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    global s6,s7,s8,s9
    s6 = StringVar()
    s7 = StringVar()
    s8 = StringVar()
    s9 = StringVar()
    label1= Label(root4,text="Enter Sender's address",font = ("Times New Roman",10))
    label1.place(x=50,y=50,height=25,width=150)
    text1 = Entry(root4,textvariable=s6,font=("Times New ROman",10))
    text1.place(x=250,y=50,height=25,width=400)
    label2=Label(root4,text="Enter Sender's password",font = ("Times New Roman",10))
    label2.place(x=50,y=90,height=25,width=150)
    text2=Entry(root4,textvariable=s7,show="*")
    text2.place(x=250,y=90,height=25,width=400)
    label3=Label(root4,text="Enter receiver's email",font = ("Times New Roman",10))
    label3.place(x=50,y=150,height=25,width=150)
    text3=Entry(root4,textvariable=s8,font=("Times New Roman",10))
    text3.place(x=250,y=150,height=25,width=400)
    label4=Label(root4,text="Enter the message",font = ("Times New Roman",10))
    label4.place(x=50,y=225,height=25,width=150)
    text4=Entry(root4,textvariable=s9,font=("Times New Roman",10))
    text4.place(x=250,y=225,height=25,width=800)
    button3 = Button(root4,text="Send Mail",command=email,font=("Times New Roman",10))
    button3.place(x=150,y=300,height=30,width=70)
    root4.mainloop()
    
def exit1():
    root2.destroy()

def exit2():
    root3.destroy()

def EncodeAMessage():
    root1.destroy()
    global root2
    root2 = Tk()
    global s1,s2
    s2=StringVar()
    s1=StringVar()
    root2.geometry("1000x800")
    root2.title("Encoding Window")
    C=Canvas(root2, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "lock.gif")
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    wel = Label(root2,text="You are here to encode",font=("Times New Roman",20))
    wel.place(x=50,y=50,height=50,width=900)
    label1 = Label(root2,text="Enter plain text",font=("Times New Roman",15))
    label1.place(x=25,y=275,height=40,width=150)
    text1 = Entry(root2,textvariable=s1,font=("Times New Roman",15))
    text1.place(x=200,y=275,height=40,width=750)
    b1 = Button(root2,text="Encode",command=encode,font=("Times New Roman",15))
    b1.place(x=500,y=345,height=40,width=100)
    label2 = Label(root2,text="Encoded Message",font=("Times New Roman",15))
    label2.place(x=25,y=415,height=40,width=150)
    text2 = Entry(root2,textvariable=s2,font=("Times New Roman",15))
    text2.place(x=200,y=415,height=40,width=750)
    b2 = Button(root2,text="Send Email",command=mail,font=("Times New Roman",25))
    b2.place(x=400,y=500,height=75,width=300)
    #b3 = Button(root2,text="Exit",command=exit1,font=("Times New Roman",25))
    #b3.place(x=400,y=500,height=75,width=300)
    root2.mainloop()
    
def DecodeAMessage():
    root1.destroy()
    global root3
    root3 = Tk()
    root3.geometry("1000x800")
    root3.title("Decoding Window")
    global s3,s4
    s3=StringVar()
    s4=StringVar()
    C=Canvas(root3, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "lock.gif")
    background_label = Label(root3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    wel = Label(root3,text="You are here to decode",font=("Times New Roman",20))
    wel.place(x=50,y=50,height=50,width=900)
    label1 = Label(root3,text="Enter cipher text",font=("Times New Roman",15))
    label1.place(x=25,y=275,height=40,width=150)
    text3 = Entry(root3,textvariable=s3,font=("Times New Roman",15))
    text3.place(x=200,y=275,height=40,width=750)
    b1 = Button(root3,text="Decode",command=decode,font=("Times New Roman",15))
    b1.place(x=500,y=345,height=40,width=100)
    label2 = Label(root3,text="Decoded Message",font=("Times New Roman",15))
    label2.place(x=25,y=415,height=40,width=150)
    text4 = Entry(root3,textvariable=s4,font=("Times New Roman",15))
    text4.place(x=200,y=415,height=40,width=750)
    b2 = Button(root3,text="Exit",command=exit2,font=("Times New Roman",25))
    b2.place(x=400,y=500,height=75,width=300)
    root3.mainloop()
    
def first_page():
    root.title("Secure Communication App Login Page")
    root.geometry("1000x800")
    wel = Label(root,text="WELCOME TO THE SECURE COMMUNICATION APP",font=("Times New Roman",25))
    wel.place(x=80,y=100,height=100,width=850)
    label=Label(root,text="Enter password",font=("Times New Roman",10))
    label.place(x=300,y=350,height=25,width=150)
    text = Entry(root,textvariable=s5,show="*")
    text.place(x=475,y=350,height=25,width=275)
    button=Button(root,text="Login",command=Login)
    button.place(x=500,y=425,height=30,width=125)

def Second_Page():
    root.destroy()
    global root1
    root1 = Tk()
    root1.geometry("1000x800")
    root1.title("Secure Communication App Choose Options")
    C=Canvas(root1, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "lock.gif")
    background_label = Label(root1, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    label5 = Label(root1,text="Do you want to encode or decode a message?",font=("Times New Roman",20))
    label5.place(x=50,y=100,height=100,width=900)
    button4 = Button(root1,text="Encode a message",command=EncodeAMessage,font=("Times New Roman",10))
    button4.place(x=360,y=350,height=50,width=350)
    button5 = Button(root1,text="Decode a message",command=DecodeAMessage,font=("Times New Roman",10))
    button5.place(x=360,y=450,height=50,width=350)
    root1.mainloop()

def Second_Page2():
    pass

def Third_Page1():
    pass

root = Tk()
s5=StringVar()
C=Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "lock.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
first_page()
root.mainloop()
