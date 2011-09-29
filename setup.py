# lesswatch
# Copyright (C) 2011 John Keyes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import find_packages
from setuptools import setup

install_requires = ['watchdog',
                    'pathfinder']

setup(name="lesswatch",
      version='0.1',
      description="Automatic compilation of modified LESS files.",
      long_description=open('README.md').read(),
      author="John Keyes",
      author_email="john@keyes.ie",
      license="GPL v3",
      url="http://github.com/jkeyes/lesswatch",
      keywords='LESS python',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Designers',
          'License :: OSI Approved :: GNU GPL v3',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX :: BSD',
          'Operating System :: Microsoft :: Windows :: Windows NT/2000',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Filesystems',
          'Topic :: Utilities',
          ],
      package_dir={'': 'src'},
      packages=find_packages("src"),
      include_package_data=True,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'lesswatch = lesswatch.lesswatch:main',
          ]
      }
      )