from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/")

wait = WebDriverWait(driver, 20)

interactions_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card-body'][contains(., 'Interactions')]")))
interactions_button.click()

sortable_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sortable']")))
sortable_button.click()

sortable_items = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='vertical-list-container mt-4']/div")))

for item in sortable_items:
    driver.execute_script("arguments[0].scrollIntoView({ inline: 'center' });", item)
    time.sleep(0.5)

time.sleep(2)

print("Ordem inicial dos itens:")
for item in sortable_items:
    print(item.text)

desired_order = ["one", "two", "three", "four", "five", "six"]

actions = ActionChains(driver)

for desired_text in desired_order:
    sortable_items = driver.find_elements(By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    current_item = next(item for item in sortable_items if item.text.lower() == desired_text)
    target_index = desired_order.index(desired_text)
    target_position = sortable_items[target_index]
    driver.execute_script("arguments[0].scrollIntoView({ inline: 'center' });", current_item)
    time.sleep(0.5)
 
    if current_item != target_position:
        actions.click_and_hold(current_item).move_to_element(target_position).release().perform()
        time.sleep(1)
    else:
        print(f"{desired_text} já está na posição correta.")

    sortable_items = driver.find_elements(By.XPATH, "//div[@class='vertical-list-container mt-4']/div")

updated_items = driver.find_elements(By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
print("Ordem final dos itens:")
for item in updated_items:
    print(item.text)

time.sleep(3)

driver.quit()
