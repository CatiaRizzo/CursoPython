"""def saudacao(nome):
    nome = int(input("Digite seu nome: "))
    print("Olá,", nome)


def soma ( ):
    primeiro_numero = int(input("Digite um número: "))
    segundo_numero= int(input("Digite um número: "))

    total = primeiro_numero + segundo_numero

    return total

resultado = soma()

print(resultado)


def soma(a, b):
    resultado = a + b
    return resultado

total = soma(5, 3)

print("A soma total é :", total) # imprime 8


def maior_valor(lista):
    
    print( "O maior valor é : ", max (lista))

maior_valor([1,2,3,4,35,89,102,138,99])"""


numeros = input("Digite uma lista de números separados por espaços: ").split() 
numeros = [int(num) for num in numeros]

def maior_valor():
    maior_valor = max(numeros)
    return maior_valor
    
print( "O maior valor é : ", maior_valor())
