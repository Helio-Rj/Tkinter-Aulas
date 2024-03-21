from tkinter import *


root = Tk()


class Aplication:
    def __init__(self):
        self.root = root  # Equivalência
        self.tela()  # toda a função "tela()"
        root.mainloop()  # loop

    def tela(self):
        self.root.title("Coloque seu Título aqui ")  # definição do texto título
        self.root.config(bg="white")  # configuração de cores fundo
        self.root.geometry("800x500")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True)  # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=950, height=650)  # Máximo tamanho permitido.
        self.root.minsize(width=550, height=350)  # Minimo tamanho permitido.


Aplication()
