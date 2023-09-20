#Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e menor valore informados pelo usuário.



maior_valor = float("-inf")  
menor_valor = float("inf")   

while True:
    try:
        valor = int(input("Digite um valor positivo inteiro (ou negativo para sair): "))
        if valor < 0:
            break  
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro válido.")

if maior_valor != float("-inf") and menor_valor != float("inf"):
    print(f"O maior valor informado foi: {maior_valor}")
    print(f"O menor valor informado foi: {menor_valor}")
else:
    print("Nenhum valor positivo foi informado.")
