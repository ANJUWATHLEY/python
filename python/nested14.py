a = 18
if a < 0:
    print("negative")
elif a > 0:
    if a <= 10:
        print("number is between 1-10")
    elif a > 10 and a <= 20:
        print("11-20")
    else:
        print("greater than 20")
else:
    print("number is zero")
