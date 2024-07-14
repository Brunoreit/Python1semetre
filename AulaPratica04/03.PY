maior1=0
maior2=0

for i in range (10):
    num=int(input("digite um número: "))

    if num > maior1:
        maior2=maior1
        maior1=num

    elif num > maior2 and num < maior1:
        maior2= num

print(f"os dois maiores números digitados são: {maior1} e {maior2}")
