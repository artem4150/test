from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_saucedemo_purchase():
    # Настройки драйвера
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Чтобы тесты запускались без GUI, если нужно
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Открытие страницы
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Выбор товара
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Убедиться, что товар добавлен
        item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_name == "Sauce Labs Backpack", "Товар не был добавлен в корзину"

        # Оформление заказа
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Завершение покупки
        driver.find_element(By.ID, "finish").click()

        # Убедиться, что покупка завершена
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert success_message == "THANK YOU FOR YOUR ORDER", "Покупка не завершена успешно"

        print("Тест успешно выполнен")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_saucedemo_purchase()
