URL= "https://www.newegg.com/p/pl?N=50001314%20100007709%20601357250%20601357247&Manufactory=1314"
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import EmailBot as eb

class NeweggBot:
    options = wd.ChromeOptions()
    #TODO set path to chrome.exe and chromedriver
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_driver_binary = "chromedriver.exe"
    driver = wd.Chrome(chrome_driver_binary, chrome_options=options)
    driver.get(URL)

    def scrapNewEgg(self):
        # driver.save_screenshot("screenshot.png")
        soup = BeautifulSoup(NeweggBot.driver.page_source)
        # soup.find("div" , {"class": "items-grid-view"})
        items = soup.find("div" , {"class": "items-grid-view"})
        items_array = items.findAll("div", {"class": "item-cell"})
        NeweggBot.driver.quit()
        rows_processed = []
        for item in items_array:
            itemTitle = item.find("a", {"class": "item-title"})
            itemPromo = item.find("p", {"class": "item-promo"})
            row = []

            row.append(itemTitle.text)
            message = ""
            if (itemPromo and itemPromo.text == "OUT OF STOCK"):
                row.append("Sold Out")
            else:
                row.append("Available")
                message += itemTitle.text + " available\n"

        if message != "":
            eb.emailMySelf("Found a Graphic Card", message)
            return True
        else:
            eb.emailMySelf("Cards Not Found", message)
            return False

if __name__ == "__main__":
    bot = NeweggBot
    NeweggBot.scrapNewEgg(bot)
