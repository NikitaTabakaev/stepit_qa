from selenium import webdriver
import time

try:
    browser = webdriver.Firefox()
    browser.get('http://suninjuly.github.io/find_xpath_form')

    browser.find_element_by_xpath("//input[@name = 'first_name']").send_keys("Бу")
    browser.find_element_by_xpath("//input[@name = 'last_name']").send_keys("Бу")
    browser.find_element_by_xpath("//input[@class= 'form-control city']").send_keys("Бу")
    browser.find_element_by_xpath("//input[@id= 'country']").send_keys("Бу")
    browser.find_element_by_xpath("//button[@type = 'submit']").click()

finally:
    time.sleep(5)
    browser.quit()