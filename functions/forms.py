from time import sleep
from functions import Navigation
import settings


class Forms:
    _driver = None

    def __init__(self, driver):
        self._driver = driver

    def search(self, text):
        Navigation(self._driver).search(text)
        results = self._driver.find_elements_by_class_name('search-result-subreddit')
        return results

    def authorization(self, login, passwd):
        elem = self._driver.find_element_by_name('user')
        elem.clear()
        elem.send_keys(login)
        elem = self._driver.find_element_by_name('passwd')
        elem.clear()
        elem.send_keys(passwd)
        elem.submit()
        sleep(1)

    def valid_authorization(self):
        self.authorization(settings.LOGIN, settings.PASSWORD)
        sleep(2)
