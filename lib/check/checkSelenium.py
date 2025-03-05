import importlib
import sys
import time
import os
import logging
from inspect import getmembers, isclass
from typing import Dict, List, Any
from pylibagent.check import CheckBase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .. import TestBase
from ..version import __version__ as version


# TODO should we do this loop at module level?
# should we raise error when no tests are found?
TESTS_DIR = os.getenv('TESTS_DIR', '/data/tests')
assert os.path.isdir(TESTS_DIR), 'invalid TEST_DIR'
sys.path.append(TESTS_DIR)

TESTS: List[TestBase] = []
for fn in sorted(os.listdir(TESTS_DIR)):
    if not fn.endswith('.py'):
        continue
    mod = importlib.import_module(fn[:-3])
    for _, cls in getmembers(mod, isclass):
        if TestBase in cls.__bases__:
            TESTS.append(cls)

assert TESTS, 'no tests found'


class CheckSelenium(CheckBase):
    key = 'selenium'
    interval = int(os.getenv('CHECK_INTERVAL', '300'))

    @classmethod
    async def run(cls) -> Dict[str, List[Dict[str, Any]]]:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

        items = []
        for mod in TESTS:
            t0 = time.time()
            success = True
            error = None
            try:
                driver.get(mod.url)
                mod.run(driver)
            except Exception as e:
                success = False
                error = str(e) or type(e).__name__
            items.append({
                'name': mod.name,
                'url': mod.url,
                'success': success,
                'error': error,
                'duration': time.time() - t0,
                'description': mod.description,
            })

        driver.quit()

        total = {
            'name': 'total',
            'success_count': sum(i['success'] for i in items),
            'failed_count': sum(not i['success'] for i in items),
            'num_checks': len(items),
            'total_duration': sum(i['duration'] for i in items),
        }
        state = {'selenium': items, 'total': [total]}
        return state
