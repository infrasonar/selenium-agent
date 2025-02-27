from selenium import webdriver
from selenium.webdriver.common.by import By

NAME = 'myTest'
DESCRIPTION = 'test'
URL = 'https://www.selenium.dev/selenium/web/web-form.html'


def run(driver: webdriver.Chrome):
    driver.get(URL)

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
