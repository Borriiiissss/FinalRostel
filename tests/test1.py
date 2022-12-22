import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
driver = webdriver.Chrome()

# открывает страницу и получает ответ сервера 200
def test1():
    driver.get('https://b2c.passport.rt.ru')
    requests.get('https://b2c.passport.rt.ru')

# открывает страницу и последовательно вводит почту, логин, телефон, лицевой счёт. ТАб переходит на соответсвующие вводу позиции
def test2():

    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    driver.find_element("id", "username").send_keys("chega123@mail.ru")
    driver.find_element("id", "username").send_keys(Keys.TAB)
    time.sleep(2)

    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    driver.find_element("id", "username").send_keys("123456789123")
    driver.find_element("id", "username").send_keys(Keys.TAB)
    time.sleep(2)

    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    driver.find_element("id", "username").send_keys("chega123@mail.ru")
    driver.find_element("id", "username").send_keys(Keys.TAB)
    time.sleep(2)

    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    driver.find_element("id", "username").send_keys("+79095657892")
    driver.find_element("id", "username").send_keys(Keys.TAB)
    time.sleep(2)

    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    driver.find_element("id", "username").send_keys("login")
    driver.find_element("id", "username").send_keys(Keys.TAB)
    time.sleep(2)

# вводит невалидные номер телефона и пароль
def test3():
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(3)
    driver.find_element("id", "username").send_keys("89095657892")
    time.sleep(3)
    driver.find_element("id", "password").send_keys("1234567")
    time.sleep(3)
    driver.find_element("id", "kc-login").send_keys(Keys.ENTER)
    time.sleep(2)

# вводит невалидные адрес эл.почты и пароль
def test4():
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(3)
    driver.find_element("id", "username").send_keys("ch123@mail.ru")
    time.sleep(2)
    driver.find_element("id", "password").send_keys("1234567")
    time.sleep(2)
    driver.find_element("id", "kc-login").send_keys(Keys.ENTER)
    time.sleep(3)

# вводит невалидные логин и пароль
def test5():
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(3)
    driver.find_element("id", "username").send_keys("login")
    time.sleep(2)
    driver.find_element("id", "password").send_keys("1234567")
    time.sleep(2)
    driver.find_element("id", "kc-login").send_keys(Keys.ENTER)
    time.sleep(3)

# вводит невалидные лицевой счёт и пароль
def test6():
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(3)
    driver.find_element("id", "username").send_keys("123456789123")
    time.sleep(2)
    driver.find_element("id", "password").send_keys("1234567")
    time.sleep(2)
    driver.find_element("id", "kc-login").send_keys(Keys.ENTER)
    time.sleep(3)
