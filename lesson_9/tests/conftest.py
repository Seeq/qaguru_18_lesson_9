import pytest, os
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_height = 800
    browser.config.window_width = 1280
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()