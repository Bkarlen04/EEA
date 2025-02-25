def extended_euclidean(a, b):
    table = []
    
    # Initial values
    orig_a = a
    orig_b = b
    setup = 2

    while b:
        if (setup == 2):
            r = a
            q, b = " ", b
            x0 = x1 = 1
            y0 = y1 = 0
        elif (setup == 1):
            r = b
            q, b = " ", b
            x0 = 0
            y0 = 1
        else:
            r = a % b
            q = a // b
            a = b
            b = r
            x0, x1 = x1 - q * x0, x0
            y0, y1 = y1 - q * y0, y0

        setup -= 1

        if (x0 == orig_b or x0 == -orig_b):
            x0 = " "
        if (y0 == -orig_a or y0 == orig_a):
            y0 = " "
        
        # Append current step to table
        table.append([r, q, x0, y0])
    
    # If gcd is not 1, no inverse exists
    if a != 1:
        return None, table
    
    # Ensure positive modular inverse
    if (y1 < 0):
        y1 += orig_a
    return y1, table
17
def print_table(table):
    print(f"{'i':<6}{'r':<6}{'q':<6}{'x':<8}{'y':<8}")
    print("-" * 34)
    for i, row in enumerate(table):
        print(f"{i-1:<6}{row[0]:<6}{row[1]:<6}{row[2]:<8}{row[3]:<8}")
    print("-" * 34)


a = int(input("Enter value a: "))
b = int(input("Enter value b: "))


inverse, table = extended_euclidean(a, b)

if inverse is not None:
    print_table(table)
    print(f"\nMultiplicative Inverse of {b} mod {a} is: {inverse}")
else:
    print("No modular inverse exists.")
