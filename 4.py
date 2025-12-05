import random

class Hangman:
    def __init__(self):
        """Инициализация игры"""
        self.words = [
            # Простые слова (4-5 букв)
            'кот', 'дом', 'лес', 'ночь', 'вода', 'ветер', 'солнце', 'река',
            'книга', 'стол', 'окно', 'дверь', 'город', 'улица', 'школа',
            
            # Средней сложности (6-8 букв)
            'компьютер', 'программа', 'библиотека', 'телефон', 'автомобиль',
            'погода', 'работа', 'праздник', 'музыка', 'картина', 'история',
            
            # Сложные слова (9+ букв)
            'государство', 'университет', 'эксперимент', 'путешествие',
            'достопримечательность', 'интеллект', 'конституция'
        ]
        
        self.word = ''
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.max_attempts = 6
        self.attempts_left = 0
        self.game_over = False
        self.won = False
        
    def select_word(self):
        """Выбор случайного слова"""
        self.word = random.choice(self.words).upper()
        self.attempts_left = self.max_attempts
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.game_over = False
        self.won = False
        
    def display_word_state(self):
        """Отображение текущего состояния слова"""
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append('_')
        
        print("Слово: " + ' '.join(display))
        print()
    
    def display_hangman(self):
        """Отображение виселицы"""
        stages = [
            # 0 попыток использовано
            """
                ------
                |    |
                |
                |
                |
                |
                |
            ------------
            """,
            # 1 попытка использована
            """
                ------
                |    |
                |    O
                |
                |
                |
                |
            ------------
            """,
            # 2 попытки использованы
            """
                ------
                |    |
                |    O
                |    |
                |
                |
                |
            ------------
            """,
            # 3 попытки использованы
            """
                ------
                |    |
                |    O
                |   /|
                |
                |
                |
            ------------
            """,
            # 4 попытки использованы
            """
                ------
                |    |
                |    O
                |   /|\\
                |
                |
                |
            ------------
            """,
            # 5 попыток использовано
            """
                ------
                |    |
                |    O
                |   /|\\
                |   /
                |
                |
            ------------
            """,
            # 6 попыток использовано (проигрыш)
            """
                ------
                |    |
                |    O
                |   /|\\
                |   / \\
                |
                |
            ------------
            """
        ]
        
        wrong_count = len(self.wrong_letters)
        print(stages[wrong_count])
    
    def display_game_state(self):
        """Отображение всего состояния игры"""
        print("\n" + "="*50)
        print("                ВИСЕЛИЦА")
        print("="*50)
        
        # Отображаем виселицу
        self.display_hangman()
        
        # Отображаем информацию
        print(f"Осталось попыток: {self.attempts_left}")
        print(f"Длина слова: {len(self.word)} букв")
        
        # Отображаем текущее состояние слова
        self.display_word_state()
        
        # Отображаем использованные буквы
        if self.wrong_letters:
            print("Неверные буквы:", ' '.join(sorted(self.wrong_letters)))
        
        if self.guessed_letters - self.wrong_letters:
            print("Угаданные буквы:", ' '.join(sorted(self.guessed_letters - self.wrong_letters)))
        
        print("="*50)
    
    def process_guess(self, guess):
        """
        Обработка предположения игрока
        
        Args:
            guess: Буква или слово, введенное игроком
            
        Returns:
            str: Сообщение о результате
        """
        guess = guess.upper().strip()
        
        # Проверка на ввод слова целиком
        if len(guess) > 1:
            if guess == self.word:
                self.won = True
                self.game_over = True
                return "Поздравляем! Вы угадали слово!"
            else:
                self.attempts_left -= 1
                if self.attempts_left <= 0:
                    self.game_over = True
                return "Неверное слово!"
        
        # Проверка на одну букву
        if len(guess) != 1:
            return "Пожалуйста, введите одну букву или всё слово!"
        
        if not guess.isalpha() or guess not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            return "Пожалуйста, введите русскую букву!"
        
        # Проверка, не вводилась ли уже эта буква
        if guess in self.guessed_letters:
            return f"Буква '{guess}' уже была!"
        
        # Добавляем букву в использованные
        self.guessed_letters.add(guess)
        
        # Проверяем, есть ли буква в слове
        if guess in self.word:
            # Проверяем, угадано ли всё слово
            if all(letter in self.guessed_letters for letter in self.word):
                self.won = True
                self.game_over = True
                return f"Буква '{guess}' есть в слове! Вы угадали всё слово!"
            else:
                return f"Буква '{guess}' есть в слове!"
        else:
            # Неверная буква
            self.wrong_letters.add(guess)
            self.attempts_left -= 1
            
            if self.attempts_left <= 0:
                self.game_over = True
                return f"Буквы '{guess}' нет в слове. Попытки закончились!"
            else:
                return f"Буквы '{guess}' нет в слове."
    
    def get_hint(self):
        """Предоставление подсказки"""
        # Находим буквы, которые еще не угаданы
        remaining_letters = [letter for letter in self.word if letter not in self.guessed_letters]
        
        if not remaining_letters:
            return "Все буквы уже угаданы!"
        
        # Выбираем случайную неугаданную букву
        hint_letter = random.choice(remaining_letters)
        self.guessed_letters.add(hint_letter)
        
        # Штраф за подсказку - потеря одной попытки
        self.attempts_left -= 1
        
        return f"Подсказка: в слове есть буква '{hint_letter}'. Вы теряете одну попытку."
    
    def display_rules(self):
        """Отображение правил игры"""
        print("\n" + "="*60)
        print("                        ПРАВИЛА ИГРЫ")
        print("="*60)
        print("""
        1. Компьютер загадывает случайное слово.
        2. Вы должны угадать слово, предлагая по одной букве.
        3. Если буква есть в слове, она открывается во всех позициях.
        4. Если буквы нет в слове, вы теряете одну попытку.
        5. У вас есть 6 попыток.
        6. Вы можете попытаться угадать всё слово сразу.
        7. Если угадаете все буквы или всё слово - вы победили!
        8. Если попытки закончатся - вы проиграли.
        
        Команды:
        - 'помощь' - показать правила
        - 'подсказка' - получить подсказку (стоит 1 попытку)
        - 'сдаюсь' - завершить текущую игру
        - 'выход' - выйти из игры
        """)
        print("="*60)
    
    def play_game(self):
        """Основной игровой цикл"""
        print("\nДобро пожаловать в игру 'Виселица'!")
        print("Угадайте слово по буквам!")
        
        self.select_word()
        self.display_rules()
        
        while True:
            if self.game_over:
                self.display_game_state()
                
                if self.won:
                    print("\n" + "*" * 50)
                    print("ПОБЕДА! Вы угадали слово!")
                    print(f"Загаданное слово: {self.word}")
                    print("*" * 50)
                else:
                    print("\n" + "-" * 50)
                    print("ПОРАЖЕНИЕ! Вы исчерпали все попытки.")
                    print(f"Загаданное слово: {self.word}")
                    print("-" * 50)
                
                play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
                if play_again in ['да', 'д', 'yes', 'y']:
                    self.select_word()
                    print("\nНовая игра начинается!")
                    continue
                else:
                    print("\nСпасибо за игру!")
                    break
            
            self.display_game_state()
            
            # Получаем ввод от игрока
            guess = input("\nВведите букву или слово (для помощи введите 'помощь'): ").strip()
            
            # Обработка команд
            if guess.lower() in ['выход', 'exit', 'quit', 'q']:
                print("\nИгра завершена. До свидания!")
                break
            elif guess.lower() in ['помощь', 'help', '?']:
                self.display_rules()
                continue
            elif guess.lower() in ['подсказка', 'hint', 'помоги']:
                if self.attempts_left > 1:
                    result = self.get_hint()
                    print(f"\n{result}")
                else:
                    print("\nНедостаточно попыток для подсказки!")
                continue
            elif guess.lower() in ['сдаюсь', 'сдаться', 'give up']:
                print(f"\nВы сдались. Загаданное слово было: {self.word}")
                play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
                if play_again in ['да', 'д', 'yes', 'y']:
                    self.select_word()
                    print("\nНовая игра начинается!")
                    continue
                else:
                    print("\nСпасибо за игру!")
                    break
            
            # Обработка буквы или слова
            if guess:
                result = self.process_guess(guess)
                print(f"\n{result}")

def main():
    """Точка входа в программу"""
    game = Hangman()
    game.play_game()

if __name__ == "__main__":
    main()