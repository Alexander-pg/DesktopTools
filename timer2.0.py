from tkinter import *
from customtkinter import *

window = Tk()
window.geometry("700x600")
window.configure(bg="#335B61")
window.resizable(False,False)

scienceImage = PhotoImage(file="data-science.png")
mathImage= PhotoImage(file="physics.png")
readingImage= PhotoImage(file="reading.png")
musicImage=PhotoImage(file="music.png")
studyingImage=PhotoImage(file="studying.png")
programmingImage=PhotoImage(file="programming.png")




def createButton(img,activity,bgColor,titles,posX,posY):
    def newWIndow():
        second=Tk()
        second.title(titles)
        second.configure(bg="black")
        second.geometry("200x200")
    CTkButton(window,text= activity ,image=img,fg_color=bgColor,command=newWIndow).place(x=posX,y=posY)

Label(window,text="What am i supposed to do?",fg="white",bg="black",font="arial 20 bold").pack(pady=20)

science = createButton(scienceImage,"Learning science","#000","science window",20,100)
math = createButton(mathImage,"Studying math","black","Math window",260,100)
programming = createButton(programmingImage,"Programming","white","Programming window",480,100)
music = createButton(musicImage,"Playing guitar","white","Music window",20,400)
reading = createButton(readingImage,"Reading","black","Reading window",260,400)
studying = createButton(studyingImage,"Studying","black","Studying window",480,400)


window.mainloop()