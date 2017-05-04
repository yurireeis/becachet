import os
import datetime
from cachet.cachet import Cachet

WEBDRIVER = os.getenv('WEBDRIVER', None)
CACHET_API = Cachet()
NOW = datetime.now
PRINT_FORMAT = '%d_%m_%Y_%H_%M_%S'
