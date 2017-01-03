from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
        name='FBRank',
        version='1.3.0',

        description="one commandline tools help visualize league rank and other imformation",
        url='https://github.com/Allianzcortex/FBRank',
        author='Allianzcortex',
        author_email='iamwanghz@gmail.com',

        license='MIT',

        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
        ],

        keywords='Football Manager SetupTools',
        packages=find_packages(),
        install_requires=['requests', 'beautifulsoup4', 'prettytable'],

        entry_points={
            'console_scripts': [
                'FB=FBRank.main:execute',
            ],
        },
)
