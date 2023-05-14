from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/ThundeRobot/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.metcom.ru/privat/mortgage/zayavka_na_ipotechnoe_kreditovanie/")
driver.set_window_size(1411, 812)
driver.find_element(By.ID, "form_dropdown_new_field_76788").click()
driver.find_element(By.XPATH, "//*[@id='form_dropdown_new_field_76788']/option[1]").click()
driver.find_element(By.ID, "form_dropdown_SIMPLE_QUESTION_332").click()
driver.find_element(By.XPATH, "//*[@id='form_dropdown_SIMPLE_QUESTION_332']/option[4]").click()
driver.find_element(By.NAME, "form_text_1355").send_keys("Петров Петр Петрович")
driver.find_element(By.NAME, "form_text_1356").send_keys("+79999999999")
driver.find_element(By.NAME, "form_text_1357").send_keys("С 12:00 до 18:00")
driver.find_element(By.NAME, "form_email_1358").send_keys("mail@gmail.com")
driver.find_element(By.NAME, "captcha_word").click()
time.sleep(10)
#Ввод капчи вручную
driver.find_element(By.NAME, "web_form_submit").click()
captcha = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/form/table/tbody/tr[8]/td[2]/img")
if captcha is None:
    print("Элемента нет")
else:
    print("Элемент есть")
time.sleep(5)
