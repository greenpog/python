a = int(input())
b = int(input())
c = int(input())
max_n = max(a,b,c)
min_n = min(a,b,c)
print("Максимальное значение:", max_n)
print("Минимальное значение:", min_n)
if a==b==c: 
    print("Все числа равны")
else: 
    print("Все числа не равны")
