from tkinter import *

root = Tk()


class Aplication:
    def __init__(self):
        self.root = root  # Equivalência
        self.tela()  # toda a função "tela()"
        self.frames_tela()  # Chamada da função "frames_tela()"
        self.widiget_frame()  # Função dos botões.
        root.mainloop()  # loop

    def tela(self):
        self.root.title("Coloque seu Título aqui ")  # definição do texto título
        self.root.config(bg="white")  # configuração de cores fundo
        self.root.geometry("500x200")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True)  # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=650, height=650)  # Máximo tamanho permitido.
        self.root.minsize(width=250, height=350)  # Minimo tamanho permitido.

    def frames_tela(self):
        self.frame = Frame(self.root, bd=4, bg='#ffff00', highlightbackground='#1a0080',
                           highlightthickness=3)  # fina borda
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96,
                         relheight=0.96)  # método para enquadramento de janela (Relative) por cordenadas

    def widiget_frame(self):
        # Botão buscar
        self.btn_buscar = Button(self.frame, text='Buscar', bd=2, bg="#4169E1", fg="#ffffff",
                                 font=('verdana', 8, 'bold'),
                                 )  # Esse botão fica dentro do frame 1
        self.btn_buscar.place(relx=0.60, rely=0.30, relwidth=0.12, relheight=0.07)  # Posicionamento do botão limpar


Aplication()