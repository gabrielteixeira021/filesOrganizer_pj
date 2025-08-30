# Code by Gabriel Teixeira C. S.
# github.com/gabrielteixeira021

import os

class FileHandling:

    @staticmethod
    def reading_file(file_path):
        
        # r = Read
        # reading a file
        with open(file_path) as f:
            print(f.read())

        return

    @staticmethod
    def get_file_content(file_path) -> str:
        
        with open(file_path, "r") as f:
            content = f.read()
            
        return content

    @staticmethod
    def append_file(file_path, content):
        
        # a = Append 
        # appending to a file
        with open(file_path, "a") as f:
            f.write(content)

    @staticmethod
    def write_file(file_path, content):
        
        # w = Write (Overwrite or Create new file)
        with open(file_path, "w") as f:
            f.write(content)
            print("File written successfully.")
        
    @staticmethod
    def create_file(file_path):
        
        # x = Create
        if not os.path.exists(file_path):
            with open(file_path, "x") as f:
                print("File created successfully.")
        else:
            print("File already exists.")

    @staticmethod
    def delete_file(file_path):
        
        # Deleting a file
        if os.path.exists(file_path):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("File does not exist.")
        
    @staticmethod
    def copy_file(src, dest, overwrite=True):  
        
        dest += " copy.txt"  # Adding 'copy' to the destination file name to avoid overwriting original file unintentionally
        
        try:
            # Copying file content from src to dest
            text = "\n" + FileHandling.get_file_content(src) 
            if overwrite:   # Overwrite/create the file if overwrite is True
                FileHandling.write_file(dest, text)
            else: # Append to the file if it exists and overwrite is False
                FileHandling.append_file(dest, text)
        except Exception as e:
            print("An error occurred while copying the file.")
            print(f"Error details: {e}")