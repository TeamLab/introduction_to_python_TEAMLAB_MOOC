sentence = "I love you"
reverse_sentence = ''
for char in sentence:
    print(char, "=====", reverse_sentence, "=====",)
    reverse_sentence = char + reverse_sentence
    print(reverse_sentence)
print (reverse_sentence)
