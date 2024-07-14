while True:
    
    num = int(input("digite o número a ser fatorado: "))

    if num < 0:
        print("Número negativo detectado! Digite um valor válido")

        continue
    fatorial = 1

    for numero in range(1,num+1):
        
        fatorial = fatorial * numero
    
    print(f"O fatorial de {num} é {fatorial}")

    escolha = int(input("Deseja inserir outro número? 1-SIM 2-NÃO:  "))

    if escolha == 1:
        continue
    else:
        break
