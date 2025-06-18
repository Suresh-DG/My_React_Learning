def validate_binary(binary): 
    return all(char in '01' for char in binary)

def binary_division(bin1, bin2): 
    dec1 = int(bin1, 2) 
    dec2 = int(bin2, 2) 
    if dec2 == 0: 
        return "Division by zero error" 
    result = dec1 // dec2 
    return bin(result)[2:]

def main(): 
    bin1 = input("Enter the first binary number: ") 
    bin2 = input("Enter the second binary number: ") 

    if not (validate_binary(bin1) and validate_binary(bin2)): 
        print("Invalid binary input.") 
        return

    result = binary_division(bin1, bin2)
    print(f"Result (Division): {result}")

if __name__ == "__main__": 
    main()
