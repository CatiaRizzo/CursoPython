from tkinter import *
from tkinter.constants import END


janela = Tk()
janela.title("Formulário de Cadastro")
janela.geometry("500x200+500+200")  
janela.config(bg="#9ffff2")  


lblNumero = Label(janela, text="Número", width=8, font="calibri",bg="#9ffff2")
lblNumero.place(x=100, y=10)
textNumero = Entry(janela, width=19, font="calibri")
textNumero.place(x=200, y=10)

def Verificar():
    numero = int(textNumero.get())
    if numero % 2 == 0:
        resultado = "O número é par."
    else:
        resultado = "O número é ímpar."

    lblResultado["text"] = resultado
    textNumero.delete(0, END)

btnEnviar = Button(janela, text="Verificar", width=25, command=Verificar, font="calibri",bg="pink")
btnEnviar.place(x=150, y=50)


lblResultado = Label(janela, text="Resultado", width=40, font="calibri",bg="#ffff9e")
lblResultado.place(x=100, y=100)

janela.mainloop()


