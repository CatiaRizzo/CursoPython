#Exercício 2:Crie uma classe chamada `Cachorro` que tenha os atributos `nome` e `idade`. Crie um método para imprimir o nome e a idade do cachorro.

class Cachorro:
    def __init__ (cachorro,nome,idade):
        cachorro.nome = nome
        cachorro.idade = idade
        
    
    def imprimir_nome(cachorro):
        print("Nome: ",cachorro.nome)
        print("Idade: ",cachorro.idade)
        

#Teste do exercício

animal = Cachorro("Yugui", 15)
animal.imprimir_nome()
