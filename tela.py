from tkinter import *


root = Tk()


class Aplication:
    def __init__(self):
        self.entry = None
        self.lb_text = None
        self.btn_go = None
        self.frame = None
        self.root = root  # Equivalência
        self.tela()  # toda a função "tela()"
        self.menus()  # Barra de menus
        self.frames_tela()  # Chamada da função "frames_tela()"
        self.widiget_frame()  # Função dos botões.
        root.mainloop()  # loop

    def tela(self):
        self.root.title("Coloque seu Título aqui ")  # definição do texto título
        self.root.config(bg="white")  # configuração de cores fundo
        self.root.geometry("400x200")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True)  # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=650, height=650)  # Máximo tamanho permitido.
        self.root.minsize(width=250, height=350)  # Minimo tamanho permitido.

    # Frame
    def frames_tela(self):
        self.frame = Frame(self.root, bd=4, bg='#ffff00', highlightbackground='#1a0080',
                           highlightthickness=3)  # fina borda
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96,
                         relheight=0.96)  # método para enquadramento de janela (Relative) por cordenadas

    # Widgets
    def widiget_frame(self):
        # Botão GO
        self.btn_go = Button(self.frame, text='GO', bd=2, bg="#4169E1", command=self.mensagem, fg="#ffffff",
                             font=('verdana', 8, 'bold'),
                             )  # Esse botão fica dentro do frame 1
        self.btn_go.place(relx=0.05, rely=0.20, relwidth=0.12, relheight=0.07)  # Posicionamento do botão limpar

        # Label
        self.lb_text = Label(self.frame, text="Clique no botão ", bg="#ffff00", fg="#4169E1",
                             font=('verdana', 9, 'bold'))
        self.lb_text.place(relx=0.05, rely=0.10)

        # Entry
        self.entry = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                           font=('verdana', 8, 'bold'))  # codigo equivalente ao o "input"
        self.entry.place(relx=0.20, rely=0.20, relwidth=0.70, relheight=0.07)

    # Barra de Menus
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        # Variável para quitar
        def sair(): self.root.destroy()

        menubar.add_cascade(label="Sobre", menu=filemenu2)
        menubar.add_cascade(label="Sair", menu=filemenu)

        filemenu.add_command(label="Sair", command=sair)
        filemenu2.add_command(label="Desenvolvido Pela Puritoka Zaybatsu Inc.")

    # Mensagem da Entry
    def mensagem(self):
        self.entry.insert(END, 'Seu App está funcionado corretamente ')


Aplication()
# Executar o comando "pyinstaller --onefile --noconsole --windowed tela.py" para fazer o Deploy
