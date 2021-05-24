from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/selects1.html")
    # так же работает и с - http://suninjuly.github.io/selects2.html

    result = int(browser.find_element_by_xpath("//span[@id = 'num1']").text) + \
             int(browser.find_element_by_xpath("//span[@id = 'num2']").text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))

    browser.find_element_by_xpath("//button[@class = 'btn btn-default']").click()
finally:

    time.sleep(6)
    browser.quit()
