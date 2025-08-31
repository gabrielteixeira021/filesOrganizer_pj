from typing import List, Dict 
from pathlib import Path
import time

# TODO: Add logging instead of print statements
# TODO: Add error handling for file access issues
# TODO: add watchdog for more efficient monitoring

class FileMonitor:
    
    DEFAULT_POOLING_INTERVAL = 10 # in seconds
    
    def __init__(self, watch_directory):
        """Initializes the file monitor with the directory to watch."""
        self.watch_directory = Path(watch_directory)    # convert to Path object
        self.initial_state = self._get_current_files()  # directory initial state
        self.handlers = {} # Dictionary to hold event handlers
        self.is_monitoring = False

    def _get_current_files(self) -> Dict[str, float]:
        """Returns a Dictionary of current files in the directory with their last modified times."""
        if not self.watch_directory.exists():
            raise ValueError(f"Directory {self.watch_directory} does not exist.")    

        return {
            entry.name: entry.stat().st_mtime
            for entry in self.watch_directory.iterdir()
            if entry.is_file()
        }
        
        
    def check_changes(self) -> List[str]:
        """Compares two dictionaries of files and returns added, removed, and modified files."""
        
        # Detect changes in the directory
        current_files = self._get_current_files()
        changes = []

        # Check for added or modified files
        for filename, mtime in current_files.items():
            if filename not in self.initial_state:
                changes.append(("added", filename))
            elif mtime != self.initial_state[filename]:
                changes.append(("modified", filename))

        # Check for removed files
        changes.extend(
            ("removed", file)
            for file in self.initial_state
            if file not in current_files
        )
        
        # Update the initial state to the current state
        self.initial_state = current_files

        return changes
    
    """Registers an event handler for a specific event type."""
    def add_event_handler(self, event_type, handler_function):
        
        if event_type not in self.handlers:
            self.handlers[event_type] = []
            
        self.handlers[event_type].append(handler_function)
        
        
        
        
    def start_monitoring(self, pooling_interval=DEFAULT_POOLING_INTERVAL):
        print(f"Started monitoring {self.watch_directory} for changes.")
        self.is_monitoring = True

        # Monitor the directory for changes while the program is running
        try:
            while self.is_monitoring:
                if changes := self.check_changes():
                    print(f"Changes detected: {changes}")

                    # Call the registered handlers for each change
                    for change_type, filename in changes:
                        if change_type in self.handlers:
                            for handler in self.handlers[change_type]:
                                handler(filename)

                time.sleep(pooling_interval)

        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
        finally:
            self.is_monitoring = False
    
    def stop_monitoring(self):
        """Stops the monitoring process."""
        self.is_monitoring = False
        print("Stopped monitoring files.")        
        