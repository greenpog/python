import random
import time
from datetime import datetime

# Сохраняет статистику игры в файл stats.txt
def save_stats(attempts, game_time, won):
    stats = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'attempts': attempts,
        'time_sec': round(game_time, 2),
        'result': 'Won' if won else 'Lost'
    }
    
    try:
        # Пытаемся прочитать существующую статистику
        with open('stats.txt', 'r') as f:
            data = f.readlines()
            # Удаляем пустые строки
            data = [line.strip() for line in data if line.strip()]
    except FileNotFoundError:
        # Если файла нет, создаем новую статистику
        data = []
    
    # Добавляем новую запись
    data.append(str(stats))
    
    # Записываем обновленные данные
    with open('stats.txt', 'w') as f:
        f.write('\n'.join(data))

# Основная логика игры
def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1
            
            if guess < number:
                print("Мое число больше!")
            elif guess > number:
                print("Мое число меньше!")
            else:
                end_time = time.time()
                game_time = end_time - start_time
                print(f"Поздравляю! Ты угадал за {attempts} попыток и {round(game_time, 2)} секунд!")
                save_stats(attempts, game_time, True)
                break
                
            if attempts >= 10:
                end_time = time.time()
                game_time = end_time - start_time
                print(f"Ты исчерпал 10 попыток. Я загадал число {number}.")
                save_stats(attempts, game_time, False)
                break
                
        except ValueError:
            print("Пожалуйста, вводи только числа!")

# Показывает статистику из файла
def show_stats():
    try:
        with open('stats.txt', 'r') as f:
            data = f.readlines()
            print("\n=== ИСТОРИЯ ИГР ===")
            for i, game in enumerate(data, 1):
                print(f"{i}. {game.strip()}")
    except FileNotFoundError:
        print("Статистика пока недоступна. Сыграйте хотя бы одну игру!")

def main():
    while True:
        print("\n1. Новая игра")
        print("2. Показать статистику")
        print("3. Выход")
        
        choice = input("Выбери действие: ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            show_stats()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуй еще раз.")

main()