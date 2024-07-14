idade_superior50 = 0 
idade10_20 = 0 
pessoas10_20 = 0
inferior_50kg = 0

for p in range(1,3):

    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    peso = int(input("Digite seu peso: "))

    if idade > 50:    
        idade_superior50 += 1

    elif 10 <= idade <= 20:
        idade10_20 += altura
        pessoas10_20 += 1

    if peso < 50:
        inferior_50kg += 1

if pessoas10_20 > 0:
    media10_20 = (idade10_20 / pessoas10_20)
else:
    media10_20 = 0
perc_pessoas_menor50 = (inferior_50kg / 25)*100

print("-----RESULTADOS-----")
print(f"A quantidade de pessoas com idade superior a 50 é: {idade_superior50}")
print(f"A média das alturas das pessoas com a idade entre 10 e 20 anos é: {media10_20}")
print(f"O percentual de pessoas com peso inferior a 50 quilos é: {perc_pessoas_menor50}")