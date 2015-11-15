import sys
import math

def stringToFloat(string):
    """ Transform a string formatted like this "xxx,xxx" into a float number """
    number = string.split(',')
    intPart = int(number[0])
    floatingPart = 0.0
    if(len(number[1])):
        floatingPart = int(number[1])/math.pow(10, len(number[1]))
    return floatingPart + intPart

# current longitude
lon = stringToFloat(raw_input())
# current latitude
lat = stringToFloat(raw_input())
# number of defibrillators
n = int(raw_input())
# closest place infos
closestPlaceName = ""
closestPlaceDistance = 0

for i in xrange(n):
    defib = raw_input()
    defibInfos = defib.split(';')
    defibName = defibInfos[1]
    defibLong = stringToFloat(defibInfos[4])
    defibLat = stringToFloat(defibInfos[5])
    # distance calculation
    defibXDist = (defibLong - lon) * math.cos((defibLat + lat)/2)
    defibYDist = (defibLat - lat)
    distance = math.sqrt(defibXDist*defibXDist + defibYDist*defibYDist) * 6371

    if(i == 0 or distance < closestPlaceDistance):
        closestPlaceDistance = distance
        closestPlaceName = defibName

print closestPlaceName
