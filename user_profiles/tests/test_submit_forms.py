import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#from django.contrib.auth import get_user_model

#User = get_user_model()


class TestCreateProfile(unittest.TestCase):
    """Test User Profile Create View Form Submission"""

    def setUp(self):
        self.firefox_webdriver = webdriver.Firefox()

        #self.user = get_user_model().objects.create_user(
        #    'testuser',
        #    'testpassword'
        #)

    def test_create_profile_fire(self):
        print("Test User Profile Create View Form Submission in Firefox")
        self.firefox_webdriver.maximize_window()  # For maximizing window
        self.firefox_webdriver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        self.firefox_webdriver.get("http://127.0.0.1:8000/user-profiles/create-profile/")
        self.firefox_webdriver.find_element(By.ID, 'id_given_name').send_keys("tests")
        self.firefox_webdriver.find_element(By.ID, 'id_surname').send_keys("profile")
        self.firefox_webdriver.find_element(By.ID, 'id_email').send_keys("test@gmx.com")
        self.firefox_webdriver.find_element(By.ID, 'id_age').send_keys("50")
        self.firefox_webdriver.find_element(By.ID, 'create-profile').click()
        self.assertIn("http://localhost:8000/", self.firefox_webdriver.current_url)

    def tearDown(self):
        self.firefox_webdriver.quit()

if __name__ == '__main__':
    unittest.main()
