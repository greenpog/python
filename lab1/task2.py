n = int(input())
print("Все числа от 1 до n:")
for i in range(n):
    print(i+1)
print("Все квадраты чисел от 1 до n:")
for i in range(n):
    print((i+1)**2)
print("Сумма всех чисел от 1 до n:")
res=0
for i in range(n):
    res=res+i+1
print(res)