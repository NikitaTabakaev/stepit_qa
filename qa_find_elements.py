from selenium import webdriver
import time

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//input[@type = 'text']")
    for element in elements:
        element.send_keys("Мой ответ")

    time.sleep(5)
    browser.find_element_by_xpath("//button[@type = 'submit']").click()
finally:
    browser.quit()
