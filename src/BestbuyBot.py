URL= "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080&sc=Global&st=graphics%20card&type=page&usc=All%20Categories"
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import EmailBot as eb

class BestbuyBot:
    options = wd.ChromeOptions()
    #TODO set path to chrome.exe and chromedriver
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_driver_binary = "chromedriver.exe"
    driver = wd.Chrome(chrome_driver_binary, chrome_options=options)
    driver.get(URL)

    def scrapBestBuy(self):
        soup = BeautifulSoup(BestbuyBot.driver.page_source)
        items = soup.find("div" , {"id": "main-results"})
        items_array = items.findAll("li", {"class": "sku-item"})
        BestbuyBot.driver.quit()
        rows_processed = []
        for item in items_array:
            itemTitle = item.find("h4", {"class": "sku-header"})
            itemPromo = item.find("button", {"class": "add-to-cart-button"})
            row = []
            print(itemPromo.text)
            row.append(itemTitle.text)
            message = ""
            if (itemPromo.text == "Sold Out" or itemPromo.text == "Coming Soon"):
                row.append("Sold Out")
            else:
                row.append("Available")
                message += itemTitle.text + " available\n"
                message += URL + " \n"

            rows_processed.append(row)

        if message != "":
            eb.emailMySelf("Found a Graphic Card on BestBuy", message)
            return True
        else:
            eb.emailMySelf("BestBuy Cards Not Found", message)
            return False

if __name__ == "__main__":
    bot = BestbuyBot
    BestbuyBot.scrapBestBuy(bot)
