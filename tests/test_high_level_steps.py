from allure_commons.types import Severity

from tests_demo.users import users
from tests_demo.pages.registration_pages import RegistrationPage
import allure


@allure.tag('WEB')
@allure.title('Successful filled registration form')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Alexandra Borland')
@allure.feature('Registration form')
@allure.description('Data match')
def test_with_high_level_registration_page():
    user = users.Alexandra
    registration_page = RegistrationPage()

    with allure.step('Open the registration form'):
        registration_page.browser_open()

    with allure.step('Fill registration form'):
        registration_page.registration(user)

    with allure.step('Check results'):
        registration_page.submit_registration(user)
