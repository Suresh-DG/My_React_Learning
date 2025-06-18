def binary_to_decimal(binary):
    return int(binary, 2)
def validate_input(value):
    return all(char in '01' for char in value)
def main():
    binary = input("Enter a Binary Number:")
    if validate_input(binary):
        print("Decimal : ", binary_to_decimal(binary))
    else:
        print("Invalid Input...")
if __name__ == "__main__":
    main()