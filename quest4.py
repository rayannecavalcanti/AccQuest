from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://demoqa.com/")

    widgets_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='card-body'][normalize-space() = 'Widgets']"))
    )
    widgets_button.click()
    
    progress_bar_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space() = 'Progress Bar']"))
    )
    progress_bar_button.click()
    time.sleep(2)

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "startStopButton"))
    )
    start_button.click()

    while True:
        time.sleep(0.5)
        
        progress_value = driver.find_element(By.CLASS_NAME, "progress-bar")
        progress_percentage = int(progress_value.get_attribute("aria-valuenow"))

        if progress_percentage == 25:
            stop_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "startStopButton"))
            )
            stop_button.click()
            print(f"Progresso atingiu 25%.")
            break
            
    time.sleep(2)

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "startStopButton"))
    )
    start_button.click()

    while True:
        time.sleep(0.5)
        
        progress_value = driver.find_element(By.CLASS_NAME, "progress-bar")
        progress_percentage = int(progress_value.get_attribute("aria-valuenow"))
        
        if progress_percentage == 100:
            reset_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "resetButton"))
            )
            time.sleep(1)
            reset_button.click()
            print("Progresso atingiu 100%. Barra reiniciada.")
            break

finally:
    time.sleep(2)
    driver.quit()
