x = int(input("Total Data: "))
n = []
for i in range(x):
    y = int(input(f"Number-{i+1}: "))
    n.append(y)
m = []
for j in n:
    if n.count(j) > 1 and j not in m:
        m.append(j)
print(m)