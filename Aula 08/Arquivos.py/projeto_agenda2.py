from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()
root.title("Agenda de Contatos")
contatos = []

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    apelido = entry_apelido.get()

    contatos.append({"Nome": nome, "Telefone": telefone, "Email": email, "Apelido": apelido})

    messagebox.showinfo("Contato adicionado", "O contato foi adicionado com sucesso!")

def listar_contatos():
    lista.delete(0, END)
    for contato in contatos:
        lista.insert(END, contato["Email"])

def deletar_contato():
    email_selecionado = lista.get(ACTIVE)
    for contato in contatos:
        if contato["Email"] == email_selecionado:
            contatos.remove(contato)
            break

    messagebox.showinfo("Contato deletado", "O contato foi deletado com sucesso!")

    listar_contatos()

label_nome = Label(root, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = Entry(root)
entry_nome.grid(row=0, column=1)

label_telefone = Label(root, text="Telefone:")
label_telefone.grid(row=1, column=0)
entry_telefone = Entry(root)
entry_telefone.grid(row=1, column=1)

label_email = Label(root, text="Email:")
label_email.grid(row=2, column=0)
entry_email = Entry(root)
entry_email.grid(row=2, column=1)

label_apelido = Label(root, text="Apelido:")
label_apelido.grid(row=3, column=0)
entry_apelido = Entry(root)
entry_apelido.grid(row=3, column=1)

button_adicionar = Button(root, text="Adicionar", command=adicionar_contato)
button_adicionar.grid(row=4, column=0)

button_deletar = Button(root, text="Deletar", command=deletar_contato)
button_deletar.grid(row=4, column=1)

lista = Listbox(root)
lista.grid(row=5, columnspan=2)

root.mainloop()