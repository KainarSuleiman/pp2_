
file = open('text.txt', 'r')
text = file.read()
file.close()

text = text.replace('.', '').replace(',', '').lower()
words = text.split()

max_word = words[0]
max_count = words.count(words[0])
for i in range(1, len(words), 1):
    current_word = words[i]  # Текущее слово
    current_count = words.count(current_word)  # Кол-во повторений текущего слова
    if max_count < current_count:
        max_word = current_word
        max_count = current_count
print(max_word, max_count)






word = 'ABABA'
flag = True
for i in range(0, len(word) // 2, 1):
    if word[i] != word[-i - 1]:
        flag = False
        break
print(flag)