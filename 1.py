import random
import sys
from typing import List, Tuple, Optional

class Puzzle15:
    def __init__(self):
        """Инициализация игрового поля"""
        self.size = 4
        self.board = []
        self.empty_pos = (3, 3)  # начальная позиция пустой клетки (правый нижний угол)
        self.init_board()
        
    def init_board(self):
        """Инициализация игрового поля в решаемом состоянии"""
        # Создаем упорядоченное поле
        self.board = [[i * self.size + j + 1 for j in range(self.size)] 
                     for i in range(self.size)]
        self.board[self.size-1][self.size-1] = 0  # пустая клетка
        
        # Перемешиваем поле, совершая случайные допустимые ходы
        self.shuffle_board()
        
    def shuffle_board(self, moves: int = 1000):
        """Перемешивание игрового поля, совершая случайные допустимые ходы"""
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # вправо, влево, вниз, вверх
        
        for _ in range(moves):
            possible_moves = []
            empty_row, empty_col = self.empty_pos
            
            # Проверяем все возможные ходы из текущей позиции
            for dr, dc in directions:
                new_row, new_col = empty_row + dr, empty_col + dc
                if 0 <= new_row < self.size and 0 <= new_col < self.size:
                    possible_moves.append((dr, dc))
            
            if possible_moves:
                # Выбираем случайный допустимый ход
                dr, dc = random.choice(possible_moves)
                self.move_tile(empty_row + dr, empty_col + dc)
    
    def move_tile(self, row: int, col: int) -> bool:
        """
        Перемещение плитки на пустое место
        
        Args:
            row: строка перемещаемой плитки
            col: столбец перемещаемой плитки
            
        Returns:
            bool: True если ход выполнен, False если ход невозможен
        """
        empty_row, empty_col = self.empty_pos
        
        # Проверяем, что плитка соседствует с пустой клеткой
        if (abs(row - empty_row) + abs(col - empty_col)) != 1:
            return False
        
        # Меняем местами плитку и пустую клетку
        self.board[empty_row][empty_col] = self.board[row][col]
        self.board[row][col] = 0
        self.empty_pos = (row, col)
        return True
    
    def is_solved(self) -> bool:
        """Проверка, решена ли головоломка"""
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    if self.board[i][j] != 0:
                        return False
                else:
                    if self.board[i][j] != i * self.size + j + 1:
                        return False
        return True
    
    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """Получение списка возможных ходов"""
        empty_row, empty_col = self.empty_pos
        possible_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                possible_moves.append((new_row, new_col))
        
        return possible_moves
    
    def display_board(self):
        """Отображение игрового поля"""
        print("\n" + "="*25)
        print("   ГОЛОВОЛОМКА '15'")
        print("="*25)
        
        for i in range(self.size):
            print("+----" * self.size + "+")
            print("|", end="")
            for j in range(self.size):
                if self.board[i][j] == 0:
                    print("    |", end="")
                else:
                    print(f" {self.board[i][j]:2d} |", end="")
            print()
        print("+----" * self.size + "+")
        
        # Показываем возможные ходы
        possible_moves = self.get_possible_moves()
        print("\nВозможные ходы (координаты строки и столбца):")
        for row, col in possible_moves:
            print(f"  ({row}, {col}) - плитка {self.board[row][col]}")
    
    def get_input_coordinates(self) -> Optional[Tuple[int, int]]:
        """Получение координат от пользователя"""
        try:
            print("\nВведите координаты плитки для перемещения")
            row = int(input("Строка (0-3): "))
            col = int(input("Столбец (0-3): "))
            
            if 0 <= row < self.size and 0 <= col < self.size:
                return (row, col)
            else:
                print("Координаты должны быть от 0 до 3!")
                return None
        except ValueError:
            print("Пожалуйста, введите числа!")
            return None

def main():
    """Основная функция игры"""
    game = Puzzle15()
    moves_count = 0
    
    print("Добро пожаловать в головоломку '15'!")
    print("Цель: упорядочить числа от 1 до 15 по возрастанию.")
    print("Пустая клетка должна быть в правом нижнем углу.")
    print("Для выхода введите 'q' вместо координат.")
    
    while True:
        game.display_board()
        
        if game.is_solved():
            print(f"\n Поздравляем! Вы решили головоломку за {moves_count} ходов!")
            break
        
        # Получаем координаты от пользователя
        coords = game.get_input_coordinates()
        if coords is None:
            continue
        
        row, col = coords
        
        # Проверяем возможность хода и выполняем его
        if game.move_tile(row, col):
            moves_count += 1
            print(f"Ход выполнен! Всего ходов: {moves_count}")
        else:
            print("Невозможно переместить эту плитку! Выберите плитку рядом с пустой клеткой.")
        
        print("\n" + "-"*40)

if __name__ == "__main__":
    main()