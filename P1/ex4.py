

anotacoes = [0, 0, 0, 0]

while True:
    try:
        situacao = int(input("\nDigite a situação do mouse(1 a 4, 0 para encerrar): "))
        if situacao == 0:
            break
        if situacao < 0:
            print("Situação inválida. Por favor, digite uma situação válida.")
        if situacao > 4:
            print("Situação inválida. Por favor, digite uma situação válida.")
        elif situacao >= 1 and situacao <= 4:
            anotacoes[situacao - 1] += 1
    except ValueError:
        print("Situação inválida. Por favor, digite uma situação válida.")

total_estados = sum(anotacoes)

estados = {
    1: "1 - Esfera                        ",
    2: "2 - Limpeza                       ",
    3: "3 - Troca do cabo ou conector     ",
    4: "4 - Quebrado ou inutilizado       "
}

print(f"\nQuantidade de mouse: {total_estados}\n")
print("Situação                              Quantidade   Percentual")

for i in range(4):
    nome = estados[i + 1]
    levantamento = anotacoes[i]
    percentual = (levantamento / total_estados) * 100
    print(f"{nome}         {levantamento}           {percentual:.0f}%")



indice = anotacoes.index(max(anotacoes))
situacao_nome = estados[indice + 1]
situacao_anotacoes = max(anotacoes)
situacao_percentual = (situacao_anotacoes / total_estados) * 100












