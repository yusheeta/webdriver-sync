from setuptools import setup, find_packages

setup(
    name="webdriver-sync",
    version="0.1.0",
    description="webdriver-sync will help manage the webdriver for the browsers",
    author="sidhant singh",
    author_email="ssid23121@gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'webdriversync = webdriversync.__main__:main',
        ],
    },
)
