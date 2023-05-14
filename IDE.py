from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/ThundeRobot/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://qahacking.guru/index.php/about")
driver.set_window_size(1411, 812)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > .uk-active > a").click()
time.sleep(5)
driver.find_element(By.ID, "firstName").send_keys("Tatyana")
driver.find_element(By.ID, "lastName").send_keys("Zolotareva")
driver.find_element(By.ID, "userEmail").send_keys("mail@gmail.com")
driver.find_element(By.ID, "sex-1").click()
driver.find_element(By.ID, "userNumber").send_keys("89122554582")
driver.find_element(By.ID, "date").click()
driver.find_element(By.CSS_SELECTOR, "html").click()
driver.find_element(By.ID, "date").send_keys("11-12-2023")
driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.ID, "hobbies-checkbox-2").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
driver.find_element(By.ID, "currentAddress").click()
driver.find_element(By.ID, "currentAddress").send_keys("8 marta st 150")
driver.find_element(By.ID, "submit").click()
time.sleep(5)
