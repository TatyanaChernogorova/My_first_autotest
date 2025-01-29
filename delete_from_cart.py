from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from log_in import log_in
@pytest.fixture()
def add_product_to_cart(log_in):
    driver = log_in

    add_to_cart = log_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    add_to_cart.click()
    add_to_cart2.click()
    return driver

def test_delete_from_cart(add_product_to_cart):
    driver = add_product_to_cart

    # Проверка, того что в корзине 2 товара
    icon_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert icon_cart.text == "2"

    #Переход в корзину
    icon_cart.click()

    #Проверка отображения кнопки удаления remove у первой позиции товара
    delete_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    assert delete_btn.is_displayed()

    #Нажатие на кнопку удаления
    delete_btn.click()
    #sleep(5)

    #Проверка, что количество поменялось на 1
    icon_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert icon_cart.text == "1"

    delete_btn2 = driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt")
    delete_btn2.click()
    icon_cart = driver.find_element(By.ID, "shopping_cart_container")
    assert icon_cart.text == ""
