while True:
    usernum = int(input('შეიყვანეთ ნატურალური რიცხვი (არაუმეტეს 1000): '))
    if usernum > 1000 or usernum < 0:
        print('შეყვანილი რიცხვი არი არის ვალიდური')
    else:
        divisors = []
        for i in range(1,usernum+1):
            if usernum % i == 0:
                divisors.append(i)

        print(divisors)
        break

