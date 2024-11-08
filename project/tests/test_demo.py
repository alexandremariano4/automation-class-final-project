import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.student_pages import StudentPage
import datetime

class TestDemo:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--disk-cache-size=0")
        self.driver = webdriver.Chrome(options=options)
        self.home_page = HomePage(self.driver)
        self.student_page = StudentPage(self.driver)
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_demo(self):
        self.home_page.load()
        
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(('id','pyscript_loading_splash')))

        
        # Step 1: Add student
        self.home_page.add_student("douglas")
        actual_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        assert actual_date in self.home_page.get_alert_message()
        assert 'douglas' in self.home_page.get_alert_message()
        
        # Step 2: Add course
        self.home_page.add_course("mat")
        assert actual_date in self.home_page.get_alert_message()
        assert 'mat' in self.home_page.get_alert_message()
        
        # Step 3: Subscribe student to course
        self.student_page.subscribe_student_to_course("1", "1")
        assert "Student id 1 subscribed to course id 1" in self.student_page.get_alert_message()
        
        # Step 4: Add second course
        self.home_page.double_click_course_name()
        self.home_page.add_course("port")
        assert "Added course id: 2, Nome: port" in self.home_page.get_alert_message()
        
        # Step 5: Add third course
        self.home_page.double_click_course_name()
        self.home_page.add_course("geo")
        assert "Added course id: 3, Nome: geo" in self.home_page.get_alert_message()
        
        # Step 6: Add discipline
        self.home_page.add_discipline("mat", "1")
        assert actual_date in self.home_page.get_alert_message()
        assert "Added discipline id: 1, Name: mat, Course: 1" in self.home_page.get_alert_message()
        
        # Step 7: Add more disciplines and subscribe student to them
        self.home_page.add_discipline("mat2", "1")
        self.home_page.add_discipline("mat3", "1")
        
        # Attempt to subscribe to discipline before 3 disciplines
        self.student_page.subscribe_student_to_discipline("1", "1")
        assert "Aluno deve se inscrever em 3 materias no minimo" in self.student_page.get_alert_message()
        
        # Subscribe student to more disciplines
        self.student_page.clear_discipline_id_field()
        self.student_page.subscribe_student_to_discipline("1", "2")
        assert "Student id 1, Name douglas subscribed to discipline id 2" in self.student_page.get_alert_message2()
        
        self.student_page.clear_discipline_id_field()
        self.student_page.subscribe_student_to_discipline("1", "3")
        assert "Student id 1, Name douglas subscribed to discipline id 3" in self.student_page.get_alert_message()
        
        # Add final discipline and verify subscription
        self.home_page.add_discipline("mat4", "1")
        assert "Added discipline id: 4, Name: mat4, Course: 1" in self.home_page.get_alert_message()
        
        self.student_page.clear_discipline_id_field()
        self.student_page.subscribe_student_to_discipline("1", "4")
        assert "Student id 1, Name douglas subscribed to discipline id 4" in self.student_page.get_alert_message()
        
        # Close the driver
        self.driver.close()
