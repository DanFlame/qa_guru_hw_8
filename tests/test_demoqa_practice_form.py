from demoqa_tests.model.pages import practice_form


def test_positive_fill_practice_form():
    practice_form.open_practice_form_page()
    practice_form.remove_ads()

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
