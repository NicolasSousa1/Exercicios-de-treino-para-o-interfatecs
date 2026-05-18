print("Hello world!")

num = int(input("Digite um numero: "))

primo = True

if num > 1:

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

else:
    primo = False

if primo:
    print(f"{num} é um numero primo")

if primo == False:
    print(f"{num} não é um numero primo")