from tkinter import *
from customtkinter import *
import time

window = Tk()
window.configure(bg="#040404")
window.resizable(False,False)
window.geometry("800x700")


userImage = PhotoImage(file="man(1).png")

searchImage = PhotoImage(file="search(1)(1).png")

readingImage=PhotoImage(file="reading-book(1).png")
scienceImage = PhotoImage(file="science(1).png")
mathImage = PhotoImage(file="calculating(1).png")
logicImage = PhotoImage(file="skills(1).png")
musicImage = PhotoImage(file="musical-notes(1).png")
programmingImage = PhotoImage(file="data(1).png")

CTkButton(window,image=searchImage,corner_radius=8,fg_color="white",text="",hover_color="#A40A8F",width=20).place(x=50,y=35)
CTkEntry(window,corner_radius=8,fg_color="white",width=200,height=25,text_color="black").place(x=110,y=38)

CTkLabel(window,image=userImage,text="",fg_color="#A40A8F",corner_radius=8).place(x=590,y=20)
CTkLabel(window,text="Jhon.html.js",text_color="white",font=("Modern", 16,)).place(x=670,y=30)

def clock():
    clockTime=time.strftime("%H:%M:%S %p")
    current_time.configure(text=clockTime)
    current_time.after(1000,clock)

current_time = CTkLabel(window,text="",text_color="white",font=("Modern", 24,))
current_time.pack_configure(pady= 150)
clock()

###Activities

 def timer():
    times = int(hrs.get())*3600+int(mins.get())*60 + int(sec.get())

    while times > -1:
        minute,second=(times//60,times %60)
        hour = 0

        if minute > 60:
            hour,minute=(minute//60,minute %60)



        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        secWindow.update()
        time.sleep(1)

        if(times ==0):
            sec.set("00")
                hrs.set("00")
                mins.set("00")

            times -= 1

def defineProgramming():
    
    secWindow = CTk()
    secWindow.geometry("400x400")
    secWindow.resizable(False,False)
    secWindow.configure(bg="#040404")

    CTkLabel(secWindow,text="Jhon.html.js",text_color="white",font=("Modern", 16,)).place(x=270,y=30)
    

    hrs = StringVar()
    Entry(secWindow,textvariable=hrs,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=30,y=155)
    hrs.set("00")

    mins = StringVar()
    Entry(secWindow,textvariable=mins,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=150,y=155)
    mins.set("00")

    sec = StringVar()
    Entry(secWindow,textvariable=sec,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=270,y=155)
    sec.set("00")

    CTkButton(secWindow,text="Start",width=80,height=10,fg_color="#A40A8F",text_color="white",command=Timer).pack()

   
            CTkButton(secWindow,text="Start",width=80,height=10,fg_color="#A40A8F",text_color="white",command=timer).pack()

def defineMusic():
    
    print("music")



def defineScience():
    
    print("Science")



def defineMath():
    
    print("programming")



def defineLogic():
    
    print("programming")



def defineReading():
    
    print("programming")






CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=programmingImage,text="",corner_radius=8).place(x=70,y=200)
CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=musicImage,text="",corner_radius=8).place(x=330,y=200)
CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=mathImage,text="",corner_radius=8).place(x=590,y=200)


CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=scienceImage,text="",corner_radius=8).place(x=70,y=450)
CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=logicImage,text="",corner_radius=8).place(x=330,y=450)
CTkLabel(window,width=150,height=150,fg_color="#A40A8F",image=readingImage,text="",corner_radius=8).place(x=590,y=450)

###BUTTONS

CTkButton(window,width=100,height=20,fg_color="white",text="Programming",text_color="black",hover_color="#A40A8F",command=defineProgramming).place(x=95,y=360)
CTkButton(window,width=100,height=20,fg_color="white",text="Music",text_color="black",hover_color="#A40A8F",command=defineMusic).place(x=355,y=360)
CTkButton(window,width=100,height=20,fg_color="white",text="Math",text_color="black",hover_color="#A40A8F",command=defineMath).place(x=615,y=360)


CTkButton(window,width=100,height=20,fg_color="white",text="Science",text_color="black",hover_color="#A40A8F",command=defineScience).place(x=95,y=610)
CTkButton(window,width=100,height=20,fg_color="white",text="Logic",text_color="black",hover_color="#A40A8F",command=defineLogic).place(x=355,y=610)
CTkButton(window,width=100,height=20,fg_color="white",text="Reading",text_color="black",hover_color="#A40A8F",command=defineReading).place(x=615,y=610)

window.mainloop()