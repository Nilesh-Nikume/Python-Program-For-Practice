from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.implicitly_wait(5) # it will wait till 5 sec to load complete elements from this page

driver.close()