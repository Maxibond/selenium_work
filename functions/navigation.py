from time import sleep


class Navigation:

    _driver = None
    _url = ''

    def __init__(self, driver, url=''):
        self._driver = driver
        self._url = url

    def to_index_page(self):
        self._driver.get(self._url)

    def search(self, text):
        elem = self._driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys(text)
        elem.submit()
        sleep(3)

    def to_first_text_post(self):
        # находим ссылку у первого текстового поста
        elem = self._driver.find_element_by_xpath("//div[@data-context='listing'"
                                            " and div[contains(@class, 'entry')]/div[contains(@class, 'selftext')]]"
                                            "/div[contains(@class, 'entry')]/p[1]/a")
        self._driver.get(elem.get_attribute('href'))
        sleep(2)
        return 'author' in self._driver.page_source
