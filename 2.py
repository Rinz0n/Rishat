import random

class BullsAndCows:
    def __init__(self):
        """Инициализация игры"""
        self.secret_number = None
        self.max_attempts = 10
        self.attempts = 0
        self.difficulty = None
        
    def generate_secret_number(self, difficulty='medium'):
        """
        Генерация секретного числа в зависимости от уровня сложности
        
        Args:
            difficulty: Уровень сложности ('easy', 'medium', 'hard')
        """
        self.difficulty = difficulty
        
        if difficulty == 'easy':
            # Легкий: 3-значное число без повторяющихся цифр
            self.secret_number = self.generate_unique_number(3)
            self.max_attempts = 12
        elif difficulty == 'medium':
            # Средний: 4-значное число без повторяющихся цифр
            self.secret_number = self.generate_unique_number(4)
            self.max_attempts = 10
        elif difficulty == 'hard':
            # Сложный: 5-значное число без повторяющихся цифр
            self.secret_number = self.generate_unique_number(5)
            self.max_attempts = 8
        else:
            # По умолчанию 4-значное число
            self.secret_number = self.generate_unique_number(4)
            self.max_attempts = 10
            
        self.attempts = 0
    
    def generate_unique_number(self, length):
        """
        Генерация числа заданной длины без повторяющихся цифр
        
        Args:
            length: Длина числа (количество цифр)
            
        Returns:
            str: Строковое представление числа
        """
        digits = list(range(10))
        # Первая цифра не может быть 0
        first_digit = random.choice(digits[1:])
        digits.remove(first_digit)
        
        number_digits = [str(first_digit)]
        
        # Добавляем остальные цифры
        for _ in range(length - 1):
            digit = random.choice(digits)
            digits.remove(digit)
            number_digits.append(str(digit))
        
        return ''.join(number_digits)
    
    def check_guess(self, guess):
        """
        Проверка предположения игрока
        
        Args:
            guess: Предположение игрока (строка)
            
        Returns:
            tuple: (быки, коровы, совпадение)
        """
        if len(guess) != len(self.secret_number):
            return 0, 0, False
        
        bulls = 0  # Правильная цифра на правильном месте
        cows = 0   # Правильная цифра на неправильном месте
        
        for i in range(len(guess)):
            if guess[i] == self.secret_number[i]:
                bulls += 1
            elif guess[i] in self.secret_number:
                cows += 1
        
        is_correct = (bulls == len(self.secret_number))
        return bulls, cows, is_correct
    
    def validate_input(self, guess, length):
        """
        Проверка ввода пользователя
        
        Args:
            guess: Ввод пользователя
            length: Ожидаемая длина числа
            
        Returns:
            tuple: (валидность, сообщение об ошибке)
        """
        if not guess.isdigit():
            return False, "Введите только цифры!"
        
        if len(guess) != length:
            return False, f"Число должно содержать {length} цифр!"
        
        if len(set(guess)) != len(guess):
            return False, "Цифры не должны повторяться!"
        
        if guess[0] == '0':
            return False, "Число не может начинаться с нуля!"
        
        return True, ""
    
    def get_difficulty_level(self):
        """Выбор уровня сложности"""
        print("\n" + "="*40)
        print("Выберите уровень сложности:")
        print("1. Легкий (3 цифры, 12 попыток)")
        print("2. Средний (4 цифры, 10 попыток) - по умолчанию")
        print("3. Сложный (5 цифр, 8 попыток)")
        print("="*40)
        
        choice = input("Ваш выбор (1-3): ").strip()
        
        if choice == '1':
            return 'easy'
        elif choice == '3':
            return 'hard'
        else:
            return 'medium'
    
    def get_hint(self, attempt_number):
        """
        Предоставление подсказки игроку
        
        Args:
            attempt_number: Номер текущей попытки
        """
        hints = [
            "Попробуйте начинать с середины диапазона возможных чисел.",
            "Обращайте внимание на цифры, которые уже встречались в ваших попытках.",
            "Помните: 'быки' - правильная цифра на правильном месте, 'коровы' - правильная цифра на неправильном месте.",
            "Попробуйте сначала определить все цифры, которые есть в числе.",
            "Используйте информацию о 'коровах' для определения позиций цифр.",
        ]
        
        if attempt_number % 3 == 0:
            print(f"\nПодсказка: {hints[(attempt_number // 3) % len(hints)]}")
    
    def display_rules(self):
        """Отображение правил игры"""
        print("\n" + "="*50)
        print("             ПРАВИЛА ИГРЫ 'БЫКИ И КОРОВЫ'")
        print("="*50)
        print("""
        Компьютер загадывает число из неповторяющихся цифр.
        Ваша задача - угадать это число за ограниченное количество попыток.
        
        После каждой вашей попытки компьютер сообщает:
        • 'Быки' - сколько цифр угадано и находятся на своих местах
        • 'Коровы' - сколько цифр угадано, но находятся не на своих местах
        
        Пример:
        Загаданное число: 1234
        Ваша попытка: 1325
        Результат: 1 бык (цифра 1 на своем месте) и 2 коровы (цифры 2 и 3 есть в числе, но не на своих местах)
        
        Удачи!
        """)
        print("="*50)
    
    def play_game(self):
        """Основной игровой цикл"""
        print("\nДобро пожаловать в игру 'БЫКИ И КОРОВЫ'!")
        
        while True:
            self.display_rules()
            
            # Выбор уровня сложности
            difficulty = self.get_difficulty_level()
            self.generate_secret_number(difficulty)
            
            length = len(self.secret_number)
            print(f"\nЗагадано {length}-значное число. У вас {self.max_attempts} попыток!")
            print("Подсказка: Все цифры в числе различны, и число не начинается с нуля.")
            
            previous_guesses = []
            
            while self.attempts < self.max_attempts:
                attempts_left = self.max_attempts - self.attempts
                print(f"\n--- Попытка: {self.attempts + 1} из {self.max_attempts} (осталось: {attempts_left}) ---")
                
                # Показываем предыдущие попытки
                if previous_guesses:
                    print("\nПредыдущие попытки:")
                    for i, (guess, bulls, cows) in enumerate(previous_guesses, 1):
                        print(f"  {i:2d}. {guess} -> Быков: {bulls}, Коров: {cows}")
                
                # Получаем предположение от игрока
                guess = input(f"\nВведите {length}-значное число (или 'сдаюсь' для выхода): ").strip()
                
                # Проверяем, не хочет ли игрок сдаться
                if guess.lower() in ['сдаюсь', 'сдаться', 'выход', 'exit', 'quit', 'q']:
                    print(f"\nВы сдались. Загаданное число было: {self.secret_number}")
                    break
                
                # Проверяем ввод
                is_valid, error_msg = self.validate_input(guess, length)
                if not is_valid:
                    print(f"Ошибка: {error_msg}")
                    continue
                
                # Проверяем предположение
                self.attempts += 1
                bulls, cows, is_correct = self.check_guess(guess)
                
                # Сохраняем попытку
                previous_guesses.append((guess, bulls, cows))
                
                # Проверяем, угадал ли игрок
                if is_correct:
                    print("\n" + "*" * 50)
                    print(f"ПОЗДРАВЛЯЕМ! Вы угадали число {self.secret_number}!")
                    print(f"Количество попыток: {self.attempts}")
                    print("*" * 50)
                    break
                else:
                    print(f"\nРезультат: {bulls} быков, {cows} коров")
                    
                    # Даем подсказку
                    if bulls + cows == length:
                        print("Отлично! Все цифры угаданы, осталось правильно их расставить!")
                    elif bulls + cows == 0:
                        print("Ни одной правильной цифры! Попробуйте другие цифры.")
                    
                    # Предоставляем подсказку каждые 3 попытки
                    self.get_hint(self.attempts)
            
            # Если попытки закончились
            if not is_correct and self.attempts >= self.max_attempts:
                print("\n" + "-" * 40)
                print("К сожалению, попытки закончились!")
                print(f"Загаданное число было: {self.secret_number}")
                print("-" * 40)
            
            # Предлагаем сыграть еще раз
            play_again = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
            if play_again not in ['да', 'д', 'yes', 'y']:
                print("\nСпасибо за игру! До новых встреч!")
                break
            
            # Сбрасываем счетчик попыток для новой игры
            self.attempts = 0
            print("\n" + "="*50 + "\n")

def main():
    """Точка входа в программу"""
    game = BullsAndCows()
    game.play_game()

if __name__ == "__main__":
    main()