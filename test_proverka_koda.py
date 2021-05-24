import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

message = ""

browser = webdriver.Firefox()

browser.get("https://stepik.org/lesson/236896/step/1")

time.sleep(5)
answer = math.log(int(time.time()))
browser.find_element_by_xpath("//textarea").send_keys(str(answer))

WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
).click()

t = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//pre[@class = 'smart-hints__hint']"))).text

if t == "Correct!":
    message += t

print(message)