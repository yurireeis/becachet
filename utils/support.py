from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utils.constants import NOW, PRINT_FORMAT, WEBDRIVER


def wait_for_element(driver, locator=None, seconds=10):
    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.visibility_of_element_located(locator))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def wait_for_element_visible(driver, locator=None, seconds=5):
    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element visibility_of_any_elements_located
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.visibility_of_element_located(locator))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def wait_for_element_not_visible(driver, locator=None, seconds=5):
    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_elementvisibility_of_any_elements_located
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.invisibility_of_element_located(locator))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def wait_for_element_is_clickable(driver, locator=None, seconds=5):
    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.element_to_be_clickable(locator))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def wait_for_elements(driver, locator=None, seconds=10):
    """

    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.visibility_of_any_elements_located(locator))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def wait_for_text(driver, locator=None, text=None, seconds=10):
    """

    :param text: the text to be found
    :param driver: browser driver
    :param seconds: ten seconds in default mode, but you can set
    :type locator: web_element
    """
    wait = WebDriverWait(driver, seconds)
    try:
        return wait.until(ec.text_to_be_present_in_element(locator, text))
    except NoSuchElementException as err:
        print('Element not found: ', err.stacktrace)


def save_print(driver, step_name):
    filename = '{}_{}'.format(step_name.lower().replace(' ', '_'), NOW().strftime(PRINT_FORMAT))
    driver.get_screenshot_as_file('/tmp/{}.png'.format(filename))


def get_webdriver():
    """
    Return a webdriver object. You can call Chrome, Firefox or PhantomJS from command line
    :return:
    """
    if WEBDRIVER == 'chromedriver':
        return webdriver.Chrome()

    if WEBDRIVER == 'firefoxdriver':
        return webdriver.Firefox()

    return webdriver.PhantomJS()


def get_incident_text(scenarios):
    """

    :param scenarios: list
    :rtype: str
    """
    msg = 'Automatized tests fails in the following scenarios:\n'
    for step in scenarios:
        msg += '- {};\n'.format(step)
    return msg
