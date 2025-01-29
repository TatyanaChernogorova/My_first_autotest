from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
#from main import driver

@pytest.fixture
def log_in():
    test_site = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    sleep(5)
    driver.get(test_site)

    assert driver.title == 'Swag Labs'
    assert driver.current_url == "https://www.saucedemo.com/"


    login = driver.find_element(By.CSS_SELECTOR, "[name='user-name']")
    login.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("secret_sauce", Keys.ENTER)

    logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))
    assert logo.text == 'Swag Labs'
    assert logo.is_displayed()

    yield driver
    driver.quit()