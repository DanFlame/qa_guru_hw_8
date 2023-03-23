from selene import have
from selene.support.shared import browser


def set_dropdown_value(locator, locator_option, value):
    browser.element(locator).click()
    browser.all(locator_option).element_by(have.exact_text(value)).click()
