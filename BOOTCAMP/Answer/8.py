x = input("Sentence: ")
x.lower()
vowels = ["a", "i", "u", "e", "o"]
result = []
for i in range(len(x)):
    if x[i] in vowels:
        result.append(x[i])
j = len(result)
if j > 0:
    print(j)
else:
    print("There are no vowels in this string")