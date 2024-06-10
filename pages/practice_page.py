from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PracticePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_on_login_page_link(self):
        link = self.driver.find_element(By.LINK_TEXT, "Test Login Page")
        link.click()
        return LoginPage(self.driver)

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
