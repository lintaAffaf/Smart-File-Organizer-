Smart File Organizer

A Python script that automatically organizes files in any folder by sorting them into subfolders based on their file extension.


About the Project

This is my first Python project, built to practice core programming concepts including file I/O, OS module usage, dictionary lookups, error handling, and writing clean, documented code.

The script scans a folder chosen by the user, reads each file's extension, assigns it to a category, creates the category subfolder if it doesn't exist, and moves the file into it automatically.


How It Works


User enters the path of the folder to organize
Script reads all files in that folder
Each file's extension is matched to a category using a dictionary
Category subfolders are created automatically if they don't exist
Files are moved into their correct subfolder
A summary is printed at the end showing how many files were moved or skipped


Categories

ExtensionCategory.png, .jpegimages.pdf, .docx, .kerasdocuments.pptxpresentations.mp4videosanything elseothers


How to Run

Requirements: Python 3.x (no external libraries needed)

bashpython file_organizer.py

You will be prompted to enter the folder path:

Enter the folder path to organize: C:\Users\YourName\Downloads

Example output:

moved invoice.pdf to documents
moved photo.jpeg to images
Skipped old_resume.pdf: Destination path already exists
Organizing complete: 42 files moved, 1 files skipped.


Concepts Practiced

os and shutil modules
Dictionary lookups with .get() and fallback values
File path handling with os.path.join and os.path.splitext
Directory creation with os.mkdir
Error handling with try/except
Python script structure with if __name__ == "__main__":
Writing clean, commented, and documented code


Author
Linta Affaf
GitHub: @lintaAffaf

