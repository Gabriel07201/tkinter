from tkinter import *

tela = Tk()
tela.title('Login')

usuario = Label(
    tela,
    text="Usuário:"
)
usuario.grid(row=0,column=0, sticky=W)
senha = Label(
    tela,
    text="Senha:"
)
senha.grid(row=1,column=0, sticky=W)


box_usuario = Entry(tela)
box_usuario.grid(row=0,column=1)
box_senha = Entry(tela)
box_senha.grid(row=1,column=1)

login = Button(tela, text="Login")
login.grid(row=2,column=1,sticky=E)

tela.mainloop()