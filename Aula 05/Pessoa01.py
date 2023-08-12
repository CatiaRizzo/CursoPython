"""Classe Pessoa:
def_init_(forma_pessoa_tem, nome, idade)
	Pessoa.nome = nome
	Pesso.idade = idade
	def função_pessoa( parâmetro :
		print( “ Olá mundo + parâmetro.nome )
Criando um objeto da classe:
	Pessoa1 = Pessoa (“João, 17 )
	Pessoa1.funcao_pessoa () ##chamando o método
   objeto = MinhaClasse(valor1, valor2)"""

#Exercício 1: Crie uma classe chamada `Pessoa` que tenha o atributo `nome`. Crie um método para imprimir o nome.


class Cliente:
    def __init__ (cliente,nome,idade,email,endereco):
        cliente.nome = nome
        cliente.idade = idade
        cliente.email = email
        cliente.endereco = endereco
    
    def imprimir_nome(cliente):
        print("Nome: ",cliente.nome)
        print("Idade: ",cliente.idade)
        print("E-mail: ",cliente.email)
        print("Endereço: ",cliente.endereco)

#Teste do exercício

cliente_01 = Cliente("Cássio", 38, 'cassio.matematia@gmail.com','Alto da Mooca')
cliente_01.imprimir_nome()


