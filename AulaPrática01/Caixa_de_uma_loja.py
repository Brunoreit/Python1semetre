valor_compra= float(input("digite o valor da compra: "))
valor_pago= float(input("digite o valor pago: "))
troco= valor_pago-valor_compra

if troco==0:
    print("não há troco!")

else:
    print(f"troco a ser devolvido é {troco}R$")

lista_cedulas= [20,10,5,1]

for celuda in lista_cedulas:
    quantidade_cedula= troco//celuda
    print(f"Será entregue {quantidade_cedula} cedulas de {celuda} ")
    troco=troco%celuda

    #SEM USAR O FOR, APENAS IF

valor_compra= float(input("digite o valor da compra: "))
valor_pago= float(input("digite o valor pago: "))
troco= valor_pago-valor_compra

cedulas=[20,10,5,1]

troco_cedula20= troco//20
print(f"Serão entregues {troco_cedula20} cedulas de 20")
troco=troco%20

troco_cedula10= troco//10
print(f"Serão entregues {troco_cedula10} cedulas de 10")
troco=troco%10

troco_cedula5= troco//5
print(f"Serão entregues {troco_cedula5} cedulas de 10")
troco=troco%5
troco_cedula1= troco//1
print(f"Serão entregues {troco_cedula1} cedulas de 10")




