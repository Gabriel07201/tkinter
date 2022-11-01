from this import s
from tkinter import *


menu_inicial = Tk()
menu_inicial.title('Grid')

largura = 700
altura = 400
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


# usando o grid
label5 = Label(
    menu_inicial,
    text='label5',
    font= 'Arial 12',
    bg= 'green',
    width=20
)
label6 = Label(
    menu_inicial,
    text='label6',
    font='Arial 12',
    bg='red',
    width=20
)
label7 = Label(
    menu_inicial,
    text='label7',
    font='Arial 12',
    bg='blue',
    width=20
)

label5.grid(row=0, column=0)
label6.grid(row=1, column=1)
label7.grid(row=2, column=2)

btn1= Button(menu_inicial, text='btn1')
btn2= Button(menu_inicial, text='btn2')
btn3= Button(menu_inicial, text='btn3')

btn1.grid(row=0, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=2, column=3)

# criando um label que ocupa mais de uma coluna
label = Label(
    menu_inicial,
    background='yellow',
    width=40
)
label.grid(row=3, columnspan=2, sticky='we')

menu_inicial.mainloop()
