# ----------------------------------------------------------------------------
# @File	:	genenet-test.py
# @Time	:	19:24:58 10/11/2023
# @Author	:	Pedro Lalanda Delgado
# @Version	:	1.0.0
# @Contact	:	piquipato@gmail.com
# @License	:	(C)Copyright 2023
# ----------------------------------------------------------------------------
# @License	:	Copyright (C) 2023	Pedro Lalanda Delgado
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# ----------------------------------------------------------------------------
# This software is a creation of PepitoDeCrema.
# ----------------------------------------------------------------------------

from protnet.genenet import GeneNetwork

from sys import exit

def initializeGeneNetwork():
    try:
        net = GeneNetwork()
        return 0
    except TypeError:
        raise AssertionError("GeneNetwork object not initializing correctly!")

if __name__ == "__main__":
    exit(initializeGeneNetwork())