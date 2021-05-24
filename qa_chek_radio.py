from selenium import webdriver
import time
import math

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/math.html")

    numb = browser.find_element_by_xpath("//span[@id = 'input_value']").text
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(str(math.log(abs(12*math.sin(int(numb))))))
    browser.find_element_by_xpath("//label[@for = 'robotCheckbox']").click()
    browser.find_element_by_xpath("//label[text() = 'Robots rule']").click()
    browser.find_element_by_xpath("//button[@class = 'btn btn-default']").click()
finally:
    time.sleep(7)
    browser.quit()
