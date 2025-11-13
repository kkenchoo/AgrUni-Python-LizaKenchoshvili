while True:
    action = input('Enter action (e/d): ').lower()

    if action != 'e' and action != 'd':
        print('Enter valid action')

    else:
        text = input('Enter text: ')
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        rows = [row1, row2, row3]

        if action == 'e':
            result = ''
            for char in text:
                found = False
                for row in rows:
                    if char in row:
                        index = row.index(char)
                        if index == len(row) - 1:
                            result += row[0]
                        else:
                            result += row[index + 1]
                        found = True
                        break

                if not found:
                    result += char
            print(result)

        elif action == 'd':
            result = ''
            for char in text:
                found = False
                for row in rows:
                    if char in row:
                        index = row.index(char)
                        if index == 0:
                            result += row[-1]
                        else:
                            result += row[index - 1]
                        found = True
                        break
                if not found:
                    result += char
            print(result)
        break

