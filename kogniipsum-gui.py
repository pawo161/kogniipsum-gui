import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)
plotno=Canvas(glowneOkno, width=1200, height=800)
obraz = Image.open("logo1.png")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(600,400, image=obrazTk)
plotno.pack()


L1 = Label(glowneOkno, text="Wpisz ilosc znakow(200+)")
L1.pack( side = LEFT)
E1 = Entry(glowneOkno, bd =5)
E1.pack(side = RIGHT)


def nowe_okno():
    master2 = Tk()
    master2.geometry("1200x800")
    master2.title("Tekst wygenerowany")
    number = random.randint(1, 30)
    temp = open("gp2_generated/gpt2_gentext%s.txt" % number, 'r')
    l = ''.join(map(str, temp))
    label = Label(master2, text=l[0:int(E1.get())])
    label.pack()
    def exit():
        master2.destroy()
    exit_btn = Button(master2, text='Wyjście', command=exit)
    exit_btn.place(relx=1, x=-2, y=2, anchor=NE)
    master2.mainloop()


przycisk_gen = Button(glowneOkno, text="GENERUJ KOGNIMOWĘ!", command = nowe_okno)
przycisk_gen.place(x=920,y=390)
przycisk_gen.pack(side=TOP)
wyjdz=Button(glowneOkno, command=glowneOkno.quit, text= "wychodzę...")
wyjdz.pack(side=BOTTOM)


def akcjaAutor():
    messagebox.showinfo("Autor", "Autorem jest Ismena, Marysia, Marcin, Pawel")
def akcjaUst():
    messagebox.showinfo("Ustawienia", "Nie ma co tu ustawiać...")
def akcjaKI():
    messagebox.showinfo("O Kogni ipsum", "Stuck with your research work? No worries! The best way to fill blank spaces in your research paper! Feel free to use large amounts of text. It is AI generated and gets really creative sometimes. Your cognitive lifestyle here and now! ")


pierwszeMenu = Menu(pasekMenu, tearoff=0)
pomocMenu = Menu(pasekMenu, tearoff=0)
kogniMenu = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Menu",
                        menu=pierwszeMenu)
pierwszeMenu.add_command(label="Ustawienia",
                            command=akcjaUst)

pomocMenu.add_command(label="O Autorze",
                            command=akcjaAutor)
pasekMenu.add_cascade(label="Autor",
menu=pomocMenu)

pasekMenu.add_cascade(label="Kogni Ipsum", menu=kogniMenu)
kogniMenu.add_command(label="O Kogni ipsum",
                            command=akcjaKI)

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
