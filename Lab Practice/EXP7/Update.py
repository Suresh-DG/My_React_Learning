def update_file(file_name):
    try:
        with open(file_name, 'a') as file:
            new_content = input("Enter content to add to the file: ")
            file.write(new_content + "\n")
            print(f"Content added to '{file_name}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error updating file: {e}")
        
if __name__ == "__main__":
    file_name = input("Enter the name of the file to update: ")
    update_file(file_name)
