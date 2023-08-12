"""for numero in range(11):
   print(numero) #imprime até o numero 10, sempre colocar uma posição a mais.
    
for numero in range(0,11):
    print(numero) #começa com zero e termina com 10

for numero in range(0,11,2): 
    print(numero) #imprime no range de 0 a 10 de dois em dois

for numero in range(0,11,2): 
    if numero % 3 == 0:
        print(numero)


##Escreva um programa que recebe uma lista de números do usuário e retorna a soma de todos os números.

numeros = input("Digite uma lista de números separados por espaços: ").split() # split trasnforma os numeros em uma lista de strings, separardo por aspas e virgulas
numeros = [int(num) for num in numeros] # o int transforma a lista (strings) em números inteiros
soma= sum(numeros)
print("A soma dos números é: ", soma)
#print(numeros)


#Escreva um programa que recebe uma lista de números do usuário que some um número com o outro. 

numeros = input("Digite uma lista de números separados por espaços: ").split() # split trasnforma os numeros em uma lista de strings, separardo por aspas e virgulas
numeros = [int(num) for num in numeros] # o int transforma a lista (strings) em números inteiros
soma = 0
for elemento in numeros: #soma os numeros um com o outro
    soma += elemento # ou soma += elemento

print("A soma dos números é: ", soma)


##Escreva um programa que recebe uma lista de números do usuário e retorna o maior valor da lista

numeros = input("Digite uma lista de números separados por espaços: ").split() # split trasnforma os numeros em uma lista de strings, separardo por aspas e virgulas#
maior = (max(int(num) for num in numeros))
print("O maior número da lista é: ", maior)


##Escreva um programa que recebe uma lista de números do usuário e retorna os numeros pares na lista
numeros = input("Digite uma lista de números separados por espaços: ").split() #
numeros = [int(num) for num in numeros] 
for i in numeros: #percorrer os números digitados pelo ususário
    if (i % 2) == 0: #se o resto da divisão por 2 for igual a zero, printar o número
        print (i)"""

##Escreva um programa que recebe uma lista de números do usuário e retorna a contagem de numeros pares na lista
numeros = input("Digite uma lista de números separados por espaços: ").split() #
numeros = [int(num) for num in numeros] 
contagem = 0 
for i in numeros: #percorrer os números digitados pelo ususário
    if (i % 2) == 0:
        contagem += 1
print ("A contagem de números pares é: ", contagem)