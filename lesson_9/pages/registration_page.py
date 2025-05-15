from time import sleep
from selene import browser, be, have
import os
from lesson_9.data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_phone = browser.element('#userNumber')
        pass

    def open(self):
        browser.open('/automation-practice-form')
        sleep(2)
        browser.element('#fixedban').should(be.visible)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('header').remove()")
        return self

    def preconditions_met(self):
        browser.element('#app').should(be.visible)
        browser.element('#app').should(have.text('Practice Form'))
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('select').element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.user_email.type(value)
        return self

    def select_gender(self,gender):
        gender_mapping = {
            "Male": '[for="gender-radio-1"]',
            "Female": '[for="gender-radio-2"]',
            "Other": '[for="gender-radio-3"]',
        }
        browser.element(gender_mapping[gender]).click()
        return self

    def fill_user_phone(self, value):
        self.user_phone.type(value)
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self,hobbies):
        hobby_mapping = {
            "Sports": '[for="hobbies-checkbox-1"]',
            "Reading": '[for="hobbies-checkbox-2"]',
            "Music": '[for="hobbies-checkbox-3"]',
        }
        for hobby in hobbies.split(", "):
            browser.element(hobby_mapping[hobby]).click()
        return self

    def upload_img(self, picture):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'files', picture))
        browser.element('input[type="file"]').set_value(file_path)
        return self

    def fill_address(self,value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        browser.element('#submit').click()
        return self

    def registration(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_user_phone(user.phone_number)
        self.fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
        self.fill_subjects(user.subjects)
        self.fill_hobbies(user.hobbies)
        self.upload_img(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.click_submit_button()
        return self




    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth, language, hobbies, photo, address, city):
        browser.element('.table').all('td:nth-child(2)').should(have.exact_texts(
            full_name,
            email,
            gender,
            phone,
            date_of_birth,
            language,
            hobbies,
            photo,
            address,
            city))
        return self
