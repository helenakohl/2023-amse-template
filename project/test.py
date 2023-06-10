import os

def file_exists(file_path):
    return os.path.exists(file_path)

# Usage

file_path1 = "../project/accidents.sqlite"
if file_exists(file_path1):
    print(f"Test successfull. File found under the following path: {file_path1}")
else:
    print("Test not succesfull.The file does not exist.")

file_path2 = "../project/traffic_june.sqlite"
if file_exists(file_path2):
    print(f"Test successfull. File found under the following path: {file_path2}")
else:
    print("Test not succesfull.The file does not exist.")