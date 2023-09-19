#Entrar com um número e imprimir a raiz quadrada do número, caso ele seja positivo. E o quadrado dele caso seja negativo.


numero = int(input("Digite um número: "))

if(numero > 0):
    print(numero ** (1 / 2))

if(numero < 0):
    print(numero ** 2)
