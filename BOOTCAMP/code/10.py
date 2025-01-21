def removes(x):
    return list(dict.fromkeys(x))
y = int(input("Total Data: "))
n = []
for i in range(y):
    z = int(input(f"Number-{i+1}: "))
    n.append(z)
print(removes(n))