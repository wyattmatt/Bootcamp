def check_input_validity():
    try:
        # Code 1: Input validation check for odd number sum
        x = int(input("Input Number-1: "))
        y = int(input("Input Number-2: "))
        if x >= y:
            raise ValueError("Number-1 should be smaller than Number-2.")
        
        # Code 2: Input check for star pattern
        n = int(input("Input Number: "))
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        
        # Code 3: Prime number check input validation
        x = int(input("Input Number-1: "))
        y = int(input("Input Number-2: "))
        if x <= 0 or y <= 0:
            raise ValueError("Both numbers must be positive integers.")

        # Code 4: Sentence input check for reversing
        x = input("Sentence: ")
        if not x:
            raise ValueError("Sentence cannot be empty.")
        
        # Code 5: Star pattern with spaces check
        n = int(input("Input Number: "))
        if n <= 0:
            raise ValueError("Number must be a positive integer.")
        
        # Code 6: Repeated numbers input check
        x = int(input("Total Data: "))
        if x <= 0:
            raise ValueError("Total data must be a positive integer.")
        
        # Code 7: Number countdown input check
        x = int(input("Input Number: "))
        if x <= 0:
            raise ValueError("Input must be a positive integer.")
        
        # Code 8: Vowel counting input check
        x = input("Sentence: ")
        if not x:
            raise ValueError("Sentence cannot be empty.")
        
        # Code 9: Average input check
        x = int(input("Total Data: "))
        if x <= 0:
            raise ValueError("Total data must be a positive integer.")
        
        # Code 10: Remove duplicates input check
        y = int(input("Total Data: "))
        if y <= 0:
            raise ValueError("Total data must be a positive integer.")
        
        print("Check passed for all inputs.")

    except Exception as e:
        print(f"Input validation failed: {e}")

check_input_validity()