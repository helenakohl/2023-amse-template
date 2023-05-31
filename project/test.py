import os
import sqlite3

def check_db_file():
    output = ["sqlite:///../data/accidents.sqlite"]
    for file in output:
        if os.path.exists(file):
            print(f"The database file '{file}' exists.")
        else:
            print(f"The database file '{file}' does not exist.")

check_db_file()