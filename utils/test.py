import urllib, urllib2, json

url = 'https://bmi.p.mashape.com/'

params = {
    'weight':{
        'value':'85.00',
        'unit':'kg'
    },
    'height':{
        'value':'170.00',
        'unit':'cm'
    },
    'sex':'m',
    'age':'24',
    'waist':'34.00',
    'hip':'40.00'
}

params = urllib.urlencode(params)

headers = {
    'X-Mashape-Key': 'fs2VyXxGiZmshQ26lUFKNpzZ7zpMp1bMFSNjsnyr6gRbjidRYi',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

request = urllib2.Request(url, data = params, headers = headers)
response = urllib2.urlopen(request)
