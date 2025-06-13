try:
    a = int(input())
    b = int(input())
    result=a/b

except ValueError:
    print("Ошибка: нечисловое значение")

except ZeroDivisionError:
    print("Ошибка: деление на ноль")

else:
    print(result)