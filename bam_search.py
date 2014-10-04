#!/usr/bin/python2.7
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  bam_search.py
#  
# Copyright 2014 Bruno Costa <brunovasquescosta@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  bam_search.py v1.0
#  Author: Bruno Costa
#  Last update: 03/10/2014

import argparse

parser = argparse.ArgumentParser(description="Remote tool")
parser.add_argument("-d",dest="dir", help="Optional, if provided searches the specified directory for tags.tsv files, if no file directory is provided uses current dir.")
parser.add_argument("-f",dest="bam_file",required=True, help="Bam file input.")
arg = parser.parse_args()

import string
import re
import glob
import pysam
path_tags=arg.dir

bam_file=arg.bam_file

samfile = pysam.Samfile( bam_file, "rb" )

for alignedread in samfile.fetch('12'):
     print alignedread

samfile.close()

