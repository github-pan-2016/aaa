class NetwrokPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

    def click_first_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

    def click_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def click_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()