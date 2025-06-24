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
