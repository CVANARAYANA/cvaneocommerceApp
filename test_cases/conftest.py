import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching the chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching the edge browser")
    else:
        driver = webdriver.Chrome()

    return driver


def pytest_addoption(parser):  #This is will get the value from the CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This is will return the browser value to setup method
    return request.config.getoption("--browser")


############ Pytest HTML Reports ##################3

#It is hook adding environment for info to HTML Reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Cva'

#It is hook for delete/Modify Environment info to HTML Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
