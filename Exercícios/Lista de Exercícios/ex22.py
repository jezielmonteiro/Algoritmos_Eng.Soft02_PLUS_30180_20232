#Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final o total do somatório, a média e o total de valores lidos.


soma = 0

valores = 0


while True:
    try:
        valor = float(input("Digite um valor (ou digite 0 para sair): "))
        if valor < 0:
            break  
        soma += valor
        valores += 1
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")

if valores > 0:
    media = soma / valores
    print(f"Total de valores lidos: {valores}")
    print(f"Somatório dos valores: {soma}")
    print(f"Média dos valores: {media}")
else:
    print("Nenhum valor foi lido.")
