import os
import logging
from typing import Dict, List, Any
from pylibagent.check import CheckBase
from selenium import (
    Selenium,
    ConfigRetrievalError,
    ServersRetrievalError,
    InvalidServerIDType,
    HTTP_ERRORS,
    NoMatchedServers)
from ..version import __version__ as version


class CheckSelenium(CheckBase):
    key = 'selenium'
    interval = int(os.getenv('CHECK_INTERVAL', '3600'))

    download = not bool(int(os.getenv('NO_DOWNLOAD', '0')))
    upload = not bool(int(os.getenv('NO_UPLOAD', '0')))
    single = bool(int(os.getenv('SINGLE', '0')))
    source = os.getenv('SOURCE', None)
    timeout = int(os.getenv('TIMEOUT', '10'))
    secure = bool(int(os.getenv('SECURE', '0')))

    @classmethod
    async def run(cls) -> Dict[str, List[Dict[str, Any]]]:

        # Find base classes and run selenium checks.
        # Each Selenium check results in an item.
        # Agent type contains the agent version
        # Overall contains number of checks success, total duration etc.
        state = {'selenium': [], 'agent': [], 'overall': []}
        return state
