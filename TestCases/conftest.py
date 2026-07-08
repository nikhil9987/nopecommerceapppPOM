from selenium import webdriver 
from pytest_metadata.plugin import metadata_key
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver =  webdriver.Chrome()
    elif browser == 'firefox':
        driver =  webdriver.firefox()
    else : driver =  webdriver.Edge()
    return driver

def pytest_addoption(parser):  # this will get the value from cli 
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):  #this will return  the browser value to setuo method
    return request.config.getoption('--browser')

######pytest html reports ######

# it is hook for adding environment info to html report 
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'testerName'

# it is hook for adding Environment info to html report 
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)

# from selenium import webdriver
# import pytest
# from pytest_metadata.plugin import metadata_key


# ###Browser Setup

# @pytest.fixture()
# def setup(browser):
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome()

#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox()

#     elif browser.lower() == "edge":
#         driver = webdriver.Edge()

#     else:
#         raise ValueError(f"Unsupported browser: {browser}")

#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     yield driver

#     driver.quit()

# #Command Line Option


# def pytest_addoption(parser):
#     parser.addoption(
#     "--browser",
#     action="store",
#     default="chrome",
#     help="Browser name: chrome, firefox or edge"
#     )

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


# ##Pytest HTML Report Metadata


# def pytest_configure(config):
#     config.stash[metadata_key]["Project Name"] = "nop Commerce"
#     config.stash[metadata_key]["Module Name"] = "Customers"
#     config.stash[metadata_key]["Tester"] = "testerName"

# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)