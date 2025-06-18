def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"\nContents of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file to read: ")
    read_file(file_name)