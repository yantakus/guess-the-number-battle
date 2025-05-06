import random
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "="*50)
    print(Fore.MAGENTA + "       🎯 Игра: Угадай число — Битва умов 🎯")
    print(Fore.CYAN + "="*50)

def get_player_guess(player_name):
    while True:
        try:
            guess = int(input(f"{player_name}, введите число от 1 до 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print(Fore.RED + "Число должно быть от 1 до 100.")
        except ValueError:
            print(Fore.RED + "Пожалуйста, введите целое число!")

def play_game():
    print_banner()

    mode = input(Fore.YELLOW + "Выберите режим: \n1 - Два игрока\n2 - Против компьютера\nВаш выбор: ")

    if mode == "1":
        player1 = input(Fore.GREEN + "Введите имя первого игрока: ")
        player2 = input(Fore.GREEN + "Введите имя второго игрока: ")
        players = [player1, player2]
    else:
        player1 = input(Fore.GREEN + "Введите ваше имя: ")
        player2 = "Компьютер"
        players = [player1, player2]

    secret_number = random.randint(1, 100)
    rounds = 10
    closest_player = None
    closest_diff = 100
    closest_guess = None

    for round_number in range(1, rounds + 1):
        print(Fore.CYAN + f"\n--- Раунд {round_number} ---")
        for player in players:
            if player == "Компьютер":
                guess = random.randint(1, 100)
                print(Fore.LIGHTBLUE_EX + f"{player} загадал число: {guess}")
            else:
                guess = get_player_guess(player)

            if guess == secret_number:
                print(Fore.GREEN + f"\nПоздравляем, {player} угадал число {secret_number}!")
                print(Fore.LIGHTMAGENTA_EX + "🏆 Победа! 🏆")
                return
            else:
                diff = abs(secret_number - guess)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_player = player
                    closest_guess = guess

    # Если никто не угадал за раунды
    print(Fore.RED + f"\nНикто не угадал число за {rounds} раундов.")
    print(Fore.YELLOW + f"Загаданное число было: {secret_number}")
    print(Fore.LIGHTGREEN_EX + f"Ближе всего был: {closest_player} (число: {closest_guess})!")

def main():
    while True:
        play_game()
        again = input(Fore.YELLOW + "\nХотите сыграть ещё раз? (да/нет): ").lower()
        if again != "да":
            print(Fore.GREEN + "Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()
