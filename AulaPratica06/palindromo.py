numeros = []

# Solicita ao usuário que insira 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

# Imprime a lista lida
print("Lista lida:", numeros)

# Calcula a média dos elementos
media = sum(numeros) / len(numeros)

# Encontra o maior e o menor elemento
maior = max(numeros)
menor = min(numeros)

# Conta a quantidade de números maiores que 29
maiores_que_29 = 0
for numero in numeros:
    if numero > 29:
        maiores_que_29 += 1

# Imprime os resultados
print("Média dos elementos:", media)
print("Maior elemento:", maior)
print("Menor elemento:", menor)
print("Quantidade de números maiores que 29:", maiores_que_29)