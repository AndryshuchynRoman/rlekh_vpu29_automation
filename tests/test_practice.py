import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from practice_page import PracticePage


class TestPractice:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_login_page_navigation(self, setup):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        # Verify the practice page title
        assert self.driver.title == "Practice"

        # Click on the "Test Login Page" link
        practice_page = PracticePage(self.driver)
        login_page = practice_page.click_on_login_page_link()

        # Verify the login page title
        assert self.driver.title == "Test Login Page"
