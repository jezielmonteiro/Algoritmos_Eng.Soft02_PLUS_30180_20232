
print("\nComparativo de Consumo de Combustível")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print("\nModelo 1")
print("--------")
print("\nCarro: Fusca")
print("Km por Litro: 8")

print("\nModelo 2")
print("--------")
print("\nCarro: Gol")
print("Km por Litro: 10")

print("\nModelo 3")
print("--------")
print("\nCarro: Uno")
print("Km por Litro: 20")

print("\nModelo 4")
print("--------")
print("\nCarro: Vectra")
print("Km por Litro: 10")

print("\nModelo 5")
print("--------")
print("\nCarro: Peugeot")
print("Km por Litro: 16")

print("\nRelatório Final")
print("===============")

fusca_litros = float(1000 / 8)
fusca_custo = float(fusca_litros * 2.25)

gol_litros = float(1000 / 10)
gol_custo = float(gol_litros * 2.25)

uno_litros = float(1000 / 20)
uno_custo = float(uno_litros * 2.25)

vectra_litros = float(1000 / 10)
vectra_custo = float(vectra_litros * 2.25)

peugeot_litros = float(1000 / 16)
peugeot_custo = float(peugeot_litros * 2.25)

print(f"\n1 - Fusca | 8 | {fusca_litros} litros | R${fusca_custo}")
print(f"2 - Gol | 10 | {gol_litros} litros | R${gol_custo}")
print(f"3 - Uno | 20 | {uno_litros} litros | R${uno_custo}")
print(f"4 - Vectra | 10 | {vectra_litros} litros | R${vectra_custo}")
print(f"5 - Peugeot | 16 | {peugeot_litros} litros | R${peugeot_custo}")

print("\nO menor consumo é do Uno.")

