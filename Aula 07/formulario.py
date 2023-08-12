from tkinter import *
from tkinter.constants import END


janela = Tk()
janela.title("Formulário de Cadastro")
janela.geometry("500x500+500+200")#largura x altura + distancia margem esquerda + distancia margem topo
janela.config(bg = "red")#define a cor do fundo da janela

#labels - rotulos ou etiquetas
lblNome = Label(janela, text="Nome", width= 8, font="calibri")
lblNome.place(x=100,y=100)
textNome = Entry(janela, text="",width= 20,font="calibri")
textNome.place(x=200,y=100)

lblCpf = Label(janela, text="CPF", width= 8, font="calibri")
lblCpf.place(x=100,y=150)
textCpf = Entry(janela, text="",width= 20,font="calibri")
textCpf.place(x=200,y=150)

lblEmail = Label(janela, text="E-mail", width= 8, font="calibri")
lblEmail.place(x=100,y=200)
textEmail = Entry(janela, text="",width= 20,font="calibri")
textEmail.place(x=200,y=200)

lblFone = Label(janela, text="Telefone", width = 8, font="calibri")
lblFone.place(x=100,y=250)
textFone = Entry(janela, text="",width= 20,font="calibri")
textFone.place(x=200,y=250)

#Função botão enviar
def Enviar():
    lblResultado["text"]="Dados Enviados com Sucesso!"
    textNome.delete(0,END)
    textCpf.delete(0,END)
    textEmail.delete(0,END)
    textFone.delete(0,END)

def Inserir():
    lblResultado["text"]="Dados Inseridos com Sucesso!"
    textNome.delete(0,END)
    textCpf.delete(0,END)
    textEmail.delete(0,END)
    textFone.delete(0,END)    

def Deletar():
    lblResultado["text"]="Dados Deeltados com Sucesso!"
    textNome.delete(0,END)
    textCpf.delete(0,END)
    textEmail.delete(0,END)
    textFone.delete(0,END) 

#Botões
btnEnviar = Button(janela, text= "Enviar", width= 10, command= Enviar,font="calibri")
btnEnviar.place(x=120,y=310)

btnInserir = Button(janela, text= "Deletar", width= 10, command= Inserir,font="calibri")
btnInserir.place(x=220,y=310)

btnDeletar = Button(janela, text= "Listar", width= 10, command= Deletar,font="calibri")
btnDeletar.place(x=320,y=310)



#label para exibir o resultado
lblResultado = Label(janela, text="Resultado", width= 40, font="calibri")
lblResultado.place(x=100,y=370)





janela.mainloop()

