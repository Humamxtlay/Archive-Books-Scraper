import os
import re
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataManager import DataManager

def main():
    dataManager = DataManager()
    progress = dataManager.load_progress()
    urls = dataManager.read_input_urls()
    overview = {}
    
    driver = webdriver.Chrome()

    for url in urls:
        identifier = url.split('/')[-1]
        local_dir = os.path.join(dataManager.DOWNLOAD_PATH, identifier)
        os.makedirs(local_dir, exist_ok=True)

        if url not in progress:
            progress[url] = {"next_page": 0, "last_download": None, "downloaded_pages": 0, "total_pages": 0}

        data = progress[url]
        next_page = data["next_page"]
        pages_downloaded_today = 0

        stopLoading = False
        while stopLoading == False:
            page_url = f"{url}/page/n{next_page}/mode/2up"
            if next_page == 0: page_url = url

            driver.get(page_url)
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.BRpage-visible .BRpageimage')))

            if data['total_pages'] == 0:
                pages = driver.find_elements(By.CSS_SELECTOR, '.BRcurrentpage')[0]
                numbers = re.findall(r'\d+', pages.text)
                data['total_pages'] = int(numbers[-1])

            # Locate all image elements
            images = driver.find_elements(By.CSS_SELECTOR, '.BRpage-visible .BRpageimage')

            # Download each image
            for _, image in enumerate(images):
                image_url = image.get_attribute('src')
                if image_url and "preview-default.png" not in image_url:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(os.path.join(local_dir, f"page_{next_page}.jpg"), 'wb') as file:
                            file.write(response.content)
                        data["downloaded_pages"] += 1
                        pages_downloaded_today += 1
                        next_page += 1                          
                else:
                    stopLoading = True

        data["next_page"] = next_page
        data["last_download"] = datetime.datetime.now().isoformat()
        
        # Update overview info
        overview[url] = {
            "total_pages": data["total_pages"],  # Assume some method to get total pages
            "downloaded_pages": data["downloaded_pages"],
            "progress": round((data["downloaded_pages"] / data["total_pages"]) * 100, 2) if data["total_pages"] else 0
        }

    driver.quit()
    dataManager.save_progress(progress)
    dataManager.update_overview(overview)

if __name__ == "__main__":
    main()
