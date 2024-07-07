import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

try:
    # Initialize the WebDriver with options
    chrome_options = Options()
    # Setup WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # Navigate to the IMDb Name Search page
    driver.get("https://www.imdb.com/search/name/")

    wait = WebDriverWait(driver, 10)
    driver.execute_script("window.scrollTo(500, 500);")
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span')))
    name_input.click()
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="text-input__62733"]')))
    search_input.send_keys("lakshmi")
    # Click on the "Credits" filter
    credits_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label')))
    credits_filter.click()
    time.sleep(2)
    credit_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')))
    actions = ActionChains(driver)
    actions.send_keys_to_element(credit_input, "Holiday").pause(2).send_keys(Keys.DOWN).pause(1).send_keys(Keys.ENTER).perform()

    print("Search performed successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()
