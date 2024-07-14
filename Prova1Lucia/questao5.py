menorMultiplo6=999999
somaMultiplo7=0 
count=0
nuns= int(input("Digite quantos números deseja inserir: "))

while (count<nuns):
    count+=1
    num= int(input("Digite um número: "))

    if (num%6 == 0) and (num < menorMultiplo6):
        menorMultiplo6=num
    
    if (num%7 ==0):
        somaMultiplo7+=num
    
print(f"{somaMultiplo7} , {menorMultiplo6}")