salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste (em %): "))

percentual_reajuste = percentual_reajuste / 100

novo_salario = salario_atual + (salario_atual * percentual_reajuste)

print("Salário mensal atual: R$", salario_atual)
print("Percentual de reajuste: ", percentual_reajuste * 100, "%")
print("Novo salário: R$", novo_salario)