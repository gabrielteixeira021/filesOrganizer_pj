# File Organizer

A simple Python app that automatically organizes downloaded files by type into appropriate folders.

## What it does

- Monitors downloaded files
- Classifies files by extension (e.g., .mp4 → Videos folder)
- Moves files to organized folders automatically

## Usage

Run the application:

```bash
python src/main.py
```

## Project Structure

```
organizador_arquivos/          # Project root directory
│
├── src/                       # Main source code
│   ├── __init__.py           # Makes src a Python package
│   ├── main.py               # Application entry point
│   ├── core/                 # Core system modules
│   │   ├── __init__.py
│   │   ├── file_monitor.py   # File monitoring
│   │   ├── file_classifier.py # File classification
│   │   └── file_mover.py     # File movement
│   ├── utils/                # Utilities and helpers
│   │   ├── __init__.py
│   │   ├── config_manager.py # Configuration management
│   │   ├── logger.py         # Logging system
│   │   └── helpers.py        # Helper functions
│   └── gui/                  # Graphical interface
│       ├── __init__.py
│       ├── main_window.py    # Main window
│       ├── settings_dialog.py # Settings dialog
│       └── components/       # Reusable UI components
│           ├── __init__.py
│           ├── file_list.py  # File list component
│           └── log_viewer.py # Log viewer component
│
├── tests/                    # Automated tests
│   ├── __init__.py
│   ├── test_core/           # Core modules tests
│   │   ├── __init__.py
│   │   ├── test_file_monitor.py
│   │   ├── test_file_classifier.py
│   │   └── test_file_mover.py
│   ├── test_utils/          # Utilities tests
│   │   ├── __init__.py
│   │   ├── test_config_manager.py
│   │   └── test_logger.py
│   └── test_gui/            # Interface tests
│       ├── __init__.py
│       └── test_main_window.py
│
├── docs/                    # Project documentation
│   ├── index.md            # Documentation main page
│   ├── vision.md           # Vision document
│   ├── requirements.md     # System requirements
│   ├── setup.md           # Installation guide
│   ├── usage.md           # Usage guide
│   └── images/            # Documentation images
│       └── architecture.png
│
├── data/                   # Application data
│   ├── config/             # Configuration files
│   │   └── settings.json   # Settings file
│   ├── categories/         # Category definitions
│   │   └── default_categories.json
│   └── logs/               # Application logs
│       └── app.log         # Log file
│
├── scripts/               # Auxiliary scripts
│   ├── install.py         # Installation script
│   ├── build.py           # Build script (future)
│   └── deploy.py          # Deploy script (future)
│
├── requirements.txt       # Project dependencies
├── README.md             # Main documentation (this file)
├── README_PT.md          # Portuguese documentation
├── LICENSE               # Project license
└── .gitignore           # Files ignored by Git
```

## Features to Add Later

- [ ] Watch Downloads folder automatically
- [ ] Configurable file type categories
- [ ] GUI interface
- [ ] Undo functionality
- [ ] Custom folder destinations
- [ ] Duplicate file handling
- [ ] Real-time file monitoring
- [ ] Configuration through GUI
- [ ] Logging and history
- [ ] Multiple directory monitoring

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

## Contributing

This project follows a simple and minimal Python development environment approach, perfect for beginner-friendly contributions.

## License

[Add your license information here]
