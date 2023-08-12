#Catia rizzo
#Curso Python
#Exercícios Eleitor

idade = int (input("Digite sua idade : "))

if idade < 16 :
    print("Você tem", idade, "anos. Você não pode votar")
elif (idade >= 16 and idade < 18):
    print("Você tem", idade, "anos. O voto é opcional, mas não é obrigatório")
elif (idade > 69):
    print("Você tem", idade, "anos. O voto é opcional, mas não é obrigatório")
else:
    print("Você tem", idade, "anos.O voto é obrigatório")