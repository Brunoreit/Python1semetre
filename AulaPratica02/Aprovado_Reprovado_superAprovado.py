N1= float(input("Digite a primeira nota: "))
N2= float(input("Digite a segunta nota: "))
P1= int(input("Digite o primeiro peso: "))
P2= int(input("Digite o segundo peso: "))
media_ponderada= (N1*P1+N2*P2)/(P1+P2)

if media_ponderada == 10:
    print("O aluno foi APROVADO COM LOUVOR")
elif media_ponderada >= 7:
    print("O aluno foi APROVADO")
else:
    print("O aluno foi REPROVADO")

    #OU
    

if (media_ponderada>=7):
    if (media_ponderada==10):
        print("aprovado com louvor!!!")
    else:
        print ("aprovado")
else:
    print ("reprovado")

