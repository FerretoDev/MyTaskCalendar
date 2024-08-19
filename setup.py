from setuptools import setup, find_packages

setup(
    name="MyTaskCalendar",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flet",
    ],
    entry_points={
        "console_scripts": [
            "MyTaskCalendar=app.main:main",
        ],
    },
)
