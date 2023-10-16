#Receber dois números e imprimi-los em ordem crescente. 


numero1 = int(input("Digite um número: "))

numero2 = int(input("Digite um segundo número: "))

if(numero1 > numero2):
    print(numero2)
    print(numero1)

if(numero2 > numero1):
    print(numero1)
    print(numero2)
