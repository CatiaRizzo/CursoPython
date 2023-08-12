# Exercício 8: Crie uma classe chamada `Aluno` que tenha os atributos `nome` e `notas` (uma lista de notas). Crie um método para calcular a média das notas.

class Aluno:
    def __init__(aluno, nome):
        aluno.nome = nome
        aluno.notas = []

    def adicionar_nota(aluno, nota):
        aluno.notas.append(nota)

    def calcular_media(aluno):
        if len(aluno.notas) == 0:
            return 0
        total = sum(aluno.notas)
        return total / len(aluno.notas)

    def mostrar_notas(aluno):
        print("Notas do aluno", aluno.nome)
        for nota in aluno.notas:
            print("A nota do bimestre é: ",nota)

    
aluno1 = Aluno("João")
aluno1.adicionar_nota(6.5)
aluno1.adicionar_nota(9.0)
aluno1.adicionar_nota(5.5)
aluno1.mostrar_notas()
print("A Média anual do aluno é :", aluno1.calcular_media())        