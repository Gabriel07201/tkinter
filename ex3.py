from tkinter import *


class MeuFrame(Frame):
    def __init__(self, parente):
        super().__init__()

        self.text1_text = StringVar()
        self.label1_text = StringVar()

        # widget
        self.label = Label(self, textvariable=self.label1_text)
        self.label.grid()
        self.text = Entry(self, textvariable=self.text1_text)
        self.text.grid()
        cmd1 = Button(self, text='Clique', command=self.Executar)
        cmd1.grid()

    def Executar(self):
        self.label1_text.set(f'Olá {self.text1_text.get()}.')


tela = Tk()
tela.geometry("400x200")

frm1 = MeuFrame(tela)
frm1.grid()

tela.mainloop()