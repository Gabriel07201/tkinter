from tkinter import *

tela = Tk()
tela.geometry("600x400")


meuMenu = Menu(tela)
meuMenu.add_command(label="edit")

fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="novo")
fileMenu.add_command(label="open")
fileMenu.add_command(label="save")
meuMenu.add_cascade(label="File", menu=fileMenu)

tela.configure(menu=meuMenu)

tela.mainloop()