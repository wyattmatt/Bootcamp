x = int(input("Input Number-1: "))
y = int(input("Input Number-2: "))
n = []
for i in range(x, y):
    if i <= 1:
        continue
    if i == 2:
        n.append(i)
        continue
    if i % 2 == 0:
        continue
    prime = True
    j = 3
    while j * j <= i:
        if i % j == 0:
            prime = False
            break
        j += 2
    if prime:
        n.append(i)
print(n)