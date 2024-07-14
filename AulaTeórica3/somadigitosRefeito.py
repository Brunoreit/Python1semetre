num= int(input("Escreva um número inteiro de até 2 dígitos: "))

if num<0:
    num*=-1

if 0<= num <= 99: 
    soma = (num // 10) + (num % 10)
    
   
    print(f"A soma dos dígitos é: {soma}")
else:
    print("Por favor, digite um número de até 2 dígitos.")