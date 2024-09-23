from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#Click a button automated test
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()




driver.get("https://kiosk.spacejat.com/link/aARezOCw40")
expected_title = "SpaceJAT"
driver.implicitly_wait(30)

print(expected_title)




Z: WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/button[2]')
Z.click()
expected_title = "Test last sprint"
driver.implicitly_wait(30)
print(expected_title)

Z1: WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/button/img')
Z1.click()
driver.implicitly_wait(30)



First_Name: WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/input')
First_Name.send_keys('Hager')
driver.implicitly_wait(30)

Last_Name:WebElement = driver.find_element(by=By.XPATH,value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/input')
Last_Name.send_keys('Mahmoud')
driver.implicitly_wait(30)

Business_Email:WebElement = driver.find_element(by=By.XPATH,value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[3]/input')
Business_Email.send_keys('hager@jatdev.com')
driver.implicitly_wait(30)

Job_Title:WebElement = driver.find_element(by=By.XPATH,value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[4]/input')
Job_Title.send_keys('QA Engineer')
driver.implicitly_wait(30)

Mobile:WebElement = driver.find_element(by=By.XPATH,value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[5]/input')
Mobile.send_keys('01090834925')
driver.implicitly_wait(30)
print(expected_title)

Create_Button:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[7]/button[2]')
Create_Button.click()

driver.implicitly_wait(50)

Join_Button:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[4]/button[2]')
Join_Button.click()
expected_title = "Select your identity"
driver.implicitly_wait(50)
print(expected_title)

Inbox_Button:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[53]/div[2]/div[1]/div[3]/div[4]/div')
Inbox_Button.click()
driver.implicitly_wait(50)


Start_Chatting_Button:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[72]/div[1]/div/div[2]/div/button[2]')
Start_Chatting_Button.click()
actual_url = driver.current_url
expected_url = "https://dashboard.spacejat.com/home"
driver.implicitly_wait(50)
print("URL Comparison:", actual_url == expected_url)


Start_Chatting_Button:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[72]/div[1]/div/div[2]/div/button[2]')
Start_Chatting_Button.click()
driver.implicitly_wait(50)



wait = WebDriverWait(driver, 10)

chatting_button = wait.until(EC.element_to_be_clickable((By.ID, 'focusInput')))
chatting_button.click()
chatting_button.send_keys('Hi')
# driver.implicitly_wait(50)



Send:WebElement = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div[1]/div[2]/div[3]/aside/div/div/div[3]/div/button[2]')
Send.click()
driver.implicitly_wait(50)






