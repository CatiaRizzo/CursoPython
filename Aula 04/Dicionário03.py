#Exercícios dicionários
#Exercécio 01 : Crie uma agenda  de contatos com nome e telefone com a entrada do usuário

"""valor = dicionario['chave'] # Acessando um valor específico
dicionario['nova_chave'] = novo_valor # Adicionando um novo elemento
dicionario['chave_existente'] = novo_valor # Atualizando um valor existente
del dicionario['chave'] # Removendo um elemento específico
dicionario.clear() # Removendo todos os elementos do dicionário
del dicionario # Removendo o dicionário por completo
if 'chave' in dicionario: # Verificando a existência de uma chave # Faça algo
for chave in dicionario:# Percorrendo as chaves do dicionário
valor = dicionario[chave] # Faça algo com a chave e o valor 
for valor in dicionario.values(): # Percorrendo os valores do dicionário# Faça algo com o valor 
for chave, valor in dicionario.items():# Percorrendo os pares chave-valor do dicionário# Faça algo com a chave e o valor"""

"""proj_agenda = {}

def menu():
    print ("===========================")
    print ("Bem vindo aos seus contatos")
    print ("===========================")

    print ("Escolha uma opção: ")
    print ("Opção 1: Adicionar")
    print ("Opção 2: Visualizar")
    print ("Opção 3: Atualizar")
    print ("Opção 4: Excluir")

    opcao = int(input())

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        visualizarr()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        excluir()
    else:
        print("Opção inválida.")

def adicionar(): # Adicionar nome. telefone e email
    nome = input("Digite seu nome:")
    telefone = input("Digite seu telefone:", sep="-") #sep - espaço - separar
    email = input("Digite seu e-mail:")
    contatos[nome]= {"telefone": telefone, "email":email}
    print("Contato adicionado com sucesso!\n")
    
def visualizar(): # Adicionar nome. telefone e email
    if contatos:
        for nome, info in pcontatos.items():
            print( "Nome", proj_agenda["nome"])
            print( "Telefone", info["telefone"])
            print( "E-mail", info["email"])
            print(".............................")
    else:
        print("Contato não encontrado!")

        
def atualizar():
    nome = input("Digite o nome do contato que deseja atualizar: ")
     if nome in contatos:
        telefone = input("digite seu telefone:", sep="-") #sep - espaço - separar
        email = input("digite seu e-mail:")
        contatos[nome]= ["telefone"] = telefone
        contatos[nome]= ["email"] = email
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado!")"""
       



  