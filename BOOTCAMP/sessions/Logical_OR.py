x = [1, 1, 0, 0]
y = [1, 0, 1, 0]
c = [0, 0, 0, 0]
for i in range(len(x)):
    if x[i] + y[i] >= 1:
        c[i] = 1
        print(c[i], end=" ")
    else:
        c[i] = 0
        print(c[i], end=" ")