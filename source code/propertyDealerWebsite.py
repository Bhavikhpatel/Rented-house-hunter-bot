from selenium import webdriver
import time
from graphicCode import GUI

from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class propertyWebsiteBot:
    def __init__(self, budget, bhk, location):
        self.budget = budget
        self.bedroomNo = bhk
        self.location = location.capitalize()
        self.filledWebsiteTabURL = None

        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--incognito')
        self.driver = webdriver.Chrome(chrome_option)

    def clickElement(self, elementName, xpath):
        element = None
        try:
            element = self.driver.find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            print(f"{elementName} NOT found")
        else:
            print(f"{elementName} found")
            element.click()
            time.sleep(1.1)
            return element

    def openWebsite(self):
        self.driver.get('https://www.magicbricks.com/')
        self.driver.maximize_window()
        time.sleep(3)

    def fillInDetails(self):
        # 1. click on Rent
        rentButton = self.clickElement('rentButton', '//*[@id="tabRENT"]')
        time.sleep(1)
        # 2. click on location input  field
        locationInputField = self.driver.find_element(by=By.XPATH, value='//*[@id="keyword"]')
        locationInputField.click()
        time.sleep(1)
        # 3. click on bangalore close button
        bangaloreCloseButton = self.clickElement('bangaloreCloseButton',
                                                 '//*[@id="keyword_autoSuggestSelectedDiv"]/div/div[2]')
        time.sleep(1)
        # 4. input location
        locationInputField.send_keys(self.location)
        time.sleep(1)
        # 5. select location from pop up
        locationFromPopUp = self.driver.find_elements(by=By.CLASS_NAME, value='mb-search__auto-suggest__item')
        locationFromPopUp[0].click()
        time.sleep(1)
        # 6. select bhk
        flatButton = self.clickElement('flatButton', '//*[@id="propType_rent"]/div[1]')
        time.sleep(1)

        bhk1Button = self.driver.find_element(by=By.ID, value='11700')
        bhk2Button = self.driver.find_element(by=By.ID, value='11701')
        bhk3Button = self.driver.find_element(by=By.ID, value='11702')
        bhk4Button = self.driver.find_element(by=By.ID, value='11703')

        bhk1Button.click()
        bhk2Button.click()
        bhk3Button.click()

        match self.bedroomNo:
            case '1':
                bhk1Button.click()
            case '2':
                bhk2Button.click()
            case '3':
                bhk3Button.click()
            case '4':
                bhk4Button.click()

        flatButton = self.clickElement('flatButton', '//*[@id="propType_rent"]/div[1]')
        time.sleep(1)
        # 7. set budget
        budgetButton = self.clickElement('budgetButton',
                                         '//*[@id="searchFormHolderSection"]/section/div/div[1]/div[3]/div[3]/div[1]')
        time.sleep(1)
        maxPriceInputField = self.driver.find_element(by=By.XPATH, value='//*[@id="budgetMax"]')
        maxPriceInputField.click()
        maxPriceInputField.send_keys(str(int(self.budget)))
        time.sleep(1)
        budgetButton = self.clickElement('budgetButton',
                                         '//*[@id="searchFormHolderSection"]/section/div/div[1]/div[3]/div[3]/div[1]')
        time.sleep(1)
        # 8. click on search
        searchButton = self.clickElement('searchButton',
                                         '//*[@id="searchFormHolderSection"]/section/div/div[1]/div[3]/div[4]')
        time.sleep(5)

        self.filledWebsiteTabURL = self.driver.current_url

    def exitWebsite(self):
        self.driver.close()
        self.driver.quit()