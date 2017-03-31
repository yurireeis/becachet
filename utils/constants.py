import os
import datetime


from cachet.cachet import Cachet

CACHET_URL = os.getenv('CACHET_URL', None)
CACHET_TOKEN = os.getenv('CACHET_TOKEN', None)
WEBDRIVER = os.getenv('WEBDRIVER', None)
CACHET_API = Cachet() if CACHET_URL and CACHET_TOKEN else None
NOW = datetime.now
PRINT_FORMAT = '%d_%m_%Y_%H_%M_%S'
