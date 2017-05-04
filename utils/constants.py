import os
from datetime import datetime

CACHET_URL = os.getenv('CACHET_URL', None)
CACHET_TOKEN = os.getenv('CACHET_TOKEN', None)
CACHET_INTEGRATION = os.getenv('CACHET_TOKEN', False)
NOW = datetime.now
PRINT_FORMAT = '%d_%m_%Y_%H_%M_%S'
