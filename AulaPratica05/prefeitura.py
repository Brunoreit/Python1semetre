total_salario=0 
total_filho=0
maior_salario=0
pessoas_sal_ate100=0
num_pessoas=0
while True:
    salario = float(input("digite seu salário: "))

    if salario < 0:
        print("Digite um valor válido!")

        continue

    num_filhos = int(input("digite o número de filhos: "))

    if num_filhos < 0:
        print("Digite um valor válido!")

        continue

    total_salario += salario
    num_pessoas += 1
    total_filho += num_filhos

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 100:
        pessoas_sal_ate100 += 1
    

    escolha = int(input("Deseja incluir mais uma pessoa? 1-SIM 2-NÃO"))

    if escolha == 1:
        continue
    else:
        break
    

media_salario = (total_salario / num_pessoas)
media_filhos = (total_filho / num_pessoas)
perc_pessoas_100 = (pessoas_sal_ate100 / num_pessoas)*100

print("----RESULTADOS----")
print(f"A média do salário da população é: {media_salario}R$")
print(f"A média do número de filhos é: {media_filhos}")
print(f"O maior salário é: {maior_salario}R$")
print(f"O percentual de pessoal com salário até R$100 é: {perc_pessoas_100} ")

        
    
    

    
