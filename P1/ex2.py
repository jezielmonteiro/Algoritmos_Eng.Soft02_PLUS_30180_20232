
total_gasto_abonos = 0
numero_colaboradores = 0
numero_minimo_abono = 0
maior_valor_abono = 0

while True:
    salario = float(input("\nDigite um valor de salário: "))
    if salario == 0:
        break
    
    abono = max(100, 0.2 * salario)

    total_gasto_abonos += abono
    numero_colaboradores += 1

    if abono == 100:
        numero_minimo_abono += 1

    if abono > maior_valor_abono:
        maior_valor_abono = abono

    print(f"\nSalário | Abono\nR$ {salario:.2f} | R$ {abono:.2f}")

print(f"\nForam processados {numero_colaboradores} colaboradores.")
print(f"\nTotal gasto com abonos: R$ {total_gasto_abonos:.2f}.")
print(f"\nValor mínimo pago a {numero_minimo_abono} colaboradores.")
print(f"\nMaior valor de abono pago: R$ {maior_valor_abono:.2f}.")
