
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)
plotno=Canvas(glowneOkno, width=1200, height=800)
plotno.pack(side=LEFT)

guzik=Frame(glowneOkno, width=100, height=800, bg='red')
guzik.pack()

wyjdz=Button(guzik, command=glowneOkno.quit, text= "WYCHODZĘ!")
wyjdz.pack()

obraz = Image.open("l.jpg")
obrazTk=ImageTk.PhotoImage(obraz)

plotno.create_image(400,400, image=obrazTk)

def akcjaZrob():
    messagebox.showinfo("coś", "Wyświetlam info")

def akcjaAutor():
    messagebox.showinfo("Autor", "Autorem jest Ismena, Marysia, Marcin, Pawel")
def akcja():
    messagebox.showinfo("idek,","Cos nowego")



pierwszeMenu = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Pierwsze",
                        menu=pierwszeMenu)
pomocMenu = Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="O Autorze",
                            command=akcjaAutor)


glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
