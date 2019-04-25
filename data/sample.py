from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.millenniumhotels.com")
# driver.find_elements(By.ID,'opt-login')[1].click()
# driver.find_element(By.LINK_TEXT,"Sign in with Google").click()
# driver.find_element(By.ID,"identifierId").send_keys("liuyan061061@gmail.com")
# driver.find_elements(By.CLASS_NAME,"RveJvd")[0].click()
# sleep(3)
# driver.find_element(By.NAME,"password").send_keys("ly605402932")
# driver.find_elements(By.CLASS_NAME,"RveJvd")[0].click()
# sleep(3)
# driver.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/a[1]').click()
# driver.find_element(By.LINK_TEXT,"Sign Out").click()

wait = WebDriverWait(driver,10,0.5)
a = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cl-text")))[1].click()
# driver.find_elements(By.CLASS_NAME,"cl-text")[1].click()
sleep(5)
driver.find_element(By.XPATH,'.//ul[@class = "show-language"]/li[6]').click()
sleep(5)
destination = driver.find_element(By.CLASS_NAME,"hotel-title").text
assert destination == "特色目的地"
print(destination)

