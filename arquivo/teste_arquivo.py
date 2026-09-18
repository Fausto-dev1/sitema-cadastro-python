pessoas = []

with open("arquivo/pessoas.txt", "r") as arquivo:
    for linha in arquivo:
        pessoas.append(linha.strip())

with open("arquivo/pessoas.txt", "w") as arquivo:
    for nome in pessoas:
        arquivo.write(nome + "\n")

print(pessoas)