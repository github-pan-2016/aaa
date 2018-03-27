from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        # self.driver.find_element(loc[0], loc[1]).click()
        WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(loc[0], loc[1])).click()



    def input_text(self, loc, text):
        # self.driver.find_element(loc[0], loc[1]).send_keys(text)
        WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(loc[0], loc[1])).send_keys(text)