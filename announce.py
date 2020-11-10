#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import configparser

#Read config conf.ini using configparser
config = configparser.ConfigParser()
config.read('conf.ini')

#Generate start of message using repeater callsign
message = u'Vous êtes bien sur '+config['DEFAULT']['callsign']+'. Ceci est une annonce locale. '

#Add bulletin message that can be generated outside (here we use a weather bulletin generated before)
with open('announce.txt', 'r') as file:
    message = message + file.read().replace('\n', '') + ". 73 a tousse."

#See http://www.voicerss.org/api/ for values below
payload =  {
    'key':config['DEFAULT']['api_key'],
    'r':-1,
    'hl':'fr-FR',
    'c':'MP3',
    'f':'16khz_16bit_mono',
    'src':message,
    'v':'Zola'
    }
r = requests.post('http://api.voicerss.org/', params =payload)

#Writeout mp3 file with message generated
with open('announce.mp3', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)