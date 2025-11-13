word = 'azcbobobegghakl'

longest = current = word[0]

for i in range(1, len(word)):
    if word[i] >= word[i-1]:
        current += word[i]
        if len(current) > len(longest):
            longest = current
    else:
        current = word[i]

print(longest)
