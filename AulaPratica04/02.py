mult4=0

num=int(input("digite um número:"))

for i in range (num-1, 0, -1): #ESSE CÓDIGO FAZ EM ORDEM DECRESCENTE
    if i % 4 == 0:
        print(i)
