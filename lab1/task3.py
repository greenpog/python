n = int(input())
print("Все числа от n до 1:")
i=n
while i>0:
    print(i)
    i-=1
print("Факториал n:")
if n>=1:
    res=1
    i=1
    while i<=n:
        res=res*i
        i+=1
    print(res)