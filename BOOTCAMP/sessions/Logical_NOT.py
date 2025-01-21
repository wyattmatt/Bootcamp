x = [1, 1, 0, 0]
c = [0, 0, 0, 0]
for i in range(len(x)):
    if x[i] == 0:
        c[i] = 1
        print(c[i], end=" ")
    else:
        c[i] = 0
        print(c[i], end=" ")