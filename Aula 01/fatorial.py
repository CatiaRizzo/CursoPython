#Catia Rizzo
#Curso Python
#Exercício 4: Calcular o fatorial de um número usando um loop "for".

numero =int(input("Digite um número: "))
fatorial = 1

for n in range(1,numero+1):
    fatorial *= n

print(fatorial)

