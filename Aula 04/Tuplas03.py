##Exercício 3: Concatenação de tuplas
##Escreva um programa que declare duas tuplas e crie uma terceira tupla que contenha os elementos das duas tuplas originais.

tupla1 = (1,3,5,7)
tupla2 = (5,89,4,21)
tupla3 = tupla1,tupla2
tupla4 = tupla1+tupla2

print("Traz a tupla em dois grupos separados.",tupla3)
print("Traz a tupla concatenada, em um único grupo.",tupla4)