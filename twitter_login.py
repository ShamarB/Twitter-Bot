from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

wait = WebDriverWait(driver, 10)
username = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')))
username.send_keys('shamarbot')

password = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')))
password.send_keys('5k8t3rb0y')

login_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div')))
login_button.click()

tweet_bar = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')))
tweet_bar.send_keys('Hello World, live from Seattle')

tweet_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')))
tweet_button.click()
