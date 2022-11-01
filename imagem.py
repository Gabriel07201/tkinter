from tkinter import *
from PIL import Image, ImageTk
tela = Tk()

canvas = Canvas(tela, width=500, height=450)
canvas.pack()
img = (Image.open('imagens\camiseta_preta.jpeg'))
img =  img.resize((500,300), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(40, 100, anchor=NW, image=img)

tela.mainloop()