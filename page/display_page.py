from selenium.webdriver.common.by import By


class DisplayPage:

    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"

    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"

    # 文本框
    text_view = By.ID, "android:id/search_src_text"

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(self.display_button[0], self.display_button[1]).click()

    def click_search(self):
        self.driver.find_element(self.search_button[0], self.search_button[1]).click()

    def input_text_view(self, text):
        self.driver.find_element(self.text_view[0], self.text_view[1]).send_keys(text)

    def click_back(self):
        self.driver.find_element(self.back_button[0], self.back_button[1]).click()
