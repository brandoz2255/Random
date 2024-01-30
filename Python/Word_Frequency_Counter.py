#counts the word frequency duhh

Input_1 = input ('Enter paragraph of text: ')

words = Input_1.split()
words = [word.strip('.,!?').lower() for word in words]

word_frequency = {} 

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word Frequency:")
for word, count in word_frequency.items():
    print(f'"{word}": {count} times')