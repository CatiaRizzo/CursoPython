##Exercício 4: Verificação de existência
##Escreva um programa que declare uma tupla e verifique se um elemento específico está presente nela.

tupla = (45,22,78,0,2,5,9,78)
num = int(input( "digite um número: "))

def verificar_elemento(tupla, num):
    if num in tupla:
        print( " O elemneto: ",num," aparece dentro da tupla.")
    else:
        print(" O elemneto: ",num," não aparece dentro da tupla")
    
verificar_elemento(tupla,num)



