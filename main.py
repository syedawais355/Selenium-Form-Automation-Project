import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def fill(driver, by, value, action="send", data=None):
    """
    Finds a web element, scrolls it into view, and performs an action.

    Args:
        driver: The Selenium WebDriver instance.
        by: The locator strategy (e.g., By.ID, By.NAME).
        value: The locator value.
        action: The action to perform ("send", "click", or "select").
        data: The data to be sent or selected.
    """
    try:
        element = driver.find_element(by, value)
        driver.execute_script("arguments.scrollIntoView({block: 'center'});", element)
        time.sleep(0.2)

        if action == "send":
            element.send_keys(data)
        elif action == "click":
            element.click()
        elif action == "select":
            Select(element).select_by_visible_text(data)
    except Exception as e:
        print(f"An error occurred while trying to interact with element ({by}, {value}): {e}")

def main():
    """
    Main function to run the Selenium automation script.
    """
    driver = webdriver.Chrome()
    driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")

    try:
        fill(driver, By.ID, "prefix", "select", "Mr.")
        fill(driver, By.ID, "firstname", "send", "Awais")
        fill(driver, By.ID, "lastname", "send", "Gillani")
        fill(driver, By.ID, "pension", "click")
        fill(driver, By.NAME, "fathername", "send", "Qayyoum")
        fill(driver, By.NAME, "mothername", "send", "Shaheen")
        fill(driver, By.ID, "studentid", "click")
        fill(driver, By.ID, "identity_number", "send", "1234567890")
        fill(driver, By.ID, "male", "click")
        fill(driver, By.ID, "dob_month", "select", "March")
        fill(driver, By.ID, "dob_date", "select", "1")
        fill(driver, By.ID, "dob_year", "select", "2008")
        fill(driver, By.ID, "single", "click")
        fill(driver, By.ID, "country_code", "select", "India (+91)")
        fill(driver, By.ID, "mobile", "send", "3123456790")
        fill(driver, By.ID, "nationality", "select", "Indian")
        fill(driver, By.NAME, "address", "send", "Gechs")
        fill(driver, By.ID, "state", "send", "dehli")
        fill(driver, By.ID, "country", "select", "India")

        time.sleep(1)

        fill(driver, By.XPATH, "//input[@value='Submit']", "click")

        try:
            alert = driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
            print("Alert accepted.")
        except Exception as e:
            print(f"No alert was present or an error occurred: {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
