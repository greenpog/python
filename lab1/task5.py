import random
a=[]
for i in range(20):
    a.append(random.randint(1,100))
print(a)

b=[]
for i in range(20):
    if a[i]%2==0:
        b.append(a[i])
print("Чётные:", b)

b=[]
for i in range(20):
    if a[i]%3==0:
        b.append(a[i])
print("Делятся на 3:", b)

sum=0
for i in range(20):
    sum=sum+a[i]
print("Среднее арифметическое:", sum/20)