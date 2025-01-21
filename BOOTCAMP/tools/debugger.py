def debug_code():
    try:
        # Code 1: Sum of odd numbers
        x = int(input("Input Number-1: "))
        y = int(input("Input Number-2: "))
        n = [i for i in range(x, y) if i % 2 != 0]
        result = sum(n)
        print(result)

        # Code 2: Star pattern
        n = int(input("Input Number: "))
        for i in range(1, n + 1):
            print('*' * i)

        # Code 3: Prime number check
        x = int(input("Input Number-1: "))
        y = int(input("Input Number-2: "))
        n = [i for i in range(x, y) if all(i % j != 0 for j in range(2, i))]
        print(n)

        # Code 4: Reverse words in sentence
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

        # Code 5: Star pattern with spaces
        n = int(input("Input Number: "))
        for i in range(n):
            for j in range(n):
                if j < n - i - 1:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

        # Code 6: Find repeated numbers
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

        # Code 7: Number countdown pattern
        x = int(input("Input Number: "))
        a = 1
        while a <= x:
            b = a
            while b > 0:
                print(b, end=" ")
                b -= 1
            print()
            a += 1

        # Code 8: Count vowels in a string
        x = input("Sentence: ")
        x = x.lower()
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

        # Code 9: Average of numbers
        x = int(input("Total Data: "))
        y = []
        for i in range(x):
            z = int(input(f"Number-{i+1}: "))
            y.append(z)
        total = sum(y)
        result = total / len(y)
        print(result)

        # Code 10: Remove duplicates from list
        def removes(x):
            return list(dict.fromkeys(x))
        y = int(input("Total Data: "))
        n = []
        for i in range(y):
            z = int(input(f"Number-{i+1}: "))
            n.append(z)
        print(removes(n))

    except Exception as e:
        print(f"An error occurred: {e}")

debug_code()