# Exercício 10:Crie uma classe chamada `Funcionario` que tenha os atributos `nome` e `salario`. Crie métodos para aumentar o salário em uma determinada porcentagem e para imprimir o nome e o salário do funcionário.

class Funcionario:
    def __init__ (funcionario,nome,salario):
        funcionario.nome = nome
        funcionario.salario = salario

    def aumento(funcionario):
        percentual = int(input("Digite o percentual para aumentar o salário: "))
        novo_Salario = funcionario.salario * percentual/100
        funcionario.salario += novo_Salario  #saldo = saldo + valor
    
    def imprimir_salario(funcionario):
        print("Nome: ",funcionario.nome)
        print("Salário: ",funcionario.salario)
        

#Teste do exercício

func = Funcionario("Arlindo",2000)
func.aumento()
func.imprimir_salario()