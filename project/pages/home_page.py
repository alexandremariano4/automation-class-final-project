from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    URL = "https://tdd-detroid.onrender.com/"
    
    LOCATORS = {
        "loading_splash": (By.ID, 'pyscript_loading_splash'),
        "student_name_input": (By.ID, "student-nome"),
        "student_button": (By.ID, "student-btn"),
        "course_name_input": (By.ID, "course-nome"),
        "course_button": (By.ID, "course-btn"),
        "alert_message": (By.CSS_SELECTOR, ".py-p"),
        "discipline_name_input": (By.ID, "discipline-nome"),
        "course_discipline_id_input": (By.ID, "course-discipline-id"),
        "discipline_button": (By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")
    }
    
    def load(self):
        self.driver.get(self.URL)
        self.wait_for_element(self.LOCATORS["loading_splash"])
    
    def add_student(self, student_name):
        self.type_text(self.LOCATORS["student_name_input"], student_name)
        self.click(self.LOCATORS["student_button"])
    
    def add_course(self, course_name):
        self.type_text(self.LOCATORS["course_name_input"], course_name)
        self.click(self.LOCATORS["course_button"])
    
    def add_discipline(self, discipline_name, course_id):
        self.type_text(self.LOCATORS["discipline_name_input"], discipline_name)
        self.type_text(self.LOCATORS["course_discipline_id_input"], course_id)
        self.click(self.LOCATORS["discipline_button"])
    
    def get_alert_message(self):
        return self.get_text(self.LOCATORS["alert_message"])
    
    def double_click_course_name(self):
        element = self.driver.find_element(*self.LOCATORS["course_name_input"])
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
