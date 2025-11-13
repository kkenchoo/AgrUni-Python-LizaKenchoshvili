text1 = list(input('შეიყვანე პირველი ტექსტი: ').lower())
text2 = list(input('შეიყვანე მეორე ტექსტი: ').lower())

if sorted(text1) == sorted(text2):
    print('YES')
else:
    print('NO')