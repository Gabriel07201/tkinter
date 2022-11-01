from tkinter import *

tela = Tk()

valor_a = IntVar()

ra_1 = Radiobutton(tela, text="Opção A 1", variable=valor_a, value=1)
ra_2 = Radiobutton(tela, text="Opção A 2", variable=valor_a, value=2)
ra_3 = Radiobutton(tela, text="Opção A 3", variable=valor_a, value=3)
ra_1.pack()
ra_2.pack()
ra_3.pack()

ra_1.select()

def ver_racio():
    print(valor_a.get())

cmd = Button(tela, text='Verificar', command=ver_racio)
cmd.pack()

tela.mainloop()