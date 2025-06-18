def hexadecimal_to_decimal (hexadecimal):
    return int(hexadecimal, 16)
def validate_input(value):
    return all(char in '0123456789ABCDEFabcdef' for char in value)
def main():
    hexadecimal = input("Enter a hexadecimal number : ")
    if validate_input(hexadecimal):
        print("Decimal : ", hexadecimal_to_decimal(hexadecimal))
    else:
        print("Invalid Input")
if __name__ == "__main__":
    main()
