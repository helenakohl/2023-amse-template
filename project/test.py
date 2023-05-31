import os

def file_exists(file_path):
    return os.path.exists(file_path)

# Example usage
file_path = "../data/accidents.sqlite"
if file_exists(file_path):
    print(f"Test successfull. File found under the following path: {file_path}")
else:
    print("Test not succesfull.The file does not exist.")
