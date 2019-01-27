from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CSV2SQLite',
    packages=find_packages(),
    version='0.1',
    description='CLI application that reads and saves a CSV file to a SQLite database.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Miguel Algorri',
    author_email='algorrim@gmail.com',
    install_requires=[
        'pandas>=0.24.0'
    ],
    extras_require={
        'test': [],
    },
    entry_points={
        'console_scripts': [
            'csv2sqlite=csv2sqlite.cmd'
        ]
    }
)
