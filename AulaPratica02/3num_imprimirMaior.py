num1=int(input("Digite o primeiro número inteiro:"))
num2=int(input("Digite o segundo número inteiro: "))
num3=int(input("Digite o terceiro número inteiro: "))
maior=0
if (num1>num2):
    maior=num1
else:
    maior=num2
if(num3>maior):
    maior=num3

print(f"o maior número entre eles é {maior}")


