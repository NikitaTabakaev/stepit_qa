from selenium import webdriver


# browser = webdriver.Firefox()
# browser.execute_script("alert('Robots at work');")

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()


# делает скрол что бы элемент был виден в браузере
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()