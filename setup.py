from setuptools import setup

setup(
    name='waffa',
    version='0.1',
    py_modules=['waffa'],
    install_requires=[
        'Click',
        'wolframalpha',
    ],
    entry_points='''
        [console_scripts]
        waffa=waffa.cli:cli
    ''',
)
