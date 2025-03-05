"""setup.py
locan installation: pip install -e .

python setup.py sdist
twine upload --repository pypitest dist/libseleniumagent-x.x.x.tar.gz
twine upload --repository pypi dist/libseleniumagent-x.x.x.tar.gz
"""
from setuptools import setup, find_packages
from libseleniumagent.version import __version__ as version

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except IOError:
    long_description = ''

install_requires = [
    'selenium',
]

setup(
    name='libseleniumagent',
    packages=find_packages(),
    version=version,
    description='Library for building Infrasonar selenium agents',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cesbit',
    author_email='info@cesbit.com',
    url='https://github.com/infrasonar/selenium-agent',
    download_url=(
        'https://github.com/infrasonar/'
        'selenium-agent/tarball/v{}'.format(version)),
    keywords=['monitoring', 'infrasonar', 'agent', 'selenium'],
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ],
)
