n=int(input("digite o número a ser fatorado: "))

fatorial=1

for numero in range (1, n+1):
    fatorial=fatorial*numero

print(f"o fatorial de {n} é {fatorial} ")
