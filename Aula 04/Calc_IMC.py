#Calculadora de IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

print("==================")
print("Calculadora de IMC")
print("==================\n")

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcular_imc(peso, altura)
interpretação = interpretar_imc(imc)

print("Seu IMC é:", imc)
print("Classificação:", interpretação)