x = input("Sentence: ")
sentence = []
word = ""
for i in x:
    if i == ".":
        sentence.append(word)
        word = ""
    else:
        word += i
if word:
    sentence.append(word)
inverted = sentence[::-1]
result = ".".join(inverted)
print(result)