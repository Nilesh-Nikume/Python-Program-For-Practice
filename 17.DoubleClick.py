import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
Double_clk = driver.find_element(By.XPATH, "//*[text()='Copy Text']")
Action = ActionChains(driver)
Action.double_click(Double_clk).perform()

time.sleep(3)