import random
a=[]
for i in range(10):
    a.append(random.randint(-5,5))
print(a)
max_a = max(a)
min_a = min(a)
print("Максимальное значение:", max_a,"\nМинимальное значение:", min_a)

res=0
for i in range(10):
    res=res+a[i]
print("Сумма:", res)

a.sort()
print("Сортировка по возрастанию:", a)