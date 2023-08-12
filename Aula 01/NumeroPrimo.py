#Catia Rizzo
#Curso Python
#Exercício 8: Verificar se um número é primo usando um loop "for".

for i in range(2,30):
    numero = 2
    numero2 = 0
    while numero < i:
        if i % numero == 0:
            numero2 = 1
            numero = numero + 1
        else:
            numero = numero + 1

    if numero2 == 0:
        print(str(i) + " é um número primo")
        numero2 = 0
    else:
        numero2 = 0 