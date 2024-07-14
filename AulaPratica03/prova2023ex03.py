n= int(input("digite o número de mercadorias: "))

baixo=medio=alto=codigo_mercadoria=valor_compra=valor_venda=lucro=soma=0

for i in range (0, n+1):
    valor_venda=float(input("digite o valor da venda: "))
    valor_compra=float(input("digite o valor da compra: "))
    codigo_mercadoria=int(input("digite o código da mercadoria: "))

    lucro=valor_venda*100/valor_compra
    soma_lucros= valor_venda-valor_compra

    if lucro<=10:
        baixo+=1
    elif lucro>10 and lucro<=20:
        medio+=1
    elif lucro >20:
        alto+=1
    
    print(f"quantidade de produtos com lucro baixo {baixo}")
    print(f"quantidade de produtos com o lucro medio {medio}")
    print(f"quantidade de produtos com o lucro alto {alto}")
    print(f"soma total dos lucros: R${soma_lucros}")

