"""
from django.test import LiveServerTestCase
from seleniumlogin import force_login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateProfileFormTest(LiveServerTestCase):
  def testform(self):
    selenium = webdriver.Chrome()
    user = get_user_model().objects.create_user(
        'testuser',
        'testpassword'
    )
    force_login(user, selenium, "http://127.0.0.1:8000")
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/user-profiles/create-profile/')
    #find the elements you need to submit form
    given_name = selenium.find_element(By.ID, 'id_given_name')
    surname = selenium.find_element(By.ID, 'id_surname')
    email = selenium.find_element(By.ID, 'id_email')
    age = selenium.find_element(By.ID, 'id_age')

    submit = selenium.find_element(By.ID, 'create-profile')


    #populate the form with data
    given_name.send_keys('tests')
    surname.send_keys('profile')
    email.send_keys('test@gmx.com')
    age.send_keys('50')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'testuser' in selenium.page_source
    print(selenium.page_source)

"""