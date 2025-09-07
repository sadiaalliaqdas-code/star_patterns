n = 5
for i in range(1, n+1):   # outer loop → controls rows
    for j in range(i):    # inner loop → controls stars in each row
        print("*", end="")
    print()
