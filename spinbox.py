from tkinter import *

tela = Tk()
tela.geometry("400x300")

s1 = Spinbox(tela, from_=0, to=10)
s1.pack()

s2 = Spinbox(tela, values=(10,20,30,40,50), wrap=True)
s2.pack()

s3 = Spinbox(tela, values=("a","b","c","d","e","f","g","h","i","j","k"))
s3.pack()

tela.mainloop()