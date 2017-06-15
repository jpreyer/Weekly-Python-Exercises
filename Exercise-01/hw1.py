import re

pattern = "r'([\w\s]*),([\w\s]*)'"

looping = True
places_list=[]
#places = {}
while looping:
    places = {}
    destination = raw_input("Tell me where you went: ")
    if destination == "":
        break
    else:
        m = re.search(r'([\w\s]*),([\w\s]*)',destination)
        city = m.group(1)
        country = m.group(2)
        m1 = re.search(r'\s*([\w\s]*)\s*', city)
        m2 = re.search(r'\s*([\w\s]*)\s*', country)
        city = m1.group(1)
        country = m2.group(1)
        places[country] = city
        places_list.append(places)
        #print "CITY:"+city+"  COUNTRY:"+country
print places_list
