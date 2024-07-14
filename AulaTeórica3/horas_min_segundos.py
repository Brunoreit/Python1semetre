num= int(input("Escreva o número inteiro em segundos: \n"))
seg_horas= num//3600
seg_min= (num%3600)//60
seg= num%60
print (f"{seg_horas}horas {seg_min}minutos {seg}segundos")