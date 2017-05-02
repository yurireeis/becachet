from selenium.webdriver.common.by import By

from utils.support import wait_for_element

DASHBOARD_BUTTON = (By.XPATH, '//a[@href="/dashboard"]')
USERNAME_FIELD = (By.NAME, 'username')
PASSWORD_FIELD = (By.NAME, 'password')
LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
USERNAME_LABEL = (By.CLASS_NAME, 'username')


def login(driver, credentials: tuple):
    """

    :param driver: instance of a navigator (browser)
    :type driver: webdriver
    :param credentials: tuple with user/password info
    :type credentials: tuple
    :rtype: bool
    """
    wait_for_element(driver, DASHBOARD_BUTTON).click()
    wait_for_element(driver, USERNAME_FIELD).send_keys(credentials[0])
    wait_for_element(driver, PASSWORD_FIELD).send_keys(credentials[1])
    wait_for_element(driver, LOGIN_SUBMIT_BUTTON).click()

    found_username = wait_for_element(driver, USERNAME_LABEL).text

    if found_username == credentials[0]:
        return True

    return False
