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
import click
import os
import imp
from mantra.utils import get_mantra_root


@click.group()
def cli():
    pass


@cli.command()
def init():
    root_dir = get_mantra_root()
    mantra_dir = imp.find_module("mantra")[1]

    settings_file_template = os.path.join(mantra_dir, "settings.py.in")
    settings_file = "settings.py"
    original_directory = os.getcwd()

    with open(settings_file_template, "r") as f:
        settings = f.read()

    if root_dir is not None:
        os.chdir(root_dir)

    with open(settings_file, "w") as f:
        f.write(settings)

    os.chdir(original_directory)
    click.echo('initialization successful')


@cli.command()
def run():
    click.echo("running server")
