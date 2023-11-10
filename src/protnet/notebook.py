# ----------------------------------------------------------------------------
# @File	:	notebook.py
# @Time	:	18:40:59 10/11/2023
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

from openpyxl import Workbook

import os, shutil

class Notebook(Workbook):
  
  # Just a reimplementation of openpyxl workbook which keeps track of
  # the path in which the workbook is located.

  def __init__(self, file_path=None, wb=None):
    self.file_path = file_path
    if isinstance(wb, Workbook):
      for key, value in vars(wb).items():
        if key != "file_path":
          setattr(self, key, value)
    else:
      super().__init__()

  # Saves Workbook to file path.
  def save(self, alt_path=None):
    # If a filepath is provided, it is saved there.
    if alt_path != None:
      super().save(alt_path)
    # Otherwise, it is saved to the current path.
    elif self.file_path != None:
      super().save(self.file_path)
    # If there is none, it saves it into the cwd.
    else:
      super().save(os.getcwd())

  # Makes a copy (optionally in another path).
  def copy(self, new_path=None, ext="cp_"):
    directory, filename = os.path.split(self.file_path)
    if new_path is not None:
      directory = new_path
    mycopy = Notebook(file_path=os.path.join(directory, ext + filename),
                            wb=self)
    mycopy.save()
    return mycopy

  # Moves workbook to another path.
  def move(self, new_path):
    shutil.move(self.file_path, new_path)
    self.file_path = os.path.join(new_path, os.path.split(self.file_path)[1])
