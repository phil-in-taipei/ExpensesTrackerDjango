from django.test import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


#from django.contrib.auth import get_user_model

#User = get_user_model()


class TestLogUserIn(unittest.TestCase):
    """Test User Profile Login Form Submission"""

    def setUp(self):
        self.firefox_webdriver = webdriver.Firefox()

        #self.user = get_user_model().objects.create_user(
        #    'TestUser',
        #    'testpassword'
        #)

    def test_user_login_fire(self):
        print("Test User Login View Form Submission in Firefox")
        self.firefox_webdriver.maximize_window()  # For maximizing window
        self.firefox_webdriver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        self.firefox_webdriver.get("http://127.0.0.1:8000/accounts/login/")
        self.firefox_webdriver.find_element(By.ID, 'id_username').send_keys("TestUser")
        self.firefox_webdriver.find_element(By.ID, 'id_password').send_keys("testpassword")
        self.firefox_webdriver.find_element(By.ID, 'login').click()
        self.assertIn("http://127.0.0.1:8000/landing/welcome/", self.firefox_webdriver.current_url)

    def tearDown(self):
        self.firefox_webdriver.quit()


if __name__ == '__main__':
    unittest.main()
