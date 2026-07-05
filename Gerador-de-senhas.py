# Importar das bibliotecas
from tkinter import *
import secrets

# Paleta de cores do sistema
cor1 = '#0d1117'
cor2 = '#161b22'
cor3 = '#238636'
cor4 = '#2ea043'

# Configuração da janela principal
janela = Tk()
janela.title('Gerador de Senhas')
janela.resizable(False, False)
janela.geometry('300x150')

# Frame pricipal da aplicação
frame_corpo = Frame(janela, width=300, height=100, bg=cor1)
frame_corpo.grid(row=1, column=0)

# Área de exibição de senha
frame_tela = Frame(janela, width=300, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

# Banco de caracteres ultilizado na geração das senhas
banco = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789@#$&?!£¢€¥%"

# Variável para guardar a senha gerada
senha = ""

# Função responsável por gerar uma senha aleatória
def gerar():
    senha = " "
    for i in range(8):
        a = secrets.choice(banco)
        senha = (senha + str(a))
    label.config(text=senha)

# Exibe senha gerada no visor
label = Label(frame_tela, text="Clique em Gerar", fg="white", width=24, height=2, padx=7, bg=cor4, font=('Ivy 13'))
label.place(x=20, y=10)

# Criação do botão de gerar senha
b1 = Button(frame_corpo, command = gerar, text='Gerar', width=7, height=1, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=100, y=30)

# Iniciaa loop principal da aplicação
janela.mainloop()
