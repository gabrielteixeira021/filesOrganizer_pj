"""
File Organizer - Automatically organize downloaded files by type
"""
from pathlib import Path

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

def writing_file(file_path, content):
    
    # a = Append 
    # writing to a file
    try:
        f = open(file_path, "a")
        f.write(content)
    except Exception as e:
        e.with_traceback()
        print("An error occurred while writing to the file.")
    finally:
        f.close()
        
    return;

def learning_file_handler(file_path):
    
    # w = Write 
    # x = Create
       
        
    return;
    
def main():
    """Main function for file organizer."""
    print("File Organizer - Ready to organize your downloads!")
    # TODO: Add your file organization logic here
    learning_file_handler("Test/texto1.txt")
    


if __name__ == "__main__":
    main()
