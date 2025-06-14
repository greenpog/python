import random
import os
import time

MIN_CARD = 2
MAX_CARD = 11
DEALER_STOP = 17
BLACKJACK = 21

def deal_card():
    #Возвращает случайную карту
    return random.randint(MIN_CARD, MAX_CARD)

def display_hands(player_hand, dealer_hand, show_all_dealer=False):
    #Отображает карты игрока и дилера.
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Ты: {player_hand} (Счёт: {sum(player_hand)})")
    if show_all_dealer:
        print(f"Дилер: {dealer_hand} (Счёт: {sum(dealer_hand)})")
    else:
        print(f"Дилер: [{dealer_hand[0]}, ***]")
    print("-" * 20)

def get_player_choice():
    #Запрашивает действие игрока с проверкой ввода.
    while True:
        choice = input("Введите 'a' чтобы взять ещё, или 's' чтобы остановиться: ").lower()
        if choice in ('a', 's'):
            return choice
        print("Некорректный ввод! Попробуйте ещё раз.")

def game_loop():
    #Основной цикл игры.
    while True:
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]
        player_score = sum(player_hand)
        
        # Фаза игрока
        while player_score <= BLACKJACK:
            display_hands(player_hand, dealer_hand)
            if player_score == BLACKJACK:
                print("Блэкджек! Ты выиграл!")
                break
                
            choice = get_player_choice()
            if choice == 'a':
                player_hand.append(deal_card())
                player_score = sum(player_hand)
                if player_score > BLACKJACK:
                    display_hands(player_hand, dealer_hand)
                    print("Перебор, ты проиграл!")
                    break
            else:
                break  # Игрок остановился

        # Фаза дилера (если игрок не проиграл)
        if player_score <= BLACKJACK:
            print("\n--- Ход дилера ---")
            dealer_score = sum(dealer_hand)
            display_hands(player_hand, dealer_hand, show_all_dealer=True)
            
            while dealer_score < DEALER_STOP:
                time.sleep(1.5)
                dealer_hand.append(deal_card())
                dealer_score = sum(dealer_hand)
                display_hands(player_hand, dealer_hand, show_all_dealer=True)
                print(f"Дилер берёт карту... Счёт: {dealer_score}")

            # Определение победителя
            print("\n--- Результат ---")
            display_hands(player_hand, dealer_hand, show_all_dealer=True)
            if dealer_score > BLACKJACK:
                print("Дилер перебрал! Ты выиграл!")
            elif dealer_score > player_score:
                print("Дилер выиграл!")
            elif player_score > dealer_score:
                print("Ты выиграл!")
            else:
                print("Ничья!")

        # Предложение сыграть ещё
        if input("\nСыграем ещё? (a/s): ").lower() != 'a':
            break

game_loop()