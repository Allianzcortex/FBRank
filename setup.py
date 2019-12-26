from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
        name='FBRank',
        version='1.8.7',

        description="A commandline tool helps you visualize league rank and other imformation",
        url='https://github.com/Allianzcortex/FBRank',
        author='Allianzcortex',
        author_email='iamwanghz@gmail.com',

        license='MIT',

        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
        ],

        keywords='Soccerball Manager SetupTools',
        packages=find_packages(),
        install_requires=['requests', 'beautifulsoup4', 'prettytable', 'translate'],

        entry_points={
            'console_scripts': [
                'FB=FBRank.main:execute',
            ],
        },
)
