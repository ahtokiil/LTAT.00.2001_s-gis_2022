import tkinter
from tkinter import *
from PIL import Image, ImageTk

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

print(valik.get())
