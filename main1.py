import os
import requests # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from PIL import Image # type: ignore
from io import BytesIO
from googletrans import Translator # type: ignore
from collections import Counter
from browserstack.local import Local # type: ignore

# Ensure the images folder exists
os.makedirs("images", exist_ok=True)

# BrowserStack credentials
username = "mounivalli98@gmail.com"
access_key = "8e3ezSBXphYs8WeAGG1F"

# Start BrowserStack local tunnel (if required for local testing)
bs_local = Local()
bs_local_args = {"key":access_key}
bs_local.start(**bs_local_args)

# Setup WebDriver options for Selenium 4.x
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# BrowserStack capabilities
capabilities = {
    "browserName": "Chrome",
    "browser_version": "latest",
    "os": "Windows",
    "os_version": "10",
    "resolution": "1920x1080",
    "name": "BrowserStack Test",
    "build": "BrowserStack Selenium Integration",
    "browserstack.local": "true",  # Enables local testing via BrowserStack
    "browserstack.user": username,
    "browserstack.key": access_key
}

def scrape_opinion_articles():
    """Scrape the first 5 articles from the Opinion section of El País."""
    print("Launching browser on BrowserStack...")
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        capabilities=capabilities 
    )
    driver.get("https://elpais.com/")
    driver.maximize_window()

    # Wait for and accept the cookies pop-up if it appears
    try:
        # Wait for the "Accept" button of the cookies pop-up to be clickable using the provided XPath
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='didomi-notice-agree-button']"))
        )
        cookies_button.click()  # Click the "Accept" button to close the cookies pop-up
        print("Cookies pop-up accepted.")
    except Exception as e:
        print("No cookies pop-up detected or failed to accept it:", e)

    # Navigate to the Opinion section
    print("Navigating to Opinion section...")
    opinion_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Opinión"))
    )
    opinion_section.click()

    # Fetch first 5 articles
    print("Scraping articles...")
    articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]
    data = []

    for article in articles:
        title = article.find_element(By.CSS_SELECTOR, "h2").text
        content = article.find_element(By.CSS_SELECTOR, "p").text  # Adjust as necessary
        try:
            img_url = article.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        except Exception:
            img_url = None

        # Save image locally
        if img_url:
            print(f"Downloading image for article: {title[:10]}...")
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            img_name = f"{title[:10]}.jpg".replace(" ", "_")
            img.save(os.path.join("images", img_name))

        data.append({"title": title, "content": content, "img_url": img_url})

    driver.quit()
    print("Scraping complete.")
    return data

def translate_headers(headers):
    """Translate article headers from Spanish to English."""
    print("Translating headers...")
    translator = Translator()
    translated_headers = [translator.translate(header, src='es', dest='en').text for header in headers]
    return translated_headers

def analyze_headers(translated_headers):
    """Analyze translated headers for repeated words."""
    print("Analyzing headers for repeated words...")
    words = ' '.join(translated_headers).split()
    word_counts = Counter(words)
    repeated_words = {word: count for word, count in word_counts.items() if count > 2}
    return repeated_words

def main():
    """Main execution function."""
    # Step 1: Scrape Data
    scraped_data = scrape_opinion_articles()

    # Step 2: Translate Headers
    headers = [item['title'] for item in scraped_data]
    translated_headers = translate_headers(headers)
    print("Translated Headers:")
    print(translated_headers)

    # Step 3: Analyze Headers
    repeated_words = analyze_headers(translated_headers)
    print("Repeated Words:")
    print(repeated_words)

if __name__ == "__main__":
    print("Starting the script...")
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

    # Stop BrowserStack local tunnel
    bs_local.stop()
