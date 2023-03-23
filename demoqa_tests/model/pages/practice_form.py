from selene import have, be
from selene.support.shared import browser
from demoqa_tests.model.controls import checkbox, datepicker, radiobutton, dropdown
from demoqa_tests.utils import image_path


def open_practice_form_page():
    browser.open('/automation-practice-form')


def set_first_name(first_name):
    browser.element('#firstName').should(be.blank).type(first_name)


def set_last_name(last_name):
    browser.element('#lastName').should(be.blank).type(last_name)


def set_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def set_gender(gender):
    radiobutton.select_by_value(browser.all('[name="gender"]'), gender)


def set_phone_number(phone_number):
    browser.element('#userNumber').should(be.blank).type(phone_number)


def set_birthday(day, month, year):
    datepicker.set_birth_date(day, month, year)


def set_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def set_hobby(hobby):
    checkbox.checkbox_click(browser.all('[for^=hobbies-checkbox]'), hobby)


def upload_picture(picture_path):
    image_path.upload_file('#uploadPicture', picture_path)


def set_address(address):
    browser.element('#currentAddress').type(address)


def set_state(state):
    dropdown.set_dropdown_value('#state', '[id^=react-select][id*=option]', state)


def set_city(city):
    dropdown.set_dropdown_value('#city', '[id^=react-select][id*=option]', city)


def assert_fields(*argument):
    browser.element('.table').all('td').even.should(have.texts(argument))


def submit_form():
    browser.element('#submit').press_enter()
