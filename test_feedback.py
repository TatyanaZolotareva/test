from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/ThundeRobot/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.metcom.ru/hot/")
driver.set_window_size(1411, 812)
driver.find_element(By.NAME, "form_text_23").send_keys("Иванов Иван иванович")
driver.find_element(By.NAME, "form_email_26").send_keys("mail@gmail.com")
driver.find_element(By.NAME, "form_text_27").send_keys("+79999999999")
driver.find_element(By.NAME, "form_text_24").send_keys("Error")
driver.find_element(By.NAME, "form_textarea_28").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse euismod.")
driver.find_element(By.NAME, "captcha_word").click()
time.sleep(20)
driver.find_element(By.NAME, "web_form_submit").click()
notetext = driver.find_element(By.CLASS_NAME, 'notetext')
if notetext is None:
    print("Элемента нет")
else:
    print("Элемент есть")
time.sleep(5)
