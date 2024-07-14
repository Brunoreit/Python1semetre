primo = 0 ; n_primo = 0 ; count = 0
num = int(input("Digite um número inteiro e positivo: "))

for n in range(1, num+1):

    if num % n == 0:
        count += 1

if count == 2:   
    primo = num

if primo:
    print(f"O número digitado é primo")

else:
    print("O número digitado não é primo")