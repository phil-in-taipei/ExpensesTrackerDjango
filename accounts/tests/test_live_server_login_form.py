"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/accounts/login/')
    #find the elements you need to submit form
    username = selenium.find_element(By.ID, 'id_username')
    password = selenium.find_element(By.ID, 'id_password')

    submit = selenium.find_element(By.ID, 'login')

    #populate the form with data
    username.send_keys('TestUser')
    password.send_keys('testpassword')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'TestUser' in selenium.page_source
    print(selenium.page_source)

"""