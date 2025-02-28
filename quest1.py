import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import modules


browser = webdriver.Chrome()

browser.get('https://demoqa.com/')
browser.maximize_window()


forms_btn = browser.find_element(By.XPATH, '//div[@class="card-body"]//h5[text()="Forms"]')
forms_btn.click()

practice_btn = browser.find_element(By.XPATH, "//span[text()='Practice Form']")
practice_btn.click()

first_name = browser.find_element(By.ID, "firstName")
first_name.send_keys(modules.first_name())
time.sleep(1)

last_name = browser.find_element(By.ID, "lastName")
last_name.send_keys(modules.last_name())
time.sleep(1)

browser.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")

email = browser.find_element(By.ID, "userEmail")
email.send_keys(modules.email())
time.sleep(1)

gender_name = modules.gender()
gender=browser.find_element(By.XPATH, f"//label[text()='{gender_name}']")
gender.click()
time.sleep(1)

mobile_number = browser.find_element(By.ID, "userNumber")
mobile_number.send_keys(modules.mobile_number())
time.sleep(1)

date_of_birth =browser.find_element(By.ID, "dateOfBirthInput")
date_of_birth.click()
date_of_birth.send_keys(Keys.CONTROL + "a")
date_of_birth.send_keys(modules.date_of_birth())
date_of_birth.send_keys(Keys.ENTER)
time.sleep(1)

subjects = browser.find_element(By.ID, "subjectsInput")
subjects.send_keys("Math")
time.sleep(1)
subjects.send_keys(Keys.ENTER)
time.sleep(1)

hobbies_name = f"//label[text()='{modules.hobbies()}']"
hobbies_field = browser.find_element(By.XPATH, hobbies_name)
hobbies_field.click()
time.sleep(1)

file_path = os.path.abspath("example.txt")
upload_input = browser.find_element(By.ID, "uploadPicture")
upload_input.send_keys(file_path)
time.sleep(1)


current_address = browser.find_element(By.ID, "currentAddress")
current_address.send_keys(modules.current_address())
time.sleep(1)

wait = WebDriverWait(browser, 10)

state_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "state")))
state_dropdown.click()

state_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'css-yt9ioa-option')]")))
selected_state = random.choice(state_options)
selected_state_text = selected_state.text
selected_state.click()
time.sleep(2)

city_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "city")))
city_dropdown.click()

city_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'css-yt9ioa-option')]")))
random.choice(city_options).click()

submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
submit_button.click()

popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='closeLargeModal']")))
time.sleep(2)
close_button.click()

time.sleep(1)
browser.quit()
