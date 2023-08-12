from tkinter import *

def verificar_par_impar():
    # Obtenha o número digitado pelo usuário
    numero = int(entrada.get())

    # Verifique se o número é par ou ímpar
    if numero % 2 == 0:
        resultado = "O número é par."
    else:
        resultado = "O número é ímpar."

    # Exiba o resultado na tela
    resultado_texto.set(resultado)

# Crie a janela tkinter
janela = Tk()
janela.title("Verificar Par ou Ímpar")# Defina o título da janela
janela.geometry("400x100+500+200")#largura x altura + distancia margem esquerda + distancia margem topo
janela.config(bg = "yellow")#define a cor do fundo da janela

# Crie uma variável para armazenar o resultado
resultado_texto = StringVar()

# Crie uma label para exibir o resultado
resultado_label = Label(janela, width= 20,textvariable=resultado_texto)
resultado_label.pack()

# Crie uma entrada para o usuário digitar o número
entrada = Entry(janela)
entrada.pack()

# Crie um botão para chamar a função de verificação ao ser clicado
botao = Button(janela, text="Verificar", width= 10,command=verificar_par_impar)
botao.pack()

# Inicie a janela principal
janela.mainloop()