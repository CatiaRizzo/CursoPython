lista_frutas = ["maçã", "banana", "laranja", "pitaya", "morango", "uva", "limão"]
lista_frutas.sort() #Ordena a lista em ordem alfabética

elemento_3 = lista_frutas[2]
print(elemento_3) #printa o elemento na posição 3

lista_frutas[0] = "jaca"
print(lista_frutas) #printa o elemento na posição 0 e troca por jaca

lista_frutas.append("carambola")
print(lista_frutas) #adiciona o elemento carambola

lista_frutas.insert(2,"nova fruta")
print(lista_frutas) #insere a palavra nova fruta na posição 3

for fruta in lista_frutas:
    print( "Fruta: ",fruta) #insere a palavra Fruta: na frente de cada fruta da lista

"""for fruta in lista_frutas:
    fruta == "maçã":
    print( "Fruta: ",fruta) #printa a fruta selecionada (maçã)"""









