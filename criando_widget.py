from tkinter import *

# ---------------------------------------------
# Widget
class FrameNome(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['border'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text='Nome:')
        text_nome = Entry(self)

        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)

# ---------------------------------------------
# GUI

tela = Tk()
tela.title('App')

frame_1 = FrameNome(tela).grid()


tela.mainloop()

