arr=list(range(1,21))

even_n = list(filter(lambda x: x%2==0, arr))
print(f"Чётные: {even_n}")

increased = list(map(lambda x: x + 10, arr))
print(f"Увеличенные на 10 числа: {increased}")

sorted = sorted(arr, key=lambda x: x, reverse=True)
print(f"Отсортированные по убыванию:{sorted}")