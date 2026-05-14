n = int(input("Digite a quantidade de alunos: "))

i = 0
nomes = [""] * n
qtde = [0] * n
UltimasLetras = [""] * n
TotaLetras = [0] * n
ni = 0


while i < n:

    nomes[i] = str(input("Digite seu Nome completo: ").strip())

    NomeSeparados = nomes[i].split() # separando os nomes e sobrenomes
    
    for nome in NomeSeparados:
        qtde[i] += 1 # calcula a quantidade de palavras

    UltimasLetras[i] = ""
    for item in NomeSeparados:
        UltimasLetras[i] += item[-1].upper()

    TotaLetras[i] = len(nomes[i].replace(" ", "")) # contando a quantidade de letras

    i+= 1

i = 0

while i < n:
    print(f"{nomes[i]} - {qtde[i]}{UltimasLetras[i]}{TotaLetras[i]}")
    i += 1