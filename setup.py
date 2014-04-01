#!/usr/bin/env python
# Copyright (c) 2014 Nick Douma < n.douma [at] nekoconeko . nl >
#
# This file is part of chaos, a.k.a. python-chaos .
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see 
# <http://www.gnu.org/licenses/>.

from os.path import join, dirname
from distutils.core import setup

NAME="chaos"
VERSION="0.1"
DESCRIPTION="Assorted libraries and subroutines"

f = open(join(dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()

setup(
	name=NAME,
	version=VERSION,
	description=DESCRIPTION,
	long_description=long_description,
	license="LGPL3",
	author="Nick Douma",
	author_email="n.douma@nekoconeko.nl",
	url="https://github.com/LordGaav/python-chaos",
	packages=["chaos", "chaos.threading", "chaos.multiprocessing"]
)
