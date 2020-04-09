# Exercise 1: Change geoxml.py to print out the two-character country code from the retrieved data. 
# Add error checking so your program does not traceback if the country code is not there. Once you have it working, 
# search for "Atlantic Ocean" and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location or type "done" to finish program: ')
    if len(address) < 1: break

    if address == "done":
        print("Exiting...")
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('===========')
    
    lst = tree.findall('result/address_component/short_name')
    print('lat', lat, 'lng', lng)
    print(location)
    
    try:
        country = lst[3].text
        print(country)
    except:
        print("Country code not found for {}".format(address))
        continue

