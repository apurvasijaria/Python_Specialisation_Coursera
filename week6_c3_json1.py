import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=raw_input('Enter Location:')
    if len(address)<1:break

    url=serviceurl+urllib.urlencode({'sensor':'false','address':address})
    print 'Retreiving',url
    uh=urllib.urlopen(url)
    data=uh.read()
    print 'Retreiving',len(data),'charaters'

    try: js=json.loads(str(data))
    except: js=None
    if 'status' not in js or js['status']!='OK':
        print '====Fialure to retrieve===='
        print data
        continue
    print json.dumps(js,indent=4)

    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location=js['results'][0]['formatted_address']
    print location