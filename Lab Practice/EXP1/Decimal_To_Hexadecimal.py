def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()
def validate_input(value):
    return value.isdigit()
def main():
    decimal = input("Enter a Decimal Number: ")
    if validate_input(decimal):
        print("hexadecimal : ", decimal_to_hexadecimal(int(decimal)))
    else:
        print("Invalid Input...")
if __name__ == "__main__":
    main()