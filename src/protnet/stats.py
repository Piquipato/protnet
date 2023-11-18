# ----------------------------------------------------------------------------
# @File	:	stats.py
# @Time	:	19:04:32 17/11/2023
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

"""
stats:
    Statistics module with utilities for the rest of the library.
"""

# Third-party libraries
from numpy import array, zeros, ones

# Built-in libraries
from math import sqrt, log, pow

def mutual_information(x: array, y: array) -> float:
    """
    mutual_information:
        Calculates the mutual information between two continuous
        variables, by the gRapHD R library method.
    """
    n = len(x)
    (v1, v2, c12, m1, m2, \
    idn, idx, idy, nuo) = tuple(zeros((1, 9)))
    for i in range(n):
        nuo += 1
        (v1, v2) += (x[i] ** 2, y[i] ** 2)
        (m1, m2) += (x[i], y[i])
        c12 += x[i] * y[i]
        (idn, idx, idy) += (x[i] == y[i], \
                            x[0] == y[i], \
                            y[0] == x[i])
    v1 = sqrt((v1 - m1 * m1 / nuo) / (nuo))
    v2 = sqrt((v2 - m2 * m2 / nuo) / (nuo))
    c12 = (c12 - m1 * m2 / nuo) / (nuo)
    c12 /= (v1 * v2)
    (m1, m2) /= nuo * tuple(ones((1, 2)))
    if not (
        (idn == nuo) or
        (idx == nuo) or
        (idy == nuo)
    ):
        return - n * log(1 - pow(c12, 2)) - log(n)