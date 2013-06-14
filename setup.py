#
# Copyright 2011 John Keyes
#
# http://jkeyes.mit-license.org/
#

from setuptools import find_packages
from setuptools import setup

install_requires = ['watchdog', 'pathfinder']

setup(
    name="lesswatch",
    version='0.2',
    description="Automatic compilation of modified LESS files.",
    long_description=open('README.md').read(),
    author="John Keyes",
    author_email="john@keyes.ie",
    license="MIT License",
    url="http://github.com/jkeyes/lesswatch",
    keywords='LESS python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'lesswatch = lesswatch.lesswatch:main',
        ]
    }
)