from tkinter import *
from customtkinter import *
import time

window = Tk()
window.configure(bg="#040404")
window.resizable(False,False)
window.geometry("800x700")


userImage = PhotoImage(file="man(1).png")

searchImage = PhotoImage(file="search(1)(1).png")

CTkButton(window,image=searchImage,corner_radius=8,fg_color="white",text="",width=20).place(x=50,y=35)
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

CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=70,y=200)
CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=330,y=200)
CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=590,y=200)


CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=70,y=450)
CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=330,y=450)
CTkFrame(window,width=150,height=150,fg_color="#A40A8F").place(x=590,y=450)

window.mainloop()