import os
import json

class DataManager:
    # Configurations
    DOWNLOAD_PATH = "downloaded_images"
    OVERVIEW_FILE = "overview.txt"
    PROGRESS_FILE = "progress.json"
    INPUT_FILE = "input.txt"

    def load_progress(self):
        if os.path.exists(self.PROGRESS_FILE):
            with open(self.PROGRESS_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_progress(self, progress):
        with open(self.PROGRESS_FILE, 'w') as file:
            json.dump(progress, file, indent=4)

    def update_overview(self, overview):
        with open(self.OVERVIEW_FILE, 'w') as file:
            for url, data in overview.items():
                progress = f"{data['downloaded_pages']} p. - {data['progress']}%"
                file.write(f"{url} - {data['total_pages']} p. - {progress}\n")

    def read_input_urls(self):
        with open(self.INPUT_FILE, 'r') as file:
            return [line.strip() for line in file if line.strip()]