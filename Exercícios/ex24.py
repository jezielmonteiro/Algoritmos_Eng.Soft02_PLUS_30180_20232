#Receber um número do teclado e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.



numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print(numero, "é divisível por 10")

if numero % 5 == 0:
    print(numero, "é divisível por 5")

if numero % 2 == 0:
    print(numero, "é divisível por 2")

else:
    print(numero, "não é divisível por 10, 5 ou 2")

