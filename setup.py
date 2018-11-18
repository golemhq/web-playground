from setuptools import setup, find_packages

import web_playground


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='web-playground',
    version=web_playground.__version__,
    author='Luciano Renzi',
    author_email='luciano@lucianorenzi.com',
    description='Demo web application for testing purposes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/golemhq/web-playground',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'web-playground = web_playground.run:main'
        ]
    },
    keywords='test automation selenium webdriver web web-playground',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Testing'
    ]
)
