preco_prod= float(input("Escreva o preço do produto: "))
desconto_porcentagem= float(input("Escreva o desconto em porcentagem: "))
porcentagem_reais= preco_prod*desconto_porcentagem/100
novo_preço= preco_prod+(preco_prod*desconto_porcentagem/100)

print(f"O valor inicial era: R$ {preco_prod}")
print(f"O desconto em porcentagem é: % {desconto_porcentagem} e em reais é: R$ {porcentagem_reais} ")
print(f"O novo valor do produto é {novo_preço}")