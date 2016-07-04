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
import os


def get_mantra_root():
    root = os.getcwd()
    settings_file = "settings.py"

    while True:
        if os.path.exists(os.path.join(root, settings_file)):
            return root
        else:
            parent_dir = os.path.split(root)[0]
            if parent_dir == root:
                break
            root = parent_dir
    return None