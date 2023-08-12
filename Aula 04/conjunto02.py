#Valores da mega sena

num_mega = {6,17,23,38,51,53}
num_loto = {1,2,4,5,7,9,15,17,20,22,23,38,51,53,}

uniao = num_mega.union(num_loto)
print(uniao)
interseccao = num_mega.intersection(num_loto)
print(interseccao)
diferenca = num_mega.difference(num_loto)
print(diferenca)