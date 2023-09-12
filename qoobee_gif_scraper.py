import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


url = "https://qoobee.com/emoji/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
save_directory = "downloaded_gifs"
os.makedirs(save_directory, exist_ok=True)


options = webdriver.ChromeOptions()
options.add_argument("--headless")  
driver = webdriver.Chrome(options=options)

# Open the website in the browser
driver.get(url)

# Scroll down to trigger content loading 
SCROLL_PAUSE_TIME = 3  
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse HTML content to find image elements
soup = BeautifulSoup(driver.page_source, "html.parser")
img_elements = soup.find_all("img", {"class": "attachment-full size-full wp-post-image jetpack-lazy-image"})

# Iterate through hyperlink elements to get GIF URLs
for img_element in img_elements:
  
    gif_url = img_element.get("src")

    if gif_url:
        file_name = os.path.join(save_directory, os.path.basename(gif_url))
        gif_response = requests.get(gif_url, headers=headers)

        if gif_response.status_code == 200:
            with open(file_name, "wb") as gif_file:
                gif_file.write(gif_response.content)
            print(f"Downloaded: {file_name}")

        else:
            print(f"Failed to download {url}. Status code: {gif_response.status_code}")

# Close the browser
driver.quit()