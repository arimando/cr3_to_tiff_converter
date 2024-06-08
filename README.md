# CR3 to TIFF Converter

A simple GUI application to convert CR3 files to TIFF format. The application supports both English and Italian based on the system language.

## Features

- Convert CR3 files to TIFF format.
- Progress bar and log area to monitor conversion progress.
- Language support for English and Italian.
- Info button displaying the creator information.
- Error handling with logs saved to `error_log.txt`.

## Prerequisites

- Windows operating system
- The executable version does not require Python or any libraries installed on the user's system.

## Installation

1. **Download the Executable:**
   Download the executable file from the release section (provide link here).

2. **Run the Executable:**
   Double-click the `convert_cr3_to_tiff_gui.exe` file to start the application.

## Usage

1. **Select Input Folder:**
   - Click the "Browse..." button next to "Input Folder" to select the directory containing your CR3 files.

2. **Select Output Folder:**
   - Click the "Browse..." button next to "Output Folder" to select the directory where you want to save the converted TIFF files.

3. **Start Conversion:**
   - Click the "Start Conversion" button to begin the conversion process. 
   - Monitor the progress in the progress bar and check the logs in the text area below the progress bar.

4. **View Info:**
   - Click the "Info" button to display information about the creator.

## Error Handling

If an error occurs, an error message will be displayed, and details will be logged to `error_log.txt` in the same directory as the executable. Check this file for more information about the error.

## Building from Source

If you want to build the executable from the source code, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
2. **Install Dependencies**
   pip install rawpy imageio pillow tqdm pyinstaller
3. **Build the Executable**
   pyinstaller --onefile --noconsole --icon=path_to_icon.ico --hidden-import=rawpy --hidden-import=imageio --hidden-import=PIL --hidden-import=tqdm convert_cr3_to_tiff_gui.py
   Replace path_to_icon.ico with the path to your icon file.
4. Lunch

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Created by F. Federico with the help of AI.

### How to Use This README

1. **Save the README:**
   Save the content above in a file named `README.md` in the root directory of your project.

2. **Customize the Repository URL:**
   Replace `<repository-url>` with the URL of your project's repository.

3. **Icon Path:**
   Ensure the path to your icon file is correctly specified in the build command.

This README provides a comprehensive guide to using, building, and understanding your project in a format that is suitable for GitHub. If you need any more adjustments or additions, let me know!
