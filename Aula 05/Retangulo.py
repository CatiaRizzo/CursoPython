# Exercício 6: Crie uma classe chamada `Retangulo` que tenha os atributos `largura` e `altura`. Crie métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__ (retangulo,largura,altura):
        retangulo.largura = largura
        retangulo.altura = altura
        
    
    def imprimir_nome(retangulo):
        print("A área do retângulo é : ",retangulo.largura * retangulo.altura)
        

#Teste do exercício

area = Retangulo(6,18)
area.imprimir_nome()