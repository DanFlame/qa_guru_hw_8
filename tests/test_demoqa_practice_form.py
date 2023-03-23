from selene.support.shared import browser
from selene import have, be
import os
from demoqa_tests.model.pages import practice_form


def test_positive_fill_practice_form():
    practice_form.open_practice_form_page()

    # When
    practice_form.set_first_name('Daniel')
    practice_form.set_last_name('Fazylov')
    practice_form.set_email('daniel@test.ru')
    practice_form.set_gender('Male')
    practice_form.set_phone_number('8999123456')
    practice_form.set_birthday('25', '11', '1998')

    practice_form.set_subject('Computer Science')
    practice_form.set_hobby('Music')

    practice_form.upload_picture('resources/picture.png')

    practice_form.set_address('Indo st. 10')
    practice_form.set_state('Uttar Pradesh')
    practice_form.set_city('Agra')

    practice_form.submit_form()

    # Then
    practice_form.assert_fields(
        'Daniel Fazylov',
        'daniel@test.ru',
        'Male',
        '8999123456',
        '25 November,1998',
        'Computer Science',
        'Music',
        'picture.png',
        'Indo st. 10',
        'Uttar Pradesh Agra',
    )


# def test_student_registration_form():
#     browser.open('/automation-practice-form')
#     browser.element('#firstName').should(be.blank).type('Daniel')
#     browser.element('#lastName').type('Fazylov')
#     browser.element('#userEmail').type('daniel@test.com')
#     browser.all('[name="gender"]').element_by(have.value('Male')).element('..').click()
#     browser.element('#userNumber').type('89991234567')
#
#     browser.element('#dateOfBirthInput').click()
#     browser.element('.react-datepicker__month-select').click()
#     browser.element(f'[value="{10}"]').click()
#     browser.element('.react-datepicker__year-select').click()
#     browser.element(f'[value="{1998}"]').click()
#     browser.element(f'.react-datepicker__day--0{13}').click()
#
#     browser.element('#subjectsInput').type('Co')
#     browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Computer Science')).click()
#     browser.all('[for^=hobbies-checkbox]').element_by(have.(f'{Music}')).click()
#     browser.element('.form-control-file').set_value(
#         os.path.dirname(os.path.abspath(__file__))+'/tmp/picture.png'
#     )
#     browser.element('#currentAddress').type('Test Address')
#     browser.element('#state').click()
#     browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Uttar Pradesh')).click()
#     browser.element('#city').click()
#     browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Agra')).click()
#     browser.element('#submit').press_enter()
#     browser.element('.table').should(have.text(
#         'Daniel Fazylov' and
#         'daniel@test.com' and
#         'Male' and
#         '0123456789' and
#         '13 December,1900' and
#         'Computer Science' and
#         'Music' and
#         'picture.png' and
#         'Test Address' and
#         'Uttar Pradesh Merrut'
#     ))
