string = input("digite sua string: ")
count = 0
countA= 0
for letra in string:

    if letra == "!":
        count += 1
    
print(f"o número de '!' na frase é: {count} ")
print(f"o número de 'a' é: {string.count('a')}")

