# Exercício 7: Crie uma classe chamada `Círculo` que tenha o atributo `raio`. Crie métodos para calcular a área e a circunferência do círculo.

class Circulo:
    def __init__ (circulo,raio):
        circulo.raio = raio
        circulo.pi = 3.14159
        
    
    def imprimir_nome(circulo):
        print("A circunfêrenia do circulo é : ",2 * circulo.raio * circulo.pi)
        

#Teste do exercício

circunferencia = Circulo(18)
circunferencia.imprimir_nome()