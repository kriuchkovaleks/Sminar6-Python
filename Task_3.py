

# пара-ра-ра-рам рам-пам-папам па-ра-па-пам


phrase = 'парара-ра-рам рам-пам-папам па-ра-па-пам'

print(phrase)

working_phrase = phrase.split()


def count_vowels(col):
    count = 0
    for i in col:
        if i == 'а':
            count += 1
    return count


result_list = list(map(count_vowels, working_phrase))

sum = 0
for i in result_list:
    sum = sum + int(i)

print(sum)

if sum % i == 0:
    print('парам пам-пам')
else:
    print('пам-парам')
