# Exercício 9: Crie uma classe chamada `Livro` que tenha os atributos `titulo`, `autor` e `ano`. Crie um método para imprimir as informações do livro.

class Livro:
    def __init__ (livro,titulo,autor,ano):
        livro.nome = titulo
        livro.autor = autor
        livro.ano = ano
    
    
    def imprimir_nome(livro):
        print("Título do livro: ",livro.nome)
        print("Autor: ",livro.autor)
        print("Ano: ",livro.ano)
        

#Teste do exercício

estante = Livro("Poeira em auto mar", "Leandro dos Reis", 2002)
estante.imprimir_nome()