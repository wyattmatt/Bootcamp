x = int(input("Total Data: "))
y = []
for i in range(x):
    z = int(input(f"Number-{i+1}: "))
    y.append(z)
total = 0
for j in y:
    total += j
divided = len(y)
result = total / divided
print(result)