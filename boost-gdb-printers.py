# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
# Auto-load of all the printers.
#
# This file is part of boost-gdb-printers.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import gdb

import os

pythondir = os.path.split(os.path.realpath(__file__))[0]

if pythondir not in sys.path:
    sys.path.insert(0, pythondir)

from boost.v1_58 import register_pretty_printers
# no object file, register globally
register_pretty_printers(gdb)

# vim:set filetype=python shiftwidth=4 softtabstop=4 expandtab:
