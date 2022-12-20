# Итоговый проект модуля B "Крестики нолики"
print('Добро пожаловать в игру крестики - нолики')
print('Введите координаты в форме столбец/строка')
print('             "a1, b2, c3"')
num = '  a b c'
num_1 = '1 2 3'
field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def window(f):
    print(num)
    for row, i in zip(f, num_1.split()):
        print(f'{i} {" ".join(str(j) for j in row)}')


coordinates = {'a1': '00', 'a2': '10', 'a3': '20', 'b1': '01', 'b2': '11', 'b3': '21',
               'c1': '02', 'c2': '12', 'c3': '22'}
stop_list = []
def game_input():
    global stop_list

    while True:
        # print(print(f'Ходит игрок {player} '))
        cord = input(f'Ходит игрок {player}: ')

        if cord not in coordinates:
            print("Введите координаты в диапазоне поля")
            continue

        if cord in stop_list:
            print('Ячейка занята!')
            continue
        else:
            stop_list.append(cord)
        i = coordinates[cord]
        x, y = map(int, i)
        break

    return x, y


def winner(func, player):
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_comb:
        win_list = []
        for c in cord:
            win_list.append(field[c[0]][c[1]])
        if win_list == ["X", "X", "X"]:
            print(window(field))
            print("!!!Выиграл X!!!")

            return True
        if win_list == ["0", "0", "0"]:
            print(window(field))
            print("!!!Выиграл 0!!!")
            return True
    return False


count = 0
while True:

    if count % 2 == 0:
        player = 'X'
    else:
        player = '0'
    if winner(field, player):
        break
    if count == 9:
        print(window(field))
        print('Ничья')
        break
    window(field)
    x,y = game_input()
    field[x][y]=player
    count += 1