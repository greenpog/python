import re

INPUT_FILENAME = "text.txt"
FILENAME_1 = "emails.txt"
FILENAME_2 = "phones.txt"
FILENAME_3 = "capital_words.txt"
REG_1 = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
REG_2 = r"\+7-\d{3}-\d{3}-\d{2}-\d{2}"
REG_3 = r"\b[A-Z][a-zA-Z-']*" #только латинские буквы и пара символов, что угодно другое (цифры) не выводится

def writefile(reg, name, text):
    result=re.findall(reg,text)
    l=len(result)
    if l!=0:
        try:
            with open(name, 'a') as f:
                for i in range(l):
                    f.write(result[i]+"\n")
        except Exception as err:
            print(f"Ошибка: {err}")
    

try: #работа с 1 файлом
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        text=f.read()
except FileNotFoundError:
    print("Нет файла с таким названием")
except Exception as err:
    print(f"Ошибка: {err}")

writefile(REG_1, FILENAME_1, text)
writefile(REG_2, FILENAME_2, text)
writefile(REG_3, FILENAME_3, text)