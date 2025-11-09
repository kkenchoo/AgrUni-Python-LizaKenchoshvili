a = float(input("სამკუთხედის პირველი გვერდი: "))
b = float(input("სამკუთხედის მეორე გვერდი: "))
c = float(input("სამკუთხედის მესამე გვერდი: "))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    semiperimeter = perimeter / 2
    area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)) ** 0.5

    print(f"\nსამკუთხედის ფართობი არის: {area:.2f}")
    print(f"სამკუთხედის პერიმეტრი არის: {perimeter}")
else:
    print("სამკუთხედი არ იკვრება")