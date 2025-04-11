from setuptools import setup

APP = ['connect4.py']
OPTIONS = {'iconsfile': 'icon2.icns', 'package': ['pygame', 'numpy']}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_require={'py2app'},
)