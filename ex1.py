from tkinter import *

def mostrar_nome():
    nome = entry.get()
    label_final = Label(tela, text="O seu nome é " + nome)
    label_final.grid()


tela = Tk()
tela.title('App')
tela.geometry("200x100")

Label_1 = Label(tela, text='Escrava o seu nome:')
entry = Entry(tela)
botao_1 = Button(tela, text='Executar', command=mostrar_nome)


Label_1.grid()
entry.grid()
botao_1.grid()

tela.mainloop()