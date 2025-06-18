def decimal_to_binary(decimal):
    return bin(decimal)[2:]
def validate_input(value):
    return value.isdigit()
def main():
    decimal = input("enter a decimal:")
    if validate_input(decimal):
        print("Binary: ", decimal_to_binary(int(decimal)))
    else:
        print("Invalid Input...")
if __name__ == "__main__":
    main()