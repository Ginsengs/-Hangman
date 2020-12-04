symbols = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
print(f'''---------
| {symbols[0]} {symbols[1]} {symbols[2]} |
| {symbols[3]} {symbols[4]} {symbols[5]} |
| {symbols[6]} {symbols[7]} {symbols[8]} |
---------''')

n = -1
while True:
    straights = [symbols[:3], symbols[3:6], symbols[6:], symbols[0:9:3], symbols[1:9:3], symbols[2:9:3], symbols[0:9:4],
                 symbols[2:7:2]]
    if ['X', 'X', 'X'] in straights:
        print('X wins')
        break
    elif ['O', 'O', 'O'] in straights:
        print('O wins')
        break
    elif '_' not in symbols:
        print("Draw")
        break

    print('Enter the coordinates: ')
    coord = input()

    if coord.replace(' ', '').isalpha():
        print("You should enter numbers!")
        pass

    else:
        coord_col, coord_row = coord.split()
        coord_x = int(coord_col) - 1
        coord_y = 3 - int(coord_row)
        index = (coord_y * 3) + coord_x

        if index <= 8:

            if 1 <= int(coord_col) <= 3 and 1 <= int(coord_row) <= 3:

                if symbols[index] != '_':
                    print("This cell is occupied! Choose another one!")
                    pass

                else:
                    try:
                        for j in range(len(symbols)):
                            n += 1
                            symbols = [i for i in symbols]
                            X_O = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
                            symbols[index] = X_O[n]

                            print('---------')
                            print('|', symbols[0], symbols[1], symbols[2], '|')
                            print('|', symbols[3], symbols[4], symbols[5], '|')
                            print('|', symbols[6], symbols[7], symbols[8], '|')
                            print('---------')
                            break
                    except IndexError:
                        print('')
                    continue

            else:
                print("Coordinates should be from 1 to 3!")
                pass

        else:
            print("Coordinates should be from 1 to 3!")
            pass
