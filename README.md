# Rented House Hunter Bot

A desktop application that automates the process of finding rental properties on MagicBricks.com, scrapes the results, and populates them into a Google Sheet for easy tracking.
---

## 🚀 Features

-   **Graphical User Interface (GUI)**: An intuitive interface built with Tkinter to input your search criteria.
-   **Automated Browser Interaction**: Uses Selenium to automatically open a browser, navigate to the property website, and fill in search details like location, budget, and BHK configuration.
-   **Web Scraping**: Employs BeautifulSoup to parse the HTML of the search results page and extract key information like property location, rent amount, and owner/agent details.
-   **Google Sheets Integration**: Utilizes the Sheety API to upload the scraped data directly into a Google Sheet of your choice, creating a personalized list of potential rental homes.

---

## 🛠️ How It Works

1.  **Input**: The user launches the application and is prompted by a GUI to enter their desired location, maximum budget, BHK preference, and the Sheety API endpoint for their Google Sheet.
2.  **Automation**: Upon clicking "Search", `Selenium` opens an incognito Chrome window and navigates to `magicbricks.com`. It programmatically fills out the search form with the user's criteria and executes the search.
3.  **Scraping**: Once the search results page loads, the bot captures the page's URL. `BeautifulSoup` then takes over to parse the page's HTML, extracting lists of property titles, rent amounts, and owner/agent names.
4.  **Uploading**: The extracted data is passed to the uploader module. It iterates through the property listings and sends a `POST` request for each one to the user-provided Sheety API endpoint.
5.  **Result**: The user's Google Sheet is automatically populated with the scraped rental property data, ready for review. The automation script then closes the browser window.

---

## ⚙️ Tech Stack

-   **Python 3**: Core programming language.
-   **Tkinter**: For the graphical user interface.
-   **Selenium**: For browser automation and interaction.
-   **BeautifulSoup4**: For web scraping and parsing HTML.
-   **Requests**: For making HTTP requests to the Sheety API.

---

## 📋 Prerequisites

Before you begin, ensure you have the following set up:

1.  **Python 3.x** installed on your system.
2.  **Google Chrome** browser installed.
3.  **ChromeDriver**: Download the version of ChromeDriver that matches your Google Chrome version. You must place it in your system's `PATH` or in the same directory as the script.
4.  **Google Sheet**: A blank Google Sheet to store the results.
5.  **Sheety Account**: A free account at [Sheety.co](https://sheety.co/) to turn your Google Sheet into an API.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rented-house-hunter-bot.git
cd rented-house-hunter-bot
Use code with caution.
Markdown
2. Install Dependencies
Install the required Python libraries using pip.
Generated bash
pip install beautifulsoup4 requests selenium
Use code with caution.
Bash
(Note: Tkinter is usually included with standard Python installations.)
3. Set up Google Sheet & Sheety
Create a new Google Sheet.
Add the following headers in the first row: area, owner/agent, rent.
Go to Sheety.co, log in, and create a new project.
Connect your Google Sheet and enable POST requests.
Copy the generated API Endpoint URL. You will need this to run the application.
🏃‍♂️ How to Run
Make sure chromedriver is accessible.
Run the main Python script from your terminal:
Generated bash
python main.py
Use code with caution.
Bash
(Assuming the main file is named main.py)
The GUI will appear.
Enter your desired location (e.g., "Koramangala, Bangalore").
Enter your maximum budget (e.g., 30000).
Enter the BHK configuration (e.g., 2).
Paste your Sheety API Endpoint URL into the final field.
Click the Search button.
A Chrome window will open and perform the search automatically. Once done, check your Google Sheet for the results!
📂 Code Structure
The application is composed of several classes, each with a specific responsibility:
GUI: Manages the Tkinter user interface, collects user input, and launches the process.
propertyWebsiteBot: Handles all Selenium-based browser automation, from opening the website to filling in the search form.
scrapperBot: Uses BeautifulSoup to parse the search results page and extract the relevant property data.
uploaderBot: Takes the scraped data and sends it to the specified Sheety API endpoint to populate the Google Sheet.
⚠️ Disclaimer
This tool depends on the HTML structure of magicbricks.com. If the website's layout changes, the web scraping component (scrapperBot) may need to be updated to match the new structure. Web scraping should be done responsibly and in accordance with the website's terms of service.
Generated code
Use code with caution.
