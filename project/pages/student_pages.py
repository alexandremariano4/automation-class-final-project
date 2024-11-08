from selenium.webdriver.common.by import By
from .base_page import BasePage

class StudentPage(BasePage):
    LOCATORS = {
        "student_id_input": (By.ID, "student-id"),
        "course_id_input": (By.ID, "course-id"),
        "course_subscription_button": (By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn"),
        "alert_message": (By.CSS_SELECTOR, ".py-p"),
        "alert_message2": (By.CSS_SELECTOR, ".py-p:nth-of-type(2)"),
        "subscribe_student_id": (By.ID, "subscribe-student-id"),
        "subscribe_discipline_id": (By.ID, "subscribe-discipline-id"),
        "subscribe_discipline_button": (By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn")
    }
    
    def subscribe_student_to_course(self, student_id, course_id):
        self.type_text(self.LOCATORS["student_id_input"], student_id)
        self.type_text(self.LOCATORS["course_id_input"], course_id)
        self.click(self.LOCATORS["course_subscription_button"])
    
    def subscribe_student_to_discipline(self, student_id, discipline_id):
        self.type_text(self.LOCATORS["subscribe_student_id"], student_id)
        self.type_text(self.LOCATORS["subscribe_discipline_id"], discipline_id)
        self.click(self.LOCATORS["subscribe_discipline_button"])
    
    def clear_discipline_id_field(self):
        self.driver.find_element(*self.LOCATORS["subscribe_discipline_id"]).clear()
    
    def get_alert_message(self):
        return self.get_text(self.LOCATORS["alert_message"])

    def get_alert_message2(self):
        return self.get_text(self.LOCATORS["alert_message2"])