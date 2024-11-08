from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def wait_for_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()
    
    def type_text(self, locator, text):
        self.wait_for_element(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
    
    def get_text(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).text
