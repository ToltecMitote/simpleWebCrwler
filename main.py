from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
on = True

while on:
    def five_seconds():
        time.sleep(5)
        cdp = "/home/kali/Desktop/chromedriver-linux64/chromedriver"
        driver = webdriver.Chrome(executable_path=cdp)

        # Here you paste the ULR you want the program to scan, you must make it more accurate than just e.g www.google.com.
        driver.get(
            "https://www.google.com/")
        # Put the class name from your chosen HTML file
        price = driver.find_element(By.CLASS_NAME, "reinventPricePriceToPayMargin")
        print(price.text)

        driver.quit()


    five_seconds()







