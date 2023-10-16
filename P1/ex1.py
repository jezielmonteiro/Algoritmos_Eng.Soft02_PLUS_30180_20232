
print("\nQual o melhor Sistema Operacional para uso em servidores?")
print("\nAs possíveis respostas são:\n")
print("1 - Windows Server")
print("2 - Unix")
print("3 - Linux")
print("4 - Netware")
print("5 - Mac OS")
print("6 - Outro")

votos = [0, 0, 0, 0, 0, 0]

while True:
    try:
        resposta = int(input("\nDigite a resposta correspondente ao sistema operacional (1 a 6, 0 para encerrar): "))
        if resposta == 0:
            break
        if resposta < 0:
            print("Resposta inválida. Por favor, digite uma resposta válida.")
        if resposta > 6:
            print("Resposta inválida. Por favor, digite uma resposta válida.")
        elif resposta >= 1 and resposta <= 6:
            votos[resposta - 1] += 1
    except ValueError:
        print("Resposta inválida. Por favor, digite uma resposta válida.")

total_votos = sum(votos)

OSs = {
    1: "Windows Server       ",
    2: "Unix                 ",
    3: "Linux                ",
    4: "Netware              ",
    5: "Mac OS               ",
    6: "Outro                "
}

print("\nSistema Operacional      Votos       %  ")
print("---------------------   -------    -----")

for i in range(6):
    nome = OSs[i + 1]
    votos_sistema = votos[i]
    percentual = (votos_sistema / total_votos) * 100
    print(f"{nome}     {votos_sistema}         {percentual:.0f}%")

print("---------------------   -------    -----")
print(f"Total                     {total_votos}")

indice_vencedor = votos.index(max(votos))
vencedor_nome = OSs[indice_vencedor + 1]
vencedor_votos = max(votos)
vencedor_percentual = (vencedor_votos / total_votos) * 100

print(f"\nO Sistema Operacional mais votado foi o {vencedor_nome}, com {vencedor_votos}, correspondendo a {vencedor_percentual:.0f}% dos votos.")












