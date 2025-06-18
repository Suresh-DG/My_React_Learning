import os

def delete_file(file_name):
    """Delete a file from the file system."""
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        else:
            print(f"Error: File '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file to delete: ")
    delete_file(file_name)
