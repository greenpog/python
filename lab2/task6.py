import re
from datetime import datetime

INPUT_FILENAME = "text.txt"
FILENAME_1 = "dates.txt"
REG_1 = r'\b(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'

def writefile(reg, name, text):
    result=re.findall(reg,text)
    l=len(result)
    
    newformat=[]
    for i in range(0, l):
        yr =  result[i][2]
        month = result[i][1]
        day = result[i][0]
        newformat.append(f"{yr}-{month}-{day}")

    res_sorted = sorted(newformat, key = lambda formated: datetime.strptime(formated, "%Y-%m-%d"))
    if l!=0:
        try:
            with open(name, 'a') as f:
                for i in range(l):
                    f.write(res_sorted[i]+"\n")
        except Exception as err:
            print(f"Ошибка: {err}")

try: #исходный
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        text=f.read()
except FileNotFoundError:
    print("Нет файла с таким названием")
except Exception as err:
    print(f"Ошибка: {err}")

writefile(REG_1, FILENAME_1, text)