from tkinter import * 

tela = Tk()
tela.title('App')
tela.geometry('500x300')

frame_login = Frame(tela)
frame_endereco = Frame(tela)

label_usuario = Label(frame_login, text='Usuário')
label_senha = Label(frame_login, text='Senha')
text_usuario = Entry(frame_login)
text_senha = Entry(frame_login)

label_rua = Label(frame_endereco, text='Rua:')
label_cidade = Label(frame_endereco, text='Cidade')
text_rua = Entry(frame_endereco)
text_cidade = Entry(frame_endereco)

cmd_entrar = Button(tela, text='Salvar')

# ---------------
# Layout

label_usuario.grid(row=0,column=0)
label_senha.grid(row=1,column=0)
text_senha.grid(row=1, column=1)
text_usuario.grid(row=0, column=1)

label_rua.grid(row=0,column=0)
label_cidade.grid(row=1,column=0)
text_rua.grid(row=1, column=1)
text_cidade.grid(row=0, column=1)

frame_login.grid()
frame_endereco.grid()
cmd_entrar.grid()


tela.mainloop()