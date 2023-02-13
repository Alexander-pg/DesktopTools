from tkinter import *
import time
from playsound import playsound 

root = Tk()
root.title("Countdown timer")
root.geometry("600x500")
root.resizable(False,False)
root.configure(bg="#000")

heading = Label(text="Timer",font= "arial 30 bold",bg = "#000",fg="#ea3548")
heading.pack(pady=10)

#clock
Label(root,font="arial 15 bold",text="Current time:",bg="papaya whip").place(x=65,y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)#after 1000 miliseconds actualize the function clock

current_time = Label(root,text="",font="arial 15 bold",fg="#000",bg="#fff")
current_time.place(x=195,y=70)
clock()

#timer

hrs = StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=30,y=155)
hrs.set("00")

mins = StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=150,y=155)
mins.set("00")

sec = StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50",bd=0,bg="#000",fg="#fff").place(x=270,y=155)
sec.set("00")

Label(root,text="Hours",bg="#000",fg="#fff").place(x=105,y=200)
Label(root,text="Minutes",bg="#000",fg="#fff").place(x=225,y=200)
Label(root,text="Seconds",bg="#000",fg="#fff").place(x=345,y=200)


        

def Timer():
    times = int(hrs.get())*3600+int(mins.get())*60 + int(sec.get())

    while times > -1:
        minute,second=(times//60,times %60)
        hour = 0

        if minute > 60:
            hour,minute=(minute//60,minute %60)



        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(times ==0):
            sec.set("00")
            hrs.set("00")
            mins.set("00")

        times -= 1


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def face():
    hrs.set("01")
    mins.set("02")
    sec.set("00")

def eggs():
    hrs.set("12")
    mins.set("02")
    sec.set("00")

    

brushing = Button(root,text="Brush",fg="white",bg = "black",command= brush)
brushing.place(x=100,y=300)

facing = Button(root,text="Face",fg="white",bg = "black",command=face)
facing.place(x=250,y=300)


egging = Button(root,text="Eggs",fg="white",bg = "black",command=eggs)
egging.place(x=500,y=300)

button = Button(root,text="Start",bg="red",fg="white",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=100,pady=40,side=BOTTOM)



root.mainloop()






