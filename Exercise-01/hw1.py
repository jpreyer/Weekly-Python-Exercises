import re

pattern = "r'([\w\s]*),([\w\s]*)'"

looping = True
places = {}
while looping:
    destination = raw_input("Tell me where you went: ")
    m = re.search(r'([\w\s]*),([\w\s]*)',destination)
    city = m.group(1)
    country = m.group(2)
    places[city] = country
    print "CITY:"+city+"  COUNTRY:"+country
