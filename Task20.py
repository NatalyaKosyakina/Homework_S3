# Задача 20 (Scrabble)

letter_cost = {'value_1': 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'.split(', '), 
    'value_2': 'D, G, Д, К, Л, М, П, У'.split(', '), 'value_3': 'B, C, M, P, Б, Г, Ё, Ь, Я'.split(', '),
    'value_4': 'F, H, V, W, Y, Й, Ы'.split(', '), 'value_5': 'K, Ж, З, Х, Ц, Ч', 'value_8': 'J, X, Ш, Э, Ю'.split(', '), 'value_10': 'Q, Z, Ф, Щ, Ъ'.split(', ')}


print(letter_cost)

word = input("Введите слово: ").upper()

word_cost = 0
for letter in range(len(word)) :
    if word[letter] in letter_cost['value_1']:
        word_cost += 1
    elif word[letter] in letter_cost['value_2']:
        word_cost += 2
    elif word[letter] in letter_cost['value_3']:
        word_cost += 3
    elif word[letter] in letter_cost['value_4']:
        word_cost += 4
    elif word[letter] in letter_cost['value_5']:
        word_cost += 5
    elif word[letter] in letter_cost['value_8']:
        word_cost += 8
    else :
        word_cost += 10 

print(word_cost)

