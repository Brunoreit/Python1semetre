salario_fixo= float(input("Escreva o salário fixo: "))
carros_vendidos= int(input("Digite o número de carros vendidos: "))
valor_total_vendas= float(input("Digite o valor total das vendas: "))

comissao= carros_vendidos*200
adicional_5= valor_total_vendas*5/100

novo_salario= salario_fixo+comissao+adicional_5

print(f"Salário base: {salario_fixo},\n número de carros vendidos: {carros_vendidos},\n Total de vendas: R$ {valor_total_vendas},\n Total de comissão: R$ {comissao},\n Total do adicional de 5%: R$ {adicional_5},\n Salário a receber: R$ {novo_salario}")
