import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://demoqa.com/')
browser.maximize_window()


wait = WebDriverWait(browser, 20) 

alerts_frame_windows_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card-body']//h5[text()='Alerts, Frame & Windows']")))
time.sleep(2)
alerts_frame_windows_btn.click()

browser_windows_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']")))
time.sleep(2)
browser_windows_btn.click()

new_window_btn = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
time.sleep(2)
new_window_btn.click()

all_windows = browser.window_handles
browser.switch_to.window(all_windows[1])

assert "This is a sample page" in browser.page_source
print("A mensagem 'This is a sample page' foi encontrada na nova janela!")

browser.close()

browser.switch_to.window(all_windows[0])
time.sleep(2)

browser.quit()
