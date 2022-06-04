while True:
    try:
        X = int(input("Please type an integer number bigger than 1 and smaller than 2000: "))
    except:
        print("Please make sure to type and integer number.\n")
    else:
        break
while True:
    try:
        Y = int(input(f"\nNow type another integer number bigger than {X} and smaller or equal to 2000: "))
    except:
        print("Please make sure to type and integer number.")
    else:
        break
for c in range(X, Y + 1):
    if c % 3 == 0 and c % 5 == 0:
        print("FizzBuzz")
    elif c % 3 == 0 and c % 5 != 0:
        print("Fizz")
    elif c % 3 != 0  and c % 5 == 0:
        print("Buzz")
    else:
        print(c)
print("Well done!")
