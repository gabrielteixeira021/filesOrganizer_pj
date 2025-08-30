# Code by Gabriel Silva
# github.com/gabrielsilvadev

import os


def reading_file(file_path):
    
    # r = Read
    # reading a file
    try:
        f = open(file_path)
        print(f.read())
    except FileNotFoundError as e:
        print("File not found. Please check the file path.")
    finally:
        f.close()
    
    return;

def get_file_content(file_path):
    
    with open(file_path, "r") as f:
        content = f.read()
        
    return content

def append_file(file_path, content):
    
    # a = Append 
    # appending to a file
    try:
        f = open(file_path, "a")
        f.write(content)
    except Exception as e:
        e.with_traceback()
        print("An error occurred while writing to the file.")
    finally:
        f.close()
        
    return;

def write_file(file_path, content):
    
    # w = Write (Overwrite or Create new file)
    try:
        f = open(file_path, "w")
        f.write(content)
        print("File written successfully.")

    except Exception as e:
        e.with_traceback()
        print("An error occurred while writing to the file.")
    finally: 
        f.close()

def create_file(file_path):
    
    # x = Create
    if not os.path.exists(file_path):
        f = open(file_path, "x")
        print("File created successfully.")
        f.close()
    else:
        print("File already exists.")

def delete_file(file_path):
    
    # Deleting a file
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")
    
def copy_file(src, dest, overwrite=True):  
    
    dest += " copy.txt"  # Adding 'copy' to the destination file name to avoid overwriting original file unintentionally
    
    try:
        # Copying file content from src to dest
        text = "\n" + get_file_content(src) 
        if overwrite:   # Overwrite/create the file if overwrite is True
            write_file(dest, text)
        else: # Append to the file if it exists and overwrite is False
            append_file(dest, text)
    except Exception as e:
        print("An error occurred while copying the file.")
        print(f"Error details: {e}")