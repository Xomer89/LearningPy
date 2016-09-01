try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That's not a number")

for value in(None, "Hi!", 7):
    try:
        print("Turning ", value, "-->", "into a number")
        print(float(value))
    except TypeError:
        print("I can turn into float only strings and numbers")
    except ValueError:
        print("I can turn into float only strings consisting from numbers")
    else:
        print("You've input ", value)
