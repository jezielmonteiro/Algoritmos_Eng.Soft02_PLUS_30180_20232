#Solicitar a idade de várias pessoas e imprimir: Total de pessoas com menos de 21 anos. Total de pessoas com mais de 50 anos. 
#O programa termina quando idade for = 99.

p21 = 0
p50 = 0

while True:
    idade = int(input("Informe sua idade: "))
    if (idade < 21):
        p21 += 1
    elif (99 > idade > 50):
        p50 += 1 
    if (idade == 99):
        break

print(f"Total de pessoas com menos de 21 anos: {p21}")
print(f"Total de pessoas com mais de 50 anos: {p50}")