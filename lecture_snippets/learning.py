f1, f2 = 1, 1
while f2 < 1000:
    print(f2)
    next_f2 = f1 + f2
    next_f1 = f2
    f1, f2 = next_f1, next_f2