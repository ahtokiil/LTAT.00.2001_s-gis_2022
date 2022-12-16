# Muusikafail on pärit https://freesound.org/people/FullMetalJedi/sounds/349473/


print('Programm ei hangu, vaid loeb helifailist andmeid ca 10 sekundit;)')


import matplotlib.pyplot as plt
from random import randrange, random, randint, choice
import turtle
from turtle import *
from colour import *
from math import *
from värvid_tekst import värv_sõne
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from andmed import andmed1, andmed2
from graafika import ring, laine


# Siit algab menüü ja valikute estitlus.
# Valitud graafiku number on funktsiooni valik väärtuseks.

root = Tk()
root.geometry("825x950")
root.title("Graafika valik")
root.config(bg="cornsilk")
root.maxsize(1000, 1000)

def valik():
   valitud = valik.get()
   return valitud

valik = IntVar()

vasak_üleval = Frame(root, width = 400, height = 400, bg = 'AntiqueWhite1')						# Ülemine vasakpoolne raam + pilt
vasak_üleval.grid(row = 0, column = 0, padx = 5, pady = 5)
pilt_1 = (Image.open("spiraal.png"))
väike_pilt1 = pilt_1.resize((400, 400))
pilt1 = ImageTk.PhotoImage(väike_pilt1)
silt1 = Label(vasak_üleval, image = pilt1)
silt1.grid(row = 0, column = 0)

parem_üleval = Frame(root, width = 400, height = 400, bg = 'light salmon')						# Ülemine parempoolne raam + pilt
parem_üleval.grid(row = 0, column = 1, padx = 5, pady = 5)
pilt_2 = (Image.open("lilleke.png"))
väike_pilt2 = pilt_2.resize((400, 400))
pilt2 = ImageTk.PhotoImage(väike_pilt2)
silt2 = Label(parem_üleval, image = pilt2)
silt2.grid(row = 0, column = 1)

valik_1_nupp = Frame(root, width = 50, height = 20)												# Esimese valiku nupp
valik_1_nupp = Radiobutton(root, text = "Minu valik", bg = 'AntiqueWhite1',
                           variable = valik, value = 1, command = valik)
valik_1_nupp.grid(row=1, column = 0, padx = 5, pady = 5)
    
valik_1_nupp = Frame(root, width = 50, height = 20)												# Teise valiku nupp
valik_1_nupp = Radiobutton(root, text = "Minu valik", bg = "light salmon",
                           variable = valik, value = 2, command = valik)
valik_1_nupp.grid(row = 1, column = 1, padx = 5, pady = 5)
    
vasak_all = Frame(root, width = 400, height = 400, bg = 'light sky blue')						# Alumine vasakpoolne raam + pilt
vasak_all.grid(row = 2, column = 0, padx = 5, pady = 5)
pilt_3 = (Image.open("kolmas_graafik.png"))
väike_pilt3 = pilt_3.resize((400, 400))
pilt3 = ImageTk.PhotoImage(väike_pilt3)
silt3 = Label(vasak_all, image = pilt3)
silt3.grid(row = 2, column = 0)

parem_all = Frame(root, width = 400, height = 400, bg = 'light goldenrod')						# Ülemine parempoolne raam + pilt
parem_all.grid(row = 2, column = 1, padx = 5, pady = 5)
pilt_4 = (Image.open("neljas_graafik.png"))
väike_pilt4 = pilt_4.resize((400, 400))
pilt4 = ImageTk.PhotoImage(väike_pilt4)
silt4 = Label(parem_all, image = pilt4)
silt4.grid(row = 2, column = 1)

valik_3_nupp = Frame(root, width = 50, height = 20)												# Kolmanda valiku nupp
valik_3_nupp = Radiobutton(root, text = "Minu valik", bg = 'light sky blue',
                           variable = valik, value = 3, command = valik)
valik_3_nupp.grid(row = 3, column = 0, padx = 5, pady = 5)

valik_4_nupp = Frame(root, width = 50, height = 20)												# Neljanda valiku nupp
valik_4_nupp = Radiobutton(root, text = "Minu valik", bg = 'light goldenrod',
                           variable = valik, value = 4, command = valik)
valik_4_nupp.grid(row = 3, column = 1, padx = 5, pady = 5)

valik_5_nupp = Frame(root, width = 100, height = 75)											# "Edasi" valiku nupp
valik_5_nupp = Button(root, text = "  Edasi  ", bg = 'red', command = root.destroy)
valik_5_nupp.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)

mainloop()

# Joonistame spiraali, kui valik on 1.
# Spiraali joonistamise algoritmi esialgne idee on pärit aadressilt https://holypython.com/turtle-spirals/

algvärvid = [100, 200, 300, 400, 500]
värvid = värv_sõne

if valik.get() == 1:
    t = turtle.Pen()
    värv = algvärvid[randrange(5)]
    t.color(värvid[värv])
    t.pensize(28)
    speed(0)
    delay(0)
    
    for samm in range(500):												
        värv += andmed2[samm]
        if värv <= 0:																			# Kui väärtused peaksid järjendist välja minema,															
            värv += abs(andmed2[samm])															# siis suuname tagasi.
        elif värv >= 551:
            värv -= andmed2[samm]
        t.color(värvid[värv])
        t.forward(2+samm/4)
        t.right(14)

    exitonclick()

# Joonistame lille, kui valik on 2.
# Poolringilise lille joonistamise algoritm on koostatud käesoleva kursuse tärnülesande lahendusena.

elif valik.get() == 2:
    
    n = randint(20, 50) 							# Õielehtede arv.
    r = randint(200, 400)							# Lehtede pikkus

    nurk = 360/n
    nurk_rad = (nurk*pi)/180
    kolmas = sqrt(2*(r**2)-2*(r**2)*cos(nurk_rad))
    r_2 = kolmas/2
    kuva = turtle.Screen()
    kuva.setup(1000,1000, startx = 300, starty = 50)

    kuva.bgcolor('gold')
    kuva.title('Lilleke rohus')
    lille_värvi_nr = randint(21,520)
    lille_värv = värvid[lille_värvi_nr]
    t = turtle.Pen()
    t.pensize(5)
    speed(0)
    delay(0)

    for i in range (n):
        t.color(lille_värv)
        t.begin_fill()
        t.forward(r)
        t.left(nurk/2)
        t.circle(r_2,180)
        t.left(nurk/2)
        t.forward(r)
        t.left(180)
        t.end_fill()
        lille_värvi_nr += int(andmed1[i][0])
        if lille_värvi_nr <= 0:
            lille_värvi_nr += abs(int(andmed1[i][0]))
        elif lille_värvi_nr > len(värvid):
            lille_värvi_nr -= abs(int(andmed1[i][0]))
        lille_värv = värvid[lille_värvi_nr]
    exitonclick()

elif valik.get() == 3:
    
    laine_img = laine(200, 200, värv_sõne[choice(algvärvid)]).resize((400, 400))

    # Akna loomine võetud siit: https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
    win = Tk()

    # Define the geometry of the window
    win.geometry("800x800")

    frame = Frame(win, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(laine_img)

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

    win.mainloop()

elif valik.get() == 4:
    ring_img = ring(200, 200, värv_sõne[choice(algvärvid)]).resize((400, 400))

    # Akna loomine võetud siit: https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
    win = Tk()

    # Define the geometry of the window
    win.geometry("800x800")

    frame = Frame(win, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(ring_img)

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

    win.mainloop()
