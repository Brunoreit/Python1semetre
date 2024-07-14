x1=0
x2=0
x3=0
x4=0

nums=float(input("digite um número: "))

while nums >=0:
    
    if nums >=0 and nums <=25:
        x1+=1
    
    elif nums>=26 and nums<=50:
        x2+=1

    elif nums>=51 and nums<=75:
        x3+=1

    elif nums>=76 and nums<=100:
        x4+=1
    nums=float(input("digite um número: "))

print(f"{x1} números estão no intervalo de 0 à 25")
print(f"{x2} números estão no intervalo de 26 à 50")
print(f"{x3} números estão no intervalo de 51 à 75")
print(f"{x4} números estão no intervalo de 76 à 100")
print("Fim do programa!")
