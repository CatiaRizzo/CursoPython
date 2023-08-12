#Calcule a área de uma quadrado, retangulo e um triangulo

def area_quadrado(lado):
    print("A área do quadrado ", lado, "é ", lado * lado)
   

def permietro_quadrado(lado):
    print("O perímetro do quadrado ", lado, "é ", lado * 4)

def cal_perimetro_quadrado():
    lado = int(input("digite o lado do quadrado: "))
    print("O perímetro do quadrado é ", lado * 4)

def area_retangulo(comprimento, largura):
     print("A área do retângulo é: ", comprimento * largura)

def permitero_retangulo(comprimento, largura):
    print("O perímetro do retângulo é: ", comprimento + largura + comprimento + largura)

def area_triangulo(base, altura):
     print("A área do triângulo é: ", (base * altura)/2)

def perimetro_triangulo(lado1 ,lado2 ,lado3):
    print("O perímetro do triângulo é: ", lado1 + lado2 + lado3)


     
    
