from tkinter import *

tela = Tk()

lista = Listbox(tela)
lista.pack()

# inserindo 1 item de cada vez
lista.insert(0, "Primeiro item da lista")
lista.insert(1, "Segundo item da lista")
lista.insert(END, "Terceiro item da lista")

# inserindo vários itens
nomes = ['Joao', 'Ana', 'Carlos']
for nome in nomes:
    lista.insert(END, nome)

lista.delete(3,3)

def executar():
    print(lista.get(ACTIVE))

cmd = Button(tela, text='executar', command=executar)
cmd.pack()

tela.mainloop()