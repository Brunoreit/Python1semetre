a=1350
print(f"a={a}", end='')
b=0
c=0

while a>0:
    if (a%10==3) or (a%10==5):
        b+=1
        c=c+a%10
    a=a//10

print(f"b={b} c={c}")