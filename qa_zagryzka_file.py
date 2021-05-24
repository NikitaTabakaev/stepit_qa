from selenium import webdriver
import os
import time
try:
    browser = webdriver.Firefox()

    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element_by_xpath("//input[@name = 'firstname']").send_keys("123")
    browser.find_element_by_xpath("//input[@name = 'lastname']").send_keys("456")
    browser.find_element_by_xpath("//input[@name = 'email']").send_keys("789")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_xpath("//input[@id = 'file']").send_keys(file_path)
    browser.find_element_by_xpath("//button[@class = 'btn btn-primary']").click()
finally:
    time.sleep(5)
    browser.quit()