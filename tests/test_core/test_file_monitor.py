import tempfile
import sys
from pathlib import Path
import time
import threading

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from core.file_monitor import FileMonitor

def test_basic_functionality():
    
    # Setup test directories
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Using temporary directory: {temp_dir}")
        
        # Initialize FileMonitor
        monitor = FileMonitor(temp_dir)
        
        # Verify initial state 
        initial_files = monitor._get_current_files()
        print(f"Initial files: {initial_files}")
        
        # Create a new test file
        test_file = Path(temp_dir) / "test_file.txt"
        test_file.write_text("This is a test file.")
        
        # Check for changes
        changes = monitor.check_changes()        
        print(f"Detected changes: {changes}")
        
        # Verify added file detection
        assert len(changes) == 1
        assert changes[0][0] == "added"
        assert changes[0][1] == "test_file.txt"
        
        print(f"Current files after addition: {monitor._get_current_files()}")
        
        print("Basic functionality test passed.")
    

def test_continuous_functionality():
    """Tests event handlers functionality."""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Using temporary directory: {temp_dir}")

        # Initialize FileMonitor
        monitor = FileMonitor(temp_dir)
        events_detected = []

        def test_event_handler(filename):
            events_detected.append(filename)            

        monitor.add_event_handler('added', test_event_handler)
        monitor.add_event_handler('modified', test_event_handler)

        # Create test files to trigger events
        test_file_0 = Path(temp_dir) / "test_file_0.txt"
        test_file_1 = Path(temp_dir) / "test_file_1.txt"
        test_file_2 = Path(temp_dir) / "test_file_2.txt"
        
        test_file_0.write_text("This is test file 0.")
        time.sleep(0.1)
        test_file_1.write_text("This is test file 1.")
        time.sleep(0.1)
        test_file_2.write_text("This is test file 2.")
        time.sleep(0.1)
        
        # Check for changes
        changes = monitor.check_changes()
        print(f"Detected changes: {changes}")
        
        # Manually call the handlers for each detected change
        # (since we're not using start_monitoring's loop)
        for change_type, filename in changes:
            if change_type in monitor.handlers:
                for handler in monitor.handlers[change_type]:
                    handler(filename)
        
        print(f"Events detected: {events_detected}")
                
        assert len(changes) == 3
        assert len(events_detected) == 3

        print("Event handlers test passed.")


def test_with_start_monitoring():
    """Tests using actual start_monitoring method with threading."""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Using temporary directory: {temp_dir}")

        # Initialize FileMonitor
        monitor = FileMonitor(temp_dir)
        events_detected = []

        def test_event_handler(filename):
            events_detected.append(filename)
            print(f"Handler called for: {filename}")

        monitor.add_event_handler('added', test_event_handler)
        monitor.add_event_handler('modified', test_event_handler)

        # Start monitoring in a separate thread
        monitor_thread = threading.Thread(target=monitor.start_monitoring, args=(1,))  # 1 second interval
        monitor_thread.start()
        
        # Give the monitor a moment to start
        time.sleep(0.5)
        
        # Create test files
        test_file_0 = Path(temp_dir) / "test_file_0.txt"
        test_file_1 = Path(temp_dir) / "test_file_1.txt"
        
        test_file_0.write_text("This is test file 0.")
        time.sleep(1.5)  # Wait for monitor to detect
        
        test_file_1.write_text("This is test file 1.")
        time.sleep(1.5)  # Wait for monitor to detect
        
        # Stop monitoring
        monitor.stop_monitoring()
        monitor_thread.join()  # Wait for thread to finish
        
        print(f"Events detected: {events_detected}")
        
        # Should have detected 2 file additions
        assert len(events_detected) >= 2
        
        print("Start monitoring test passed.")

def test_file_modification():
    """Tests detection of file modifications."""
    
    # Setup test directory
    with tempfile.TemporaryDirectory() as temp_dir:
        
        # Create a test file
        test_file = Path(temp_dir) / "test_file.txt"
        test_file.write_text("Initial content.")
        
        # Initialize FileMonitor
        monitor = FileMonitor(temp_dir)
        
        # Modify the test file
        time.sleep(1)
        test_file.write_text("Modified content.")
        
        # Check for changes
        changes = monitor.check_changes()
        print(f"Detected changes after modification: {changes}")
        
        # Verify modified file detection
        assert len(changes) == 1
        assert changes[0][0] == "modified"
        
        print("File modification test passed.")

def test_file_removal():
    """Tests detection of file removals"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        
        # Create a test file
        test_file = Path(temp_dir) / "test_file.txt"
        test_file.write_text("This file will be deleted.")
        
        # Initialize FileMonitor
        monitor = FileMonitor(temp_dir)
        
        # Remove the test file
        test_file.unlink()
        
        # Check for changes
        changes = monitor.check_changes()
        
        print(f"Detected changes after removal: {changes}")
        
        assert len(changes) == 1
        assert changes[0][0] == "removed"
        
        print("File removal test passed.")

if __name__ == "__main__":
    print("Running basic functionality test...")
    test_basic_functionality()
    print("\nRunning event handlers test...")
    test_continuous_functionality()
    print("\nRunning start monitoring test...")
    test_with_start_monitoring()    
    print("\nRunning file modification test")
    test_file_modification()
    print("\nRunning removal test")
    test_file_removal()