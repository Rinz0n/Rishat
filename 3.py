class TicTacToe:
    def __init__(self):
        """Инициализация игры"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X ходит первым
        self.game_over = False
        self.winner = None
        self.moves_count = 0
        
    def display_board(self):
        """Отображение игрового поля"""
        print("\n" + "="*25)
        print("   КРЕСТИКИ-НОЛИКИ")
        print("="*25)
        print()
        print("    0   1   2")  # Номера столбцов
        print("  +---+---+---+")
        
        for i in range(3):
            print(f"{i} |", end="")  # Номер строки
            for j in range(3):
                print(f" {self.board[i][j]} |", end="")
            print()
            print("  +---+---+---+")
        print()
        
    def is_valid_move(self, row, col):
        """Проверка, является ли ход допустимым"""
        if not (0 <= row <= 2 and 0 <= col <= 2):
            return False
        if self.board[row][col] != ' ':
            return False
        return True
    
    def make_move(self, row, col):
        """
        Выполнение хода
        
        Args:
            row: Строка (0-2)
            col: Столбец (0-2)
            
        Returns:
            bool: True если ход выполнен, False если ход недопустим
        """
        if not self.is_valid_move(row, col):
            return False
            
        self.board[row][col] = self.current_player
        self.moves_count += 1
        
        # Проверяем победу
        if self.check_winner():
            self.game_over = True
            self.winner = self.current_player
        # Проверяем ничью
        elif self.moves_count == 9:
            self.game_over = True
        else:
            # Меняем игрока
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            
        return True
    
    def check_winner(self):
        """Проверка, есть ли победитель"""
        # Проверка строк
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
        
        # Проверка столбцов
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != ' ':
                return True
        
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False
    
    def check_line_win(self):
        """
        Проверка, есть ли выигрышная линия и возвращение её координат
        """
        # Проверка строк
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return [(i, 0), (i, 1), (i, 2)]
        
        # Проверка столбцов
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != ' ':
                return [(0, j), (1, j), (2, j)]
        
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return [(0, 2), (1, 1), (2, 0)]
        
        return None
    
    def display_board_with_highlight(self):
        """Отображение доски с подсветкой выигрышной линии"""
        winning_line = self.check_line_win()
        
        print("\n" + "="*25)
        print("   КРЕСТИКИ-НОЛИКИ")
        print("="*25)
        print()
        print("    0   1   2")
        print("  +---+---+---+")
        
        for i in range(3):
            print(f"{i} |", end="")
            for j in range(3):
                cell = self.board[i][j]
                # Подсвечиваем выигрышную линию
                if winning_line and (i, j) in winning_line:
                    print(f" *{cell}*|", end="")
                else:
                    print(f" {cell} |", end="")
            print()
            print("  +---+---+---+")
        print()
    
    def get_player_input(self):
        """Получение ввода от игрока"""
        while True:
            try:
                print(f"Ход игрока {self.current_player}")
                row = int(input("Введите номер строки (0-2): "))
                col = int(input("Введите номер столбца (0-2): "))
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Ошибка! Координаты должны быть от 0 до 2.")
                    continue
                    
                return row, col
                
            except ValueError:
                print("Ошибка! Введите числа от 0 до 2.")
    
    def display_help(self):
        """Отображение справки по игре"""
        print("\n" + "="*40)
        print("              СПРАВКА")
        print("="*40)
        print("Игровое поле имеет координаты:")
        print("  Столбцы: 0, 1, 2 (слева направо)")
        print("  Строки:  0, 1, 2 (сверху вниз)")
        print()
        print("Пример координат:")
        print("  (0,0) - левый верхний угол")
        print("  (1,1) - центр поля")
        print("  (2,2) - правый нижний угол")
        print("="*40)
    
    def reset_game(self):
        """Сброс игры к начальному состоянию"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves_count = 0
        print("\nИгра сброшена. Начинаем новую партию!")
    
    def play_game(self):
        """Основной игровой цикл"""
        print("\nДобро пожаловать в игру 'Крестики-нолики'!")
        print("Игрок X ходит первым.")
        print("Для справки введите 'помощь' или 'help'.")
        print("Для выхода введите 'выход' или 'exit'.")
        print("Для сброса игры введите 'сброс' или 'reset'.")
        
        while True:
            self.display_board()
            
            if self.game_over:
                if self.winner:
                    self.display_board_with_highlight()
                    print(f"Игрок {self.winner} победил!")
                else:
                    print("Ничья! Поле полностью заполнено.")
                
                play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
                if play_again in ['да', 'д', 'yes', 'y']:
                    self.reset_game()
                    continue
                else:
                    print("\nСпасибо за игру!")
                    break
            
            # Получаем ввод от игрока
            print(f"\nСейчас ходит: {self.current_player}")
            command = input("Введите координаты (строку столбец) или команду: ").strip().lower()
            
            # Обработка команд
            if command in ['выход', 'exit', 'quit', 'q']:
                print("\nИгра завершена. До свидания!")
                break
            elif command in ['помощь', 'help', '?']:
                self.display_help()
                continue
            elif command in ['сброс', 'reset', 'новая игра']:
                self.reset_game()
                continue
            
            # Парсим координаты
            try:
                if ' ' in command:
                    parts = command.split()
                    if len(parts) == 2:
                        row, col = int(parts[0]), int(parts[1])
                    else:
                        print("Ошибка! Введите две координаты через пробел.")
                        continue
                else:
                    # Пробуем разные форматы ввода
                    if len(command) == 2 and command.isdigit():
                        row, col = int(command[0]), int(command[1])
                    else:
                        print("Ошибка! Неверный формат ввода.")
                        print("Используйте формат: 'строка столбец' (например: '1 2')")
                        continue
                
                # Выполняем ход
                if self.make_move(row, col):
                    print(f"Ход выполнен на клетку ({row}, {col})")
                else:
                    print("Недопустимый ход! Клетка уже занята или координаты неверны.")
                    
            except ValueError:
                print("Ошибка! Введите числа для координат.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

def main():
    """Точка входа в программу"""
    game = TicTacToe()
    game.play_game()

if __name__ == "__main__":
    main()