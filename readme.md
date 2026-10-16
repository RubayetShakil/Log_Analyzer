# Python Log Analyzer

A Python command-line tool that analyzes `.log` files, counts log severity levels, and identifies frequently occurring error messages.

This project demonstrates Python file handling, directory traversal, command-line arguments, and dictionary-based frequency counting.

## Features

- **Recursive log scanning:** Searches the specified directory and its subdirectories for `.log` files.
- **Severity counting:** Counts log entries containing `INFO`, `WARNING`, and `ERROR`.
- **Error summarization:** Counts occurrences of extracted error messages.
- **Frequent error identification:** Identifies the error message or messages with the highest occurrence count.
- **Command-line input:** Accepts a log directory as an argument.
- **Directory validation:** Checks whether the specified directory exists before processing.

## Technologies

- Python 3
- `os` — directory traversal and path handling
- `sys` — command-line arguments and program exit
- Dictionaries — error frequency counting

All dependencies are from the Python standard library.

## Project Structure

```text
log-analyzer/
├── log_analyzer.py
├── sample_logs/
│   └── ...
├── README.md
└── .gitignore
```

The `sample_logs/` directory contains example log files for testing the program.

## Requirements

- Python 3
- A directory containing `.log` files

No third-party Python packages are required.

## Usage

Run the analyzer by providing the path to a log directory:

```bash
python3 log_analyzer.py sample_logs
```

You can also provide an absolute or relative path to another directory:

```bash
python3 log_analyzer.py /path/to/log_directory
```

If the directory does not exist or no directory argument is provided, the program displays an error or usage message.

## Example Output

The exact output depends on the contents of your log files.

```text
INFO: 4
WARNING: 2
ERROR: 4
=====ERROR SUMMARY=====
Database connection failed: 2
=====Most Frequent Errors=====
Database connection failed : 2
```

## Limitations

- Log severity detection uses text matching rather than a configurable log-format parser.
- Error message extraction assumes a consistent log-line structure.
- The program currently focuses on counting and summarizing errors rather than diagnosing their root causes.

## Future Improvements

- Support different log formats.
- Improve error handling for unreadable files and invalid encodings.
- Export analysis results to CSV or JSON.
- Add date-based filtering and severity summaries.

