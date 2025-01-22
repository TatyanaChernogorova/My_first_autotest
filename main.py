from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    test_site = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    sleep(5)
    driver.get(test_site)
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    assert driver.title == 'Swag Labs'
    assert driver.current_url == "https://www.saucedemo.com/"


    login = driver.find_element(By.CSS_SELECTOR, "[name='user-name']")
    login.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("secret_sauce", Keys.ENTER)

    logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))
    assert logo.text == 'Swag Labs'
    assert logo.is_displayed()


    open_product = driver.find_element(By.ID, "item_4_title_link")
    btn_add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='add-to-cart-sauce-labs-backpack']")
    assert open_product.is_displayed()
    assert open_product.text == 'Sauce Labs Backpack'
    assert btn_add_to_cart.is_displayed()
    assert btn_add_to_cart.text == 'Add to cart'


    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    btn_add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='add-to-cart-sauce-labs-backpack']")
    assert cart.is_displayed()
    assert cart.text == ''
    btn_add_to_cart.click()
    assert cart.text == '1'

    cart.click()
    product_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert product_in_cart.is_displayed()

