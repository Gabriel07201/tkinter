from tkinter import *

tela = Tk()

def apresentar():
    print(valor_check.get())

valor_check = BooleanVar()
check = Checkbutton(
    tela,
    text= "Checkbox",
    variable=valor_check,
    command=apresentar
)
check.pack()



tela.mainloop()