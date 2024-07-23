import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def open(driver, mock, wait):
    if mock:
        try:
            driver.find_element(By.XPATH, "//a[contains(@href, 'mock')]").click()
            try:
                driver.find_element(By.XPATH, "//*[contains(text(),'This function is not available.')]")
                print("Mock registration is not available.")
            except NoSuchElementException:
                print("Mock Registration is available.")
            driver.find_element(By.XPATH, "//*[@id='mainForm:nextButton']").click()
        except Exception as e:
            raise Exception(f"Mock registration failed: {str(e)}")
    else:
        try:
            driver.find_element(By.XPATH,
                                "//a[@href='/eStudent/secure/my-subject-registration/subject-register-select-acad-year-sem.jsf']").click()
            try:
                driver.find_element(By.XPATH, "//*[contains(text(),'This function is not available.')]")
                print("Registration is not available.")
                if wait:
                    print("Wait for registration to be available.....")
                    while True:
                        driver.refresh()
                        try:
                            driver.find_element(By.XPATH, "//*[contains(text(),'This function is not available.')]")
                            print("Registration is not available.")
                            time.sleep(0.5)
                        except:
                            break
            except NoSuchElementException:
                print("Registration is available.")
            driver.find_element(By.XPATH, "//*[@id='mainForm:nextButton']").click()
        except Exception as e:
            raise Exception(f"Registration failed: {str(e)}")
