freecells = 9
field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
message = ''


def round_(isCross):
    pos = {'x': -1,
           'y': -1}

    tmp = input('Введите координаты в формате X Y: ')
    x, y = tmp.split()
    pos['x'], pos['y'] = TryParse(x, 'X'), TryParse(y, 'Y')

    symb = 'x' if isCross else 'o'
    field[pos['x']][pos['y']] = symb

    global freecells
    freecells -= 1


def TryParse(num, cat):
    try:
        num = int(num)
        if num > 2:
            raise ValueError
        else:
            return num
    except ValueError:
        num = input(f'Значение {cat} неверно. Введите снова: ')
        return TryParse(num, cat)


def hasLine():
    if field[0] == [field[0][0]] * 3 != ['-'] * 3:
        return True
    elif field[1] == [field[1][0]] * 3 != ['-'] * 3:
        return True
    elif field[2] == [field[2][0]] * 3 != ['-'] * 3:
        return True
    elif field[0][0] == field[1][0] == field[2][0] != '-':
        return True
    elif field[0][1] == field[1][1] == field[2][1] != '-':
        return True
    elif field[0][2] == field[1][2] == field[2][2] != '-':
        return True
    elif field[0][0] == field[1][1] == field[2][2] != '-':
        return True
    elif field[0][2] == field[1][1] == field[2][0] != '-':
        return True

    return False


def isVictory():
    global freecells, message
    if hasLine():
        freecells = 0
        message = 'Победа игрока'
        return True

    return False


def printField():
    print('  0 1 2 x')
    for i in range(3):
        print(f'{i} {field[0][i]} {field[1][i]} {field[2][i]}')
    print('y', end='\n\n')


def play():
    isCross = True
    printField()
    while(freecells > 0):
        print(f'Ход игрока "{"x" if isCross else "o"}"')
        round_(isCross)
        printField()
        if isVictory():
            print(f'{message} "{"x" if isCross else "o"}"')
        isCross = not isCross



if __name__ == "__main__":
    play()
    input()