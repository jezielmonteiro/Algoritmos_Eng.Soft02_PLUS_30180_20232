
def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def uso_percentual(espaco, total):
    return (espaco / total) * 100

usuarios = []
espaco_total = 0

with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        partes = linha.split()
        usuario = partes[0]
        espaco = int(partes[1])
        usuarios.append((usuario, espaco))
        espaco_total += espaco

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc.\tUso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 60 + "\n")
    relatorio.write("Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n")

    for i, (usuario, espaco) in enumerate(usuarios, start=1):
        espaco_em_mb = bytes_para_mb(espaco)
        percentual = uso_percentual(espaco, espaco_total)
        relatorio.write(f"{i}\t{usuario}\t{bytes_para_mb(espaco):.2f}MB\t\t{percentual:.2f}%\n")

    espaco_total_mb = bytes_para_mb(espaco_total)
    espaco_medio_mb = espaco_total_mb / len(usuarios)
    relatorio.write(f"\nEspaço total ocupado: {bytes_para_mb(espaco_total):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {bytes_para_mb(espaco_total / len(usuarios)):.2f} MB\n")

print("Relatório gerado com sucesso!")
