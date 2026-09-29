def get_integer():
    try:
        number = int(input("Enter a whole number: "))
        return number
    except ValueError:
        return "Invalid input"


print(get_integer())