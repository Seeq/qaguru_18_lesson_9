from lesson_9.data.users import user
from lesson_9.pages.registration_page import RegistrationPage



def test_register_user(setup_browser):
    registration_page = RegistrationPage()
    (registration_page.open()
     .registration(user)
     .should_registered_user_with(user))

def test_complete_form(setup_browser):
    RegistrationPage()\
        .open()\
        .preconditions_met()\
        .fill_first_name("Sergey")\
        .fill_last_name("Labov")\
        .fill_email("qaguru@nosuchdomain.net")\
        .select_gender()\
        .fill_user_phone("9111002030")\
        .fill_date_of_birth('1989', '7', '017')\
        .fill_subjects("English")\
        .fill_hobbies()\
        .upload_img()\
        .fill_address("First street, Second house, Third app.")\
        .select_state()\
        .select_city()\
        .click_submit_button()\
        .should_registered_user_with(
            "Sergey Labov",
            "qaguru@nosuchdomain.net",
            "Male",
            "9111002030",
            "17 August,1989",
            "English",
            "Sports, Reading, Music",
            "meme.png",
            "First street, Second house, Third app.",
            "Rajasthan Jaiselmer")
