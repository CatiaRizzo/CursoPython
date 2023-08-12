#Subconjunto

conjunto1 = {1,2,3,4,5,6}
conjunto2 = {1,2,3}

subconjunto =  conjunto2.issubset(conjunto1)

print(subconjunto)

#Inprime os numeros maiores que 2
conjunto = {1, 2, 3, 4, 5}
subconjunto = {x for x in conjunto if x > 2}
print(subconjunto)

# exercíco 4 
lista1 = {"Marcelo","CPF:123456789","-"}
lista2 = {"Fernando","CPF: 198732154"}
uniao = lista1.union(lista2)
print(uniao)
