#Ler um número inteiro e verificar se está compreendido entre 20 e 80. Se tiver, imprimir "parabéns", senão imprimir "chimpanzé".


numero = int(input("Digite um número: "))

if(20 < numero < 80):
    print("Parabéns!")

else:
    print("Chimpanzé.")
