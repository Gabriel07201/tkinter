from tkinter import *
from tkinter import font

# criando uma tela inical
menu_inicial = Tk() 
# colocando uma nome para essa tela
menu_inicial.title('Tkinter learn')

# colocando centralizado
largura = 700
altura = 400
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
# dimensão e posição da tela quando iniciar
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
# permitindo/negando a alteração das dimensões
menu_inicial.resizable(1,1)

# colocando um valor mínimo para as dimensões
menu_inicial.minsize(700,400)
# colocando um valor máximo para as dimensões
menu_inicial.maxsize(1400,800)

# colocando em tela cheia, nesse caso será o limite que eu defini
menu_inicial.state("normal") # "iconic" inicia ele com a tela no mínimo

# adicionando um ícone
menu_inicial.iconbitmap("imagens/LOGO.ico")

# criando função para o botão
def cmd_click(mensagem):
    print(mensagem)
# botão
btn = Button(menu_inicial, text= "Gravar", command=lambda: cmd_click('Ola mundo!'))
# chamando o botão para a tela
btn.pack()

btn2 = Button(menu_inicial, text= "Tchau", command=lambda: cmd_click('Adeus mundo!'))
btn2.pack()

# adicionando um label
label1 = Label(menu_inicial, 
                text="Label1",
                bg="blue", # background color
                fg="white", # cor da letra
                font= "Times 12",
                width=20 # largura da label
                )
label1.pack()

label2 = Label(menu_inicial, 
                text="frase1\nfrase2",
                font= "Arial 20",
                borderwidth=5,
                relief="solid",
                width=20,
                height=4,
                anchor=SE # posição do texto com base em norte/sul/leste/oeste
                )
label2.pack()

label3 = Label(menu_inicial,
                text="label3\nteste\nsuco de uva",
                font="Times 20",
                bd=3,
                relief="solid",
                padx=50, # padding, bascimente o espaço entre o texto e as bordas
                pady=20,
                justify=LEFT
                )
label3.pack()                
label3['text'] = 'novo texto teste após o pack'


texto = StringVar()
texto.set('Olá mundo!')
label4 = Label(
    menu_inicial,
    textvariable=texto,
    font='Arial 12',
    background='black',
    foreground='white'
)
label4.pack()

texto.set('Papaia')






# abrindo o tela continuamente
menu_inicial.mainloop() 

