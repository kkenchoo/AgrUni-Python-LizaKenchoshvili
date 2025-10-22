while True:
    usernum = int(input('შეიყვანეთ ნატურალური რიცხვი (არაუმეტეს 100): '))

    if usernum>100 or usernum < 0:
        print('შეყვანილი რიცხვი არი არის ვალიდური')
    else:
        fibonacci_list = [0, 1]

        while len(fibonacci_list) < usernum:
            next_num = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_num)

        print(fibonacci_list[:usernum])