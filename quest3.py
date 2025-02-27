from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/")
time.sleep(2)

elements_section = driver.find_element(By.XPATH, "//h5[text()='Elements']")
elements_section.click()
time.sleep(2)

web_tables = driver.find_element(By.XPATH, "//span[text()='Web Tables']")
web_tables.click()
time.sleep(2)

add_button = driver.find_element(By.ID, "addNewRecordButton")
add_button.click()
time.sleep(2)

first_name = modules.first_name()
last_name = modules.last_name()
user_email = modules.email()
age = str(random.randint(18, 65))
salary = str(random.randint(30000, 150000))
department = random.choice(["QA", "Development", "HR", "Marketing", "Sales"])

driver.find_element(By.ID, "firstName").send_keys(first_name)
time.sleep(1)
driver.find_element(By.ID, "lastName").send_keys(last_name)
time.sleep(1)
driver.find_element(By.ID, "userEmail").send_keys(user_email)
time.sleep(1)
driver.find_element(By.ID, "age").send_keys(age)
time.sleep(1)
driver.find_element(By.ID, "salary").send_keys(salary)
time.sleep(1)
driver.find_element(By.ID, "department").send_keys(department)
time.sleep(1)

driver.find_element(By.ID, "submit").click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
last_record_row = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='rt-tr-group'])[last()]")))

edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@title='Edit'])[last()]")))

edit_button.click()
time.sleep(2)

data_map = {
    "firstName": modules.first_name(),
    "lastName": modules.last_name(),
    "userEmail": modules.email(),
    "age": str(random.randint(18, 65)),
    "salary": str(random.randint(30000, 150000)),
    "department": random.choice(["QA", "Development", "HR", "Marketing", "Sales"])
}

field_to_edit = random.choice(list(data_map.keys()))
edit_field = driver.find_element(By.ID, field_to_edit)
edit_field.clear()
time.sleep(1)
edit_field.send_keys(data_map[field_to_edit])
time.sleep(1)

driver.find_element(By.ID, "submit").click()
time.sleep(2)

delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@title='Delete'])[last()]")))

delete_button.click()
time.sleep(2)

driver.quit()
