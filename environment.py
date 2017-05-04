from cachet.cachet import Cachet
from utils.constants import CACHET_TOKEN, CACHET_URL, CACHET_INTEGRATION
from utils.support import save_print, get_webdriver, get_incident_text


def before_feature(context, feature):
    context.failed_scenario = []


def before_all(context):
    """

    :type context: object
    """
    context.browser = get_webdriver()
    context.browser.get('https://qa.socialbase.com.br')


def after_feature(context, feature):
    if feature.status == "failed" and CACHET_INTEGRATION:
        text = get_incident_text(context.failed_scenario)
        Cachet(CACHET_URL, CACHET_TOKEN).post_incidents(feature.name, text, 0, 0)


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if step.status == 'failed':
        save_print(context.browser, context.step.name)
