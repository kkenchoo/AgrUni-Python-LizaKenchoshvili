while True:
    year = input('შეიყვანეთ წელი: ')
    if not year.isdigit():
        print('შეიყვანეთ რიცხვი!')

    elif int(year) <= 0:
        print('წელი უნდა იყოს დადებითი!')

    else:
        year = int(year)

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print('ნაკიანი წელი!')
        else:
            print('არ არის ნაკიანი წელი!')
        break

