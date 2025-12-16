from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# start the selenium browser session
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome()
# load desired page in the browser
driver.get("https://www.sunbeaminfo.in")
driver.maximize_window()
time.sleep(3)
print("Page Title:", driver.title)
# define wait strategy
#driver.implicitly_wait(5)
# interact with web controls
#list_item = driver.find_elements(By.XPATH,f"//a[@href='internship']")[1]
#list_item.send_keys(Keys.RETURN)
# wait = WebDriverWait(driver,20)
Internship = driver.find_element(By.XPATH,"//nav//a[normalize-space()='Internship']") # Replace "Sign in" with the link's exact visible text
    
    # 4. Click the link
Internship.click()
# print("Link clicked successfully!")
time.sleep(5)

driver.implicitly_wait(5)
# get Internship Batches Schedule
table_body = driver.find_elements(By.TAG_NAME, "tbody")[2]
table_rows = table_body.find_elements(By.TAG_NAME, "tr")
for row in table_rows:
    # print(row.text)
    cols = row.find_elements(By.TAG_NAME, "td")
    info = {
        "sr": cols[0].text,
        "title": cols[1].text,
        "author": cols[2].text,
        "category": cols[3].text,
        "price": cols[4].text
    }
    print(info)

#Available Internship Programs
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# wait for and click the "Available Internship Programs" toggle button
plus_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#collapseSix']")))
driver.execute_script("arguments[0].scrollIntoView(true);", plus_button)
plus_button.click()

#InternshipProg = driver.find_element(By.XPATH,"//nav//a[normalize-space()='Available Internship Programs']") # Replace "Sign in" with the link's exact visible text
    
    # 4. Click the link
#InternshipProg.click()
# print("Link clicked successfully!")
time.sleep(5)

driver.implicitly_wait(5)

table_body = driver.find_elements(By.TAG_NAME, "tbody")[1]
table_rows = table_body.find_elements(By.TAG_NAME, "tr")
for row in table_rows:
    # print(row.text)
    cols = row.find_elements(By.TAG_NAME, "td")
    info = {
        "sr": cols[0].text,
        "title": cols[1].text,
        "author": cols[2].text,
        "category": cols[3].text,
        "price": cols[4].text
    }
    print(info)
# stop the session
driver.quit()