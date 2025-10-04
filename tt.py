import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action= 'store', default='firefox',
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, end...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        #Для chrome добавить
        browser = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Ycheba/Safarov/Python/chromedriver.exe')
    elif browser_name == "firefox":
        print("\nstart firefox browser for test")
        browser = webdriver.Firefox(executable_path='C:/Temp/fsssd.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()