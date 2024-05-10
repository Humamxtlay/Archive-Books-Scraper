# Archive Page Downloader

## Description

This Python script automates the downloading of image pages from archived book listings at the Internet Archive website, following specific URL patterns. Due to restrictions on the website, the script is designed to download a limited number of pages per day (10 pages per 24 hours) to comply with viewing restrictions. It manages multiple URLs and tracks download progress over multiple days, storing each page's image in separate directories named after each book's unique identifier.

## Features

- **Automated Downloads**: Automatically navigates and downloads up to 10 pages per book per day.
- **Progress Tracking**: Keeps track of downloaded pages and resumes from the last page after a 24-hour wait period.
- **Local Organization**: Downloads images are saved in directories corresponding to their book identifiers.
- **Overview Updates**: Generates and updates an overview file listing all URLs with the number of pages downloaded and percentage completion.

## Installation

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Requests library

To install Python and necessary packages:

```bash
# Install Python from your distribution's repository or the Python website.

# After Python installation, install the required Python packages:
pip install selenium requests
```

### WebDriver
You need to download and set up a WebDriver for Selenium. This script uses ChromeDriver, which you can download from ChromeDriver - WebDriver for Chrome. Ensure it is added to your system's PATH.

## Usage
- **Prepare Input File:**

    Create an input.txt file in the script's directory.
    Add one URL per line for each book you wish to download pages from.
- **Run the Script:** 

    Execute the script daily to comply with the download limits:
    ```bash
    Copy code
    python archive_page_downloader.py
    ```
- **Check Outputs:**

    - Images are saved in the downloaded_images folder under subfolders named after each book's identifier.
    - Review the overview.txt file for progress updates on each book.

## Configuration
No additional configuration is needed outside of the initial setup of the input file and ensuring the WebDriver is correctly installed.

## Limitations
The script adheres to the Internet Archive's 10-page preview limit per day to avoid violating terms of service.
Changes in the webpage structure or URL format at the Internet Archive may require updates to the script.