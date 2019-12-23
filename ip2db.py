#!/usr/bin/python

from requests import get
import logging

###############################################################################################################
######   Popis: Skript zistuje vonkajsiu IP adresu  a uklada ju do DB
######   Autor: Tomas Klein,  R-SYS 2019
######   Datum: 20.12.2019
###############################################################################################################

################################ PYTHON BASIC SETUP ###########################################################
#Nastavenie loggera - ukladanie do súboru
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                    filemode='a',
                    filename="ip2db.log"
                    )

#Nastavenie Logger pre konzolu
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
###############################################################################################################

try:
    ip = get('https://api.ipify.org').text
    logging.info('My public IP address is: ' + ip)
except Exception as e:
    logging.exception("Get request for IP - ERROR")
