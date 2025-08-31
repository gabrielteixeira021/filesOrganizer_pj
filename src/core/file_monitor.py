from ast import Dict
import os
from pathlib import Path
import time


class fileMonitor:
    
    DEFAULT_POOLING_INTERVAL = 10 # in seconds
    
    def __init__(self, watch_directory=str):
        self.watch_directory = Path(watch_directory)
        self.initial_state = {}
    
    def get_current_files(self) -> Dict[str, float]:
        """Returns a set of current files in the directory."""
        if not self.watch_directory.exists():
            raise ValueError(f"Directory {self.watch_directory} does not exist.")

        return {
            entry.name: entry.stat().st_mtime
            for entry in os.scandir(self.watch_directory)
            if entry.is_file()
        }
        
    def check_changes(self, before: Dict[str, float], after: Dict[str, float]):
        """Compares two dictionaries of files and returns added, removed, and modified files."""
        
        
        
    def start_monitoring(self, file_path=str):
        print(f"Started monitoring {file_path} for changes.")

        # Dictionary to map the files inside the directory
        before = dict ([])
        
    
    def stop_monitoring(self):
        print("Stopped monitoring files.")    