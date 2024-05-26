# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.
def nod(a, b):
    if a*b == 0:
        return a+b
    if a < b:
        return nod(a, b%a)
    else:
        return nod(a%b, b)

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

print(f'Наибольшей общий делитель {a} и {b} равен {nod(a,b)}')

# Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен угадать его.
# После ввода пользователем числа программа сообщает, сколько цифр числа угадано (быки) и сколько цифр угадано
# и стоит на нужном месте (коровы). После отгадывания числа на экран необходимо вывести количество сделанных
# пользователем попыток. В программе необходимо использовать рекурсию.

def bull_and_cow(list_1, n):
    bulls = 0
    cows = 0
    list_2 = input("Введите четырёхзначное число ")
    for i in range(4):
        if list_2[i] in list_1:
            bulls += 1
        if list_2[i] == list_1[i]:
            cows += 1
    print(f'{bulls} быка и  {cows}  коровы')
    if bulls == 4:
        print(f'Вы победили! Количество попыток {n}')
    else:
        bull_and_cow(list_1, n+1)

import random
a = '0123456789'
list_1 = random.choice(a)
for i in range(3):
    a = ''.join(a.split(list_1[i]))
    list_1 += random.choice(a)
bull_and_cow(list_1, 1)

# Дана шахматная доска размером 8×8 и шахматный конь. Программа должна запросить у пользователя координаты
# клетки поля и поставить туда коня. Задача программы найти и вывести путь коня, при котором он обойдет все
# клетки доски, становясь в каждую клетку только один раз. (Так как процесс отыскания пути для разных начальных
# клеток может затянуться, то рекомендуется сначала опробовать задачу на поле размером 6×6). В программе
# необходимо использовать рекурсию.

chessboard = [[0] * 8 for _ in range(8)]
moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
def move_horse(x, y, board, n):
    board[x][y] = n
    if n <= 64:
        for i, j in moves:
            x_i = x + i
            y_j = y + j
            if 0 <= x_i <= 7 and 0 <= y_j <= 7:
                if board[x_i][y_j] == 0:
                    move_horse(x_i, y_j, board, n+1)
    return board

x_1 = int(input('Введите координату коня по горизонтали ')) - 1
y_1 = int(input('Введите координату коня по вертикали ')) - 1
arr = move_horse(x_1, y_1, chessboard, 1)
print('Матрица ходов: ')
print("\n".join(map(str, arr)))

# Написать игру «Пятнашки»
import random

empty_cell = ' x '
win_shield = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '],
              ['13 ', '14 ', '15 ', empty_cell]]
first_list = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', '10 ', '11 ', '12 ', '13 ', '14 ', '15 ',
              empty_cell]
random.shuffle(first_list)

game_shield = []
for i in range(len(first_list) // 4):
    game_shield.append(first_list[i * 4:i * 4 + 4])
if len(first_list) % 4 > 0:
    game_shield.append(first_list[-1 * (len(first_list) % 4):])

def new_shield():
    if game_shield == win_shield:
        print('Победа!')
    print('\n', game_shield[0], '\n', game_shield[1], '\n', game_shield[2], '\n', game_shield[3], '\n')
    for x in range(0, len(game_shield)):
        for y in range(0, len(game_shield[x])):
            if game_shield[x][y] == empty_cell:
                a = x
                b = y
                break
    hod = str(input('Ваш ход: '))
    try:
        if hod != 'вверх' and hod != 'вниз' and hod != 'вправо' and hod != 'влево':
            raise ValueError('Неправильный ход')
    except ValueError:
        print('Неправильный ход')
        new_shield()
    return new_hod(hod, a, b)

def new_hod(hod, a, b):
    if hod == 'вверх':
        try:
            if a - 1 < 0:
                raise TypeError()
        except TypeError:
            print('Ход вне поля!')
            new_shield()

        game_shield[a][b], game_shield[a - 1][b] = game_shield[a - 1][b], game_shield[a][b]
        new_shield()

    if hod == 'вниз':
        try:
            if a + 1 > 3:
                raise TypeError()
        except TypeError:
            print('Ход вне поля!')
            new_shield()

        game_shield[a][b], game_shield[a + 1][b] = game_shield[a + 1][b], game_shield[a][b]
        new_shield()

    if hod == 'влево':
        try:
            if b - 1 < 0:
                raise TypeError()
        except TypeError:
            print('Ход вне поля!')
            new_shield()

        game_shield[a][b], game_shield[a][b - 1] = game_shield[a][b - 1], game_shield[a][b]
        new_shield()

    if hod == 'вправо':
        try:
            if b + 1 > 3:
                raise TypeError()
        except TypeError:
            print('Ход вне поля!')
            new_shield()

        game_shield[a][b], game_shield[a][b + 1] = game_shield[a][b + 1], game_shield[a][b]
        new_shield()

new_shield()