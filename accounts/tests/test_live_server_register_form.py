"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model

user = get_user_model()


class RegisterFormTest(LiveServerTestCase):
  def testform(self):
    print("Test Live Server Register -- must delete TestUser2 from db afterwards")
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/accounts/register/')
    #find the elements you need to submit form
    username = selenium.find_element(By.ID, 'id_username')
    password1 = selenium.find_element(By.ID, 'id_password1')
    password2 = selenium.find_element(By.ID, 'id_password2')

    submit = selenium.find_element(By.ID, 'register')

    #populate the form with data
    username.send_keys('TestUser2')
    password1.send_keys('testpassword')
    password2.send_keys('testpassword')


    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Login' in selenium.page_source
    print(selenium.page_source)

"""
