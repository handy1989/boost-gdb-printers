# -*- tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4 -*-
# GDB pretty printers for Boost.Smart Ptr.
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

import gdb

import boost.util.printing as printing


class SmartPtrPrinter:
    """Prints smart pointers based on Boost.SmartPtr"""

    def __init__(self, typename, value):
        self.typename = typename
        self.value = value

    def to_string(self):
        if self.value['px']:
            countobj = self.value['pn']['pi_'].dereference()
            refcount = countobj['use_count_']
            weakcount = countobj['weak_count_']
            return "%s (use_count %d, weak_count %d) %s" % (self.typename, refcount, weakcount, self.value['px'].dereference())
        else:
            return "empty %s" % (self.typename,)

class ScopedPtrPrinter:
    """Prints smart pointers based on Boost.SmartPtr"""

    def __init__(self, typename, value):
        self.typename = typename
        self.value = value

    def to_string(self):
        if self.value['px']:
            return "%s %s" % (self.typename, self.value['px'].dereference())
        else:
            return "empty %s" % (self.typename,)


printer = None

def build_pretty_printers():
    global printer

    if printer != None:
        return

    printer = printing.Printer("boost.smart_ptr")

    printer.add('boost::shared_ptr', SmartPtrPrinter)
    # printer.add('boost::shared_array', SmartPtrPrinter)
    printer.add('boost::weak_ptr', SmartPtrPrinter)
    printer.add('boost::scoped_ptr', ScopedPtrPrinter)
    # printer.add('boost::scoped_array', SmartPtrPrinter)

def register_pretty_printers(obj):
    printing.register_pretty_printer(printer, obj)

build_pretty_printers()

# vim:set filetype=python shiftwidth=4 softtabstop=4 expandtab:
