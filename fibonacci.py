print("Hello world!")

num = int(input("Digite quantos termos da sequencia de fibonacci deseja mostrar: "))
vet = [0] * num

vet[0] = 1
vet[1] = 1

print(f"|{vet[0]}|\n|{vet[1]}|")

for i in range(2, num):
    vet[i] = vet[i-1] + vet[i-2]
    print(f"|{vet[i]}|")