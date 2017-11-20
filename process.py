# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:20:52 2017

@author: Thomas

Etape 1 : exporter la bibliothèque iTunes sous forme d'XML.
Etape 2 : lancer preprocess.py
Etape 3 : lancer process.py

"""



import csv
import xml.etree.ElementTree as ET

FILE_TO_READ = 'new 2.xml'
FILE_TO_WRITE = 'liste.csv'
DEFAULT_VALUE = '__'

def get_tracks(file):
    tree = ET.parse(file)
    root = tree.getroot()
    tracks = root.findall("./dict/dict/dict")
    return tracks

tags = ['track-id', 'name', 'artist',
        'album-artist', 'album', 'genre',
 'kind','size', 'total-time', 'track-number',
 'year', 'date-modified',
 'date-added', 'play-count',
 'play-date', 'play-date-utc', 'track-type', 'composer']

with open(FILE_TO_WRITE, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=tags, delimiter='\t')
    writer.writeheader()
    for track in get_tracks(FILE_TO_READ):
        row = {}
        for tag in tags:
            row[tag] = DEFAULT_VALUE
            
        for data in track:
            if data.tag in tags:
                row[data.tag] = data.text
    
        writer.writerow(row)
