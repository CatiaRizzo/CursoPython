
agenda = {}  # Cria um dicionário vazio para a agenda telefônica

def adicionar_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda[nome] = contato
    print("Contato adicionado com sucesso!")

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")

def exibir_contatos():
    if len(agenda) > 0:
        print("Agenda Telefônica:")
        for contato in agenda.values():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Agenda Telefônica vazia.")

# Exemplo de uso:
"""adicionar_contato("João", "123456789", "joao@email.com")
adicionar_contato("Maria", "987654321", "maria@email.com")
exibir_contatos()

remover_contato("João")
exibir_contatos()"""
