import random

def fillfile():  #создаёт файл с числами
    with open("data.txt", "w") as clean:
        pass
    f = open("data.txt", "a")
    for i in range(0, 10):
        randomint = random.randint(0, 1000)
        f.write(str(randomint) + "\n")
    f.close()
            
def readfile(): #считывает числа и записывает в итоговый файл
    fillfile()
    numlist = []
    f = open("data.txt", "r")
    for i in range(0, 10):
        num = f.readline()
        num = int(num)
        numlist.append(num)
    f.close()
    f = open("results.txt", "a")
    summ = sum(numlist)
    maximal = max(numlist)
    minimal = min(numlist)
    f.write(f"Результаты для: {numlist}\n")
    f.write(f"Сумма: {summ}\n")
    f.write(f"Среднее: {summ/10}\n")
    f.write(f"Максимум: {maximal}\n")
    f.write(f"Минимум: {minimal}\n\n")
    return(numlist)

gtegt = readfile()
print(gtegt)