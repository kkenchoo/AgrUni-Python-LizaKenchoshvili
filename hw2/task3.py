import random

rand_list = random.choices(range(1, 5), k = 5)
new_list = []

for i in rand_list:
    new_list.extend([i] * i)

print(rand_list)
print(new_list)



