import abc
import time
from selenium import webdriver
from typing import Optional


class TestBase(abc.ABC):
    url: str
    name: str
    description: str
    version: str

    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, 'url'):
            raise NotImplementedError('`url` not implemented')
        if not isinstance(cls.url, str):
            raise NotImplementedError('`url` must be type str')
        if not hasattr(cls, 'name'):
            raise NotImplementedError('`name` not implemented')
        if not isinstance(cls.name, str):
            raise NotImplementedError('`name` must be type str')
        if not hasattr(cls, 'description'):
            raise TypeError('`description` not implemented')
        if not isinstance(cls.description, str):
            raise TypeError('`description` must be type str')
        if not hasattr(cls, 'version'):
            raise TypeError('`version` not implemented')
        if not isinstance(cls.version, str):
            raise TypeError('`version` must be type str')
        return super().__init_subclass__(**kwargs)

    @classmethod
    def run(cls, driver: Optional[webdriver.Chrome]=None):
        '''
        Can be used to run the test

        Argument `driver` can be use to specifiy a (local) webdriver
        When not given it defaults to the remote chrome webdriver
        '''
        if driver is None:
            options = webdriver.ChromeOptions()
            driver = webdriver.Remote(options=options)

        t0 = time.time()
        try:
            driver.get(cls.url)
            cls.test(driver)
        except Exception as e:
            error = str(e) or type(e).__name__
            print(f'Test {cls.name} failed: {error}')
        else:
            duration = round(time.time() - t0, 3)
            print(f'Test {cls.name} finished in {duration}s')
        finally:
            driver.quit()

    @abc.abstractclassmethod
    def test(cls, driver: webdriver.Chrome):
        ...
