######## Sistema controle de faltas ###########
""" Crie um sistema  que calcula a quantidade de faltas nnum curso de 80 horas, sendo que a quantidade permitida é de no máximo 25% do total de horas do curso"""


falta = int (input("Digite a quantidade de faltas : "))

if falta <= (0.25*80) :
    print("Você tem", falta, "faltas. Você está reprovado")
else:
    print("Você tem", falta, "faltas. Você está aprovado")