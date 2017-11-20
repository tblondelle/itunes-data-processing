# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:14:36 2017

@author: Thomas

Etape 1 : exporter la bibliothèque iTunes sous forme d'XML.
Etape 2 : lancer preprocess.py
Etape 3 : lancer process.py

"""

## Remplace un XML mal fait par Apple par des balises claires
import re

# [^<]* <==> data
replacements = """<key>Track ID</key><integer>([^<]*)</integer>
<track-id>\\1</track-id>

<key>Name</key><string>([^<]*)</string>
<name>\\1</name>

<key>Artist</key><string>([^<]*)</string>
<artist>\\1</artist>

<key>Album Artist</key><string>([^<]*)</string>
<album-artist>\\1</album-artist>

<key>Composer</key><string>([^<]*)</string>
<composer>\\1</composer>

<key>Album</key><string>([^<]*)</string>
<album>\\1</album>

<key>Genre</key><string>([^<]*)</string>
<genre>\\1</genre>

<key>Kind</key><string>([^<]*)</string>
<kind>\\1</kind>

<key>Size</key><integer>([^<]*)</integer>
<size>\\1</size>

<key>Total Time</key><integer>([^<]*)</integer>
<total-time>\\1</total-time>

<key>Track Number</key><integer>([^<]*)</integer>
<track-number>\\1</track-number>

<key>Year</key><integer>([^<]*)</integer>
<year>\\1</year>

<key>Date Modified</key><date>([^<]*)</date>
<date-modified>\\1</date-modified>

<key>Date Added</key><date>([^<]*)</date>
<date-added>\\1</date-added>

<key>Bit Rate</key><integer>([^<]*)</integer>
<bit-rate>\\1</bit-rate>

<key>Sample Rate</key><integer>([^<]*)</integer>
<sample-rate>\\1</sample-rate>

<key>Play Count</key><integer>([^<]*)</integer>
<play-count>\\1</play-count>

<key>Play Date</key><integer>([^<]*)</integer>
<play-date>\\1</play-date>

<key>Play Date UTC</key><date>([^<]*)</date>
<play-date-utc>\\1</play-date-utc>

<key>Skip Count</key><integer>([^<]*)</integer>
<skip-count>\\1</skip-count>

<key>Skip Date</key><date>([^<]*)</date>
<skip-date>\\1</skip-date>

<key>Artwork Count</key><integer>([^<]*)</integer>
<artwork-count>\\1</artwork-count>

<key>Persistent ID</key><string>([^<]*)</string>
<persistent-id>\\1</persistent-id>

<key>Track Type</key><string>([^<]*)</string>
<track-type>\\1</track-type>

<key>Location</key><string>([^<]*)</string>
<location>\\1</location>

<key>File Folder Count</key><integer>([^<]*)</integer>
<file-folder-count>\\1</file-folder-count>

<key>Library Folder Count</key><integer>([^<]*)</integer>
<library-folder-count>\\1</library-folder-count>"""

replacements_list = replacements.split('\n\n')

FILE_TO_READ = 'Library12-11-17.xml'
FILE_TO_WRITE = 'new 2.xml'


with open(FILE_TO_READ, 'r', encoding='utf-8') as file_to_be_read:
    file = file_to_be_read.read()
    
for replacement in replacements_list:
    pattern_search, pattern_replace = replacement.split('\n')
    print('Replacing... ', pattern_replace)
    # Overwrite file for every replacement.
    file = re.sub(pattern_search, pattern_replace, file)

with open(FILE_TO_WRITE, 'w', encoding='utf-8') as f:
    f.write(file)
