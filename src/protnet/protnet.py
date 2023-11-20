# ----------------------------------------------------------------------------
# @File	:	genenet.py
# @Time	:	18:40:56 10/11/2023
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
protnet:
    Core module to protnet's library. Classes concerning the network building
    from expression data are contained within this module.
"""

# Third-party libraries
from networkx import Graph
from pandas import DataFrame
from numpy import array

class ProtNetwork(Graph):

    # Central implementation of a Gene Network. Built-in methods to calculate
    # a variety of useful structures to study the network.

    def __init__(self, dataframe):
        if not isinstance(dataframe, DataFrame):
            TypeError("The inputed object is not a recognised data type. " \
                      "You should try using lists, a pandas DataFrame or a " \
                      "numpy array.")

    def __init__(self, dataset, genes, obs):
        if not isinstance(dataset, array) or \
            not isinstance(genes, array) or \
            not isinstance(obs, array):
            TypeError("The inputed object is not a recognised data type. " \
                      "You should try using lists, a pandas DataFrame or a " \
                      "numpy array.")