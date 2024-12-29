Web Scraping with Selenium - El País Opinion Articles:
This project demonstrates how to scrape the first 5 articles from the "Opinión" section of the Spanish news outlet El País. The script also handles cookies pop-ups, translates the article titles from Spanish to English, and analyzes the translated titles for repeated words. The solution is built using Python and the Selenium framework.

Features:
Scrape Articles: Extracts the title and content of the first 5 articles from the Opinión section.
Handle Cookie Pop-up: Automatically accepts the cookies consent pop-up using XPath.
Image Downloading: Downloads and saves cover images for the articles.
Translate Titles: Translates the article titles from Spanish to English using the Google Translate API.
Analyze Repeated Words: Analyzes the translated titles to identify repeated words.
Prerequisites
Before you run the script, make sure you have the following installed:

Python 3.x
Google Translate API (can be installed via googletrans library)
Selenium (for browser automation)
WebDriver Manager (for managing the browser drivers)
PIL (Python Imaging Library) for image handling
Requests for making HTTP requests
Installed the required dependencies using pip:

pip install selenium googletrans requests pillow webdriver-manager


Web Browser
Google Chrome is required for Selenium to run the tests.
Chromedriver will be automatically managed by webdriver-manager.

.
├── images/              # Folder to store downloaded images
├── main.py              # Main Python script
└── README.md            # Project documentation
How to Run:
Clone the repository:

git clone <repository_url>
cd <repository_directory>

Install required libraries:

pip install -r requirements.txt

Run the script:

python main.py

OUPUT: The script will:

1.Open the El País website.
2.Accept the cookie consent pop-up.
3.Navigate to the Opinión section.
4.Scrape the first 5 articles.
5.Download the article images to the images/ directory.
6.Translate the article titles from Spanish to English.
7.Analyze and print repeated words in the translated titles.

How It Works
1. Cookie Consent Handling
The script waits for the cookie consent button (//*[@id='didomi-notice-agree-button']) to appear and clicks it automatically.

2. Navigating to the Opinion Section
Once the page is loaded, the script navigates to the Opinión section using the link text "Opinión" and extracts the first 5 articles.

3. Scraping Article Data
For each of the first 5 articles, the following data is extracted:

Title
Content 
Image URL 
The images are downloaded and saved locally in the images/ folder.

4. Translation of Titles
The script translates the article titles from Spanish to English using the Google Translate API.

5. Analyzing Repeated Words
After translation, the script analyzes the translated titles and prints the words that are repeated more than twice.

Troubleshooting
Cookies Pop-up Not Dismissing: Ensure the XPath for the "Accept" button is correct by inspecting the element in the browser.
Articles Not Found: Check the CSS selector for article titles and content. The structure of the website may have changed.


Contact
For any questions or feedback, please reach out to:

Email: mounika.vallivedu24@gmail.com
GitHub: 
