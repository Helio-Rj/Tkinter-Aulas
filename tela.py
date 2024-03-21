from tkinter import *


root = Tk()


class Aplication:
    def __init__(self):
        self.root = root  # Equivalência
        self.tela()  # toda a função "tela()"
        self.frames_tela()  # Chamada da função "frames_tela()"
        root.mainloop()  # loop

    def tela(self):
        self.root.title("Coloque seu Título aqui ")  # definição do texto título
        self.root.config(bg="white")  # configuração de cores fundo
        self.root.geometry("800x500")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True)  # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=950, height=650)  # Máximo tamanho permitido.
        self.root.minsize(width=550, height=350)  # Minimo tamanho permitido.

    def frames_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#ffff00', highlightbackground='#1a0080',
                             highlightthickness=3)  # fina borda
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96,
                           relheight=0.96)  # método para enquadramento de janela (Relative) por cordenadas


Aplication()
