from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def seach_by_code(driver, sub_code, component):
    try:
        input_box = driver.find_element(By.XPATH, '// *[ @ id = "mainForm:basicSearchSubjectCode"]')
        input_box.clear()
        input_box.send_keys(sub_code)
        search_button = driver.find_element(By.XPATH, '//*[@id="mainForm:basicSearchButton"]')
        search_button.click()
        select_element = driver.find_element(By.XPATH, '//*[@id="mainForm:basicSearchTable:0:basicSearchSubjectGroup_"]')
        select = Select(select_element)
        for option in select.options:
            if component in option.text:
                option.click()
                break
        add_button = driver.find_element(By.XPATH,
                                         '//*[@id="mainForm:basicSearchTable:0:basicSearchAddSubjectButton_"]')
        add_button.click()
    except Exception as e:
        raise Exception(f"Search implementation failed: {str(e)}")


def select_time(driver, time_slot):
    try:
        for num in time_slot:
            time_slot_button = driver.find_element(By.XPATH,
                                                   f'//*[@id="mainForm:ComponentTable:{num}:selectCompSelected_"]')
            time_slot_button.click()
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="mainForm:selectButton"]')
        add_to_cart_button.click()
    except Exception as e:
        raise Exception(f"Time slot selection failed: {str(e)}")
