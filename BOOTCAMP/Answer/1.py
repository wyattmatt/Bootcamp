x = int(input("Input Number-1: "))
y = int(input("Input Number-2: "))
n = []
for i in range(x, y):
    if i % 2 != 0:
        n.append(i)
result = 0
for j in n:
    result += j
print(result)