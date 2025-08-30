"""
File Organizer - Automatically organize downloaded files by type
"""
from pathlib import Path
import util.file_handling as fh

def main():
    """Main function for file organizer."""
    print("File Organizer - Ready to organize your downloads!")
    # TODO: file organization logic here
    
    
    
    fh.copy_file("Test/texto1.txt", "Test/texto3", overwrite=True)

if __name__ == "__main__":
    main()
