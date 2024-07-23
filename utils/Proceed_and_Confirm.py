from selenium.webdriver.common.by import By



def proceed_and_preview(driver, proceed_each):
    proceed_button = driver.find_element(By.XPATH,'//*[@id="mainForm:confirmButton"]')
    proceed_button.click()
    confirm_button = driver.find_element(By.XPATH, '//*[@id="mainForm:confirmButton"]')
    confirm_button.click()
    if proceed_each:
        driver.back()
        driver.back()
