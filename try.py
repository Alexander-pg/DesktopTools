from tkinter import*
from customtkinter import *

window = Tk()

window.geometry("700x600")
window.configure(bg="#2F4A4F")
mainFrame = CTkFrame(window,width=650,height=500,fg_color="black")
mainFrame.pack_configure(pady=20)

userIMage = PhotoImage(file = "man(1).png")

myLabel = CTkLabel(mainFrame,image=userIMage,text="",fg_color="#2F4A4F",corner_radius=8)
myLabel.place(x=450,y=26)

myUser = CTkLabel(mainFrame,text_color = "white",text="jhon.html.js",corner_radius=8)
myUser.place(x=520,y=36)

window.mainloop()