from setuptools import setup
from setuptools import find_packages
from settings import __version__

try:
    license = open('LICENSE').read()
except:
    license = None

try:
    readme = open('README.md').read()
except:
    readme = None

setup(
    name='kiki',
    version=".".join(str(x) for x in __version__),
    package_dir={'kiki': 'src'},
    packages=['kiki', 'kiki.commons', 'kiki.sample', 'kiki.tests'],
    description='ZZiZiLY Commons Project',
    long_description=readme,
    author='crom',
    author_email='crom@zzizily.com',
    url='https://github.com/deuxksy/kiki',
    install_requires=[
        'aiohttp',
        'appdirs',
        'async-timeout',
        'chardet',
        'colorama',
        'decorator',
        'ipython',
        'ipython-genutils',
        'multidict',
        'packaging',
        'pickleshare',
        'pip',
        'prompt-toolkit',
        'psycopg2',
        'Pygments',
        'PyMySQL',
        'pyparsing',
        'redis',
        'requests',
        'setuptools',
        'simplegeneric',
        'six',
        'slacker',
        'telepot',
        'traitlets',
        'urllib3',
        'wcwidth',
        'wheel',
        'win-unicode-console',
        'yarl',
    ],
    license=license,
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Korean',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='zzizily commons api'
)
