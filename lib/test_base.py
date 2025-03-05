import abc
from selenium import webdriver


class TestBase(abc.ABC):
    url: str
    name: str
    description: str

    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, 'url'):
            raise NotImplementedError('`url` not implemented')
        if not isinstance(cls.url, str):
            raise NotImplementedError('`url` must be type str')
        if not hasattr(cls, 'name'):
            raise NotImplementedError('`name` not implemented')
        if not isinstance(cls.name, str):
            raise NotImplementedError('`name` must be type str')
        if not hasattr(cls, '`description`'):
            raise TypeError('`description` not implemented')
        if not isinstance(cls.description, str):
            raise TypeError('`description` must be type str')
        return super().__init_subclass__(**kwargs)

    @abc.abstractclassmethod
    async def run(cls, driver: webdriver.Chrome):
        ...
