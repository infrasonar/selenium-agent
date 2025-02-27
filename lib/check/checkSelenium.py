import importlib
import time
import os
import logging
from typing import Dict, List, Any
from pylibagent.check import CheckBase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..version import __version__ as version


item_funs = []
for fn in sorted(os.listdir('recipes')):
    if not fn.endswith('.py'):
        continue
    mod = importlib.import_module(f'recipes.{fn[:-3]}')
    if not hasattr(mod, 'NAME'):
        continue
    if not hasattr(mod, 'URL'):
        continue
    if not hasattr(mod, 'DESCRIPTION'):
        continue
    if not hasattr(mod, 'run'):
        continue
    item_funs.append(mod)


class CheckSelenium(CheckBase):
    key = 'selenium'
    interval = int(os.getenv('CHECK_INTERVAL', '300'))

    @classmethod
    async def run(cls) -> Dict[str, List[Dict[str, Any]]]:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

        items = []
        for mod in item_funs:
            t0 = time.time()
            success = True
            error = None
            try:
                mod.run(driver)
            except Exception as e:
                success = False
                error = str(e) or type(e).__name__
            items.append({
                'name': mod.NAME,
                'url': mod.URL,
                'success': success,
                'error': error,
                'duration': time.time() - t0,
                'description': mod.DESCRIPTION,
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
