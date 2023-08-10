# Folder Synchronization Program

This is a simple Python program that synchronizes the content of a source folder to a replica folder at regular intervals. The synchronization is one-way, ensuring that the replica folder matches the content of the source folder. The program logs file creation, copying, and removal operations to a log file and also displays them on the console.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal/command prompt and navigate to the folder containing the program files.

3. Run the program using the following command:

$ python sync_files.py /path/to/source /path/to/replica 60 /path/to/log.txt
$ python sync_files.py ./source ./replica 60 ./log.txt

Replace the placeholders with the actual paths and values:

- `/path/to/source`: The path to the source folder you want to synchronize.
- `/path/to/replica`: The path to the replica folder that will be kept in sync with the source folder.
- `sync_interval_minutes`: The synchronization interval in minutes.
- `/path/to/log.txt`: The path to the log file that will record synchronization actions.

4. The program will start synchronizing the folders and display synchronization actions on the console. It will also write these actions to the specified log file.

5. To stop the program, press Ctrl+C in the terminal.

## Requirements

- Python 3.x

## Notes

- The program uses built-in Python libraries (`os`, `shutil`, and `time`) for basic operations and synchronization logic. It does not use third-party libraries specifically designed for folder synchronization.

- The synchronization interval can be specified in minutes. For example, to synchronize every 60 minutes, provide `60` as the `sync_interval_minutes` argument.

- The program provides basic error handling and logs any exceptions that might occur during synchronization.

## License

This program is provided under the MIT License. Feel free to modify and use it according to your needs.

---
Created by Sajid Ullah
