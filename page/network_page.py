from selenium.webdriver.common.by import By


class NetwrokPage:

    # 更多
    more_button = By.XPATH, "//*[contains(@text,'更多')]"

    # 移动网络
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"

    # 首选类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"

    # 2g
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"

    # 3g
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"


    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(self.more_button[0], self.more_button[1]).click()
        self.driver.find_element(self.network_button[0], self.network_button[1]).click()

    def click_first_network(self):
        self.driver.find_element(self.first_network_button[0], self.first_network_button[1]).click()

    def click_network_3g(self):
        self.driver.find_element(self.network_3g_button[0], self.network_3g_button[1]).click()

    def click_network_2g(self):
        self.driver.find_element(self.network_2g_button[0], self.network_2g_button[1]).click()