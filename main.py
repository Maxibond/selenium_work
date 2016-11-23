from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import manager

if __name__ == '__main__':
    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    try:
        manager.start(driver)
    finally:
        driver.quit()
