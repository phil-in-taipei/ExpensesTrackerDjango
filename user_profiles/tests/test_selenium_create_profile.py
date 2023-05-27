"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumlogin import force_login
#from django.test import TestCase


from django.contrib.auth import get_user_model

User = get_user_model()


class TestCreateProfile(unittest.TestCase):
    #Test User Profile Create View Form Submission

    def setUp(self):
        self.firefox_webdriver = webdriver.Firefox()
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )
        #force_login(self.user, self.firefox_webdriver, "http://127.0.0.1:8000/")
        #self.firefox_webdriver.force_login(self.user)
        #force_login(user, selenium, live_server.url)

    def test_create_profile_fire(self):
        print("Test User Profile Create View Form Submission in Firefox")
        force_login(self.user, self.firefox_webdriver, "http://127.0.0.1:8000")
        self.firefox_webdriver.maximize_window()  # For maximizing window
        self.firefox_webdriver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        self.firefox_webdriver.get("http://127.0.0.1:8000/user-profiles/create-profile/")
        self.firefox_webdriver.find_element(By.ID, 'id_given_name').send_keys("tests")
        self.firefox_webdriver.find_element(By.ID, 'id_surname').send_keys("profile")
        self.firefox_webdriver.find_element(By.ID, 'id_email').send_keys("test@gmx.com")
        self.firefox_webdriver.find_element(By.ID, 'id_age').send_keys("50")
        self.firefox_webdriver.find_element(By.ID, 'create-profile').click()
        self.assertIn("http://localhost:8000/", self.firefox_webdriver.current_url)
        # self.assertRedirects(response, '/accounts/login/?next=/sekrit/')
        # http://127.0.0.1:8000/accounts/login/?next=/user-profiles/create-profile/

    def tearDown(self):
        self.firefox_webdriver.quit()


if __name__ == '__main__':
    unittest.main()

"""