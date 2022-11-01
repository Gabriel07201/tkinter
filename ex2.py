from tkinter import *

tela = Tk()
tela.title('Conversor de temperatura')
tela.geometry("500x300")

def conversor():
    fahrenheit = float(temperatura.get())
    celcius = (fahrenheit - 32) * 5/9
    resultado = Label(tela, text='A temperatura em graus celcius é de ' + str(round(celcius,2)))
    resultado.grid()

label_1 = Label(tela, text='Inserir Fahrenheit')
temperatura = Entry(tela)
botao = Button(tela, text='Converter', command=conversor)

temperatura.focus()

label_1.grid()
temperatura.grid()
botao.grid()

tela.mainloop()