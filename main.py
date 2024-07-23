from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.LoginPage import LoginPage
from utils.MainPage import open
from utils.BasicSearch import seach_by_code, select_time
from utils.Proceed_and_Confirm import proceed_and_preview
from selenium.webdriver.chrome.options import Options

mock = True
wait = False
proceed_each = False
subject_list = [["COMP3423", "1011", [0]], ["AF3313", "1013", [0, 4]], ["COMP3438", "1011", [2, 5]], ["APSS2S07", "1000", [0]], ["COMP2121", "1011", [0, 2]]]
username = "your-username"
password = "your-password"


chrome_options = Options()
chrome_options.add_argument("--headless")  # 添加无头参数

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

login_page = LoginPage(driver)

try:
    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
except Exception as e:
    print("Login failed.", e)
print("Login finished. Mock is", mock)

try:
    open(driver, mock, wait)
    print("Subject registration page opened.")
    for subject in subject_list:
        seach_by_code(driver, subject[0], subject[1])
        select_time(driver, subject[2])
        if proceed_each:
            proceed_and_preview(driver, proceed_each)
    print("Select Finished.")
except Exception as e:
    print("Error", e)
try:
    if not proceed_each:
        print("Proceed and preview started.")
        proceed_and_preview(driver, proceed_each)
except Exception as e:
    print("Error", e)

print("Finished.")
input("Press Enter to quit.")
driver.quit()
