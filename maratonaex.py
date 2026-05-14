print("Hello world!")

i= 0
n = int(input("Digite a quantidade de alunos: "))
nomes = [""] * n
anos = [""] * n
letras = [0] * n
iniciais = [""] * n

while i < n:
    inicial = str(input("Digite o nome do aluno e seu ano de ingresso: Ex(Neymar Junior|2026)").strip()) #recebe o nome e o ano

    separador = inicial.split("|") #separa o nome e o ano em duas variaveis
    nomes[i] = separador[0] # recebe apenas o nome
    anos[i] = separador[1] # recebe apenas o ano

    letras[i] = len(nomes[i].replace(" ", "")) # conta a quantidade de letras no nome

    NomeSeparado = nomes[i].split() #separa cada nome da pessoa

    for palavra in NomeSeparado: # para cada palavra em NomeSeparado adicionar a inical da palavra
        iniciais[i] += palavra[0]
    
    i += 1

i = 0

while i < n:
    print(f"{nomes[i]} - {anos[i]}{iniciais[i].upper()}{letras[i]}")
    i+= 1