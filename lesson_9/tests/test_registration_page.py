from lesson_9.data.users import user
from lesson_9.pages.registration_page import RegistrationPage


def test_register_user(setup_browser):
    registration_page = RegistrationPage()
    (registration_page.open()
     .registration(user)
     .should_registered_user_with(user))
