idadejovem = 99999; nomejovem = ''; idadevelha = 0; nomevelha = ''

while True :

    nome = input("digite seu primeiro nome: ")
    idade = int(input("digite sua idade: "))

    if idade < 0:
        print("Idade não pode ser negativa. PROGRAMA ENCERRADO")
        break

    if idade < idadejovem:
        idadejovem = idade
        nomejovem = nome

    elif idade == idadejovem:
        nomejovem += "," +nome
    
    if idade > idadevelha:
        idadevelha = idade
        nomevelha = nome
    

print(f"O nome e a idade da pessoa mais jovem é: {nomejovem} que possui {idadejovem} anos")
print(f"O nome e a idade da pessoa mais velha é: {nomevelha} {idadevelha}")