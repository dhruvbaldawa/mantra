"""
    mantra
    Copyright (C) 2016  Dhruv Baldawa<dhruvbaldawa@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup

setup(
    name='mantra',
    version='0.1',
    description='Facebook Messenger Bot Framework',
    author='Dhruv Baldawa',
    author_email='dhruvbaldawa@gmail.com',
    packages=['mantra'],
    entry_points={
        'console_scripts': [
            'mantra = mantra.cli:cli',
        ],
    },
)
