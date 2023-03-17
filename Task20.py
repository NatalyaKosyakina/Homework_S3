# Задача 20 (Scrabble)

letter_cost = ['A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'.split(', '), 
    'D, G, Д, К, Л, М, П, У'.split(', '), 'B, C, M, P, Б, Г, Ё, Ь, Я'.split(', '),
    'F, H, V, W, Y, Й, Ы'.split(', '), 'K, Ж, З, Х, Ц, Ч'.split(', '), 'J, X, Ш, Э, Ю'.split(', '), 
    'Q, Z, Ф, Щ, Ъ'.split(', ')]

word = input("Введите слово: ").upper()

word_cost = 0
for letter in range(len(word)) :
    for i in range(len(letter_cost)-2) :
        if word[letter] in letter_cost[i]:
            word_cost += i + 1
    if word[letter] in letter_cost[-2]:
        word_cost += 8
    if word[letter] in letter_cost[-1]:
        word_cost += 10

print(word_cost)

