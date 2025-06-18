def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("This is the initial content of the file.\n")
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file to create: ")
    create_file(file_name)
