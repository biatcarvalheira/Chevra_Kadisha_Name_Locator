
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait



def close_driver(driver):
    driver.quit()

def make_request(url):
    driver = webdriver.Chrome(config.folder_path)
    driver.get(url)
    time.sleep(1)
    success = True
    print('Keep Chrome Window Open')
    return driver, success
def make_request_headless(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(config.folder_path, options=options)
    driver.get(url)
    time.sleep(1)
    success = True
    print('Loading url...')
    return driver, success



def insert_text(driver, xpath, input_text):
    wait = WebDriverWait(driver, 2)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(input_text)


def load_and_click(driver, xpath):

    try:
        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        label_content = element.text
        time.sleep(2)
        element.click()
        print('Selecting... ', label_content)
    except Exception as e:
        print("Unable to click element.")
        # Handle the case when the element is unclickable
        # Add your desired error handling code here
    time.sleep(2)
def load_and_click_longer(driver, xpath):
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(visibility_of_element_located((By.XPATH, xpath)))
        element.click()
        return True
    except Exception as e:
        print("Unable to click element:", str(e))
        # Handle the case when the element is unclickable
        # Add your desired error handling code here
        return False
    except TimeoutException as t:
        print('An error occurred... ', str(t))
        return False

    time.sleep(2)

def load_and_click_any (driver, selector, name):

    try:
        element = driver.find_element(selector, name)
        label_content = element.text
        time.sleep(1)
        element.click()
        print('Selecting... ', label_content)

    except Exception as e:
        print("Unable to click element:", str(e))
        # Handle the case when the element is unclickable
        # Add your desired error handling code here
        return False

    except TimeoutException as t:
        print('An error occurred... ', str(t))
        return False


def click_till_no_more(driver, xpath):
    while True:
        try:
            wait = WebDriverWait(driver, 2)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            time.sleep(5)  # Adjust the sleep time as needed
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
def click_if_clickable(driver, xpath):
    try:
        wait = WebDriverWait(driver, 3)
        button = wait.until(EC.element_to_be_clickable(xpath))
        button.click()
    except TimeoutException:
        raise Exception("Button not available")

def move_item_into_view(driver, xpath):
    try:
        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        time.sleep(1)
        # use JavaScript to scroll to the element
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # wait for the element to become visible
        ActionChains(driver).move_to_element(element).perform()
        element.click()
        time.sleep(1)
        return True
    except Exception as e:
        print('An error occured')
        return False
def items_found_message (list_name):
    print(len(list_name), 'vehicles were found.')
def display_list_number (counter):
    print(f'######## Loading information on item nº {counter} #######')
def move_into_view_no_click(driver, xpath):
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    time.sleep(1)
    # use JavaScript to scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", element)
    # wait for the element to become visible
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(1)

# scroll u
def scroll_page (driver, value):
    scroll_script = f"window.scrollBy(0, {value});"
    driver.execute_script(scroll_script)
def find_element (driver, selector, name):
    element = driver.find_element(selector, name)
    return element

def check_if_element_exists (driver, xpath):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))  # Replace with your locator
        return True
    except TimeoutException:
        print("Element does not exist")
        return False


