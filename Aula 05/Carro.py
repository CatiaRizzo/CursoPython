#Exercício 4: Crie uma classe chamada `Carro` que tenha os atributos `marca`, `modelo` e `ano`. Crie um método para imprimir as informações do carro.

class Carro:
    def __init__ (carro,marca,modelo,ano):
        carro.marca = marca
        carro.modelo = modelo
        carro.ano = ano
        
    
    def imprimir_nome(carro):
        print("Marca: ",carro.marca)
        print("Modelo: ",carro.modelo)
        print("Ano: ",carro.ano)
        

#Teste do exercício

auto = Carro( "Honda", "I-30",2022)
auto.imprimir_nome()
