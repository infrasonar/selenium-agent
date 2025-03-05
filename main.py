import os
import logging
from pylibagent.agent import Agent
from lib.check.checkSelenium import CheckSelenium
from lib.tests import TESTS
from lib.version import __version__ as version


if __name__ == '__main__':
    # Update ASSET_ID and set a default for the selenium agent
    ASSET_ID = os.getenv('ASSET_ID', '/data/.asset.json')
    os.environ['ASSET_ID'] = ASSET_ID

    checks = [CheckSelenium]
    agent = Agent('selenium', version)

    # logger is inited by now
    logging.warning(f'Number of tests: {len(TESTS)}')

    agent.start(checks, asset_kind='Website')
