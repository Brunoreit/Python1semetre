num = int(input("Digite a quantidade de números a serem lidos: "))
soma7=0

for numero in range (1,num+1):
    if numero%7 == 0:
        soma7+=numero

print(f"a soma dos multiplos de 7 foi: {soma7}")