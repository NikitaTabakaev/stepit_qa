from selenium import webdriver

try:
    browser = webdriver.Firefox()
    # говорю webdriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

finally:
    browser.quit()