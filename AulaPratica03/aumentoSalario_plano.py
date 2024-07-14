salario_atual= float(input("digite o salario atual: "))
plano= int(input("digite o plano atual: "))


if plano==1:
    novo_salario=salario_atual+(salario_atual*0.10)
    
    
elif plano==2:
    novo_salario=salario_atual+(salario_atual*0.15)
    

elif plano==3:
    novo_salario=salario_atual+(salario_atual*0.20)
    
if plano==1 or plano==2 or plano==3:
    print(f"o novo salário de acordo com o plano {plano} é {novo_salario}")

else:
    print("digite um plano válido!")

