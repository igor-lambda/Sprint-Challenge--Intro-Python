import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  
  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
# cities = []

def cityreader():

  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  cities = []
  with open('cities.csv') as csvfile:
    citiesreader = csv.reader(csvfile)
    next(citiesreader) # skip first line
    for city in citiesreader:
      cities.append(City(city[0], float(city[3]), float(city[4])))  
  return cities

cities = cityreader()

for city in cities:
  print('zl', city.name, city.lat, city.lon)



# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

user = input("Enter two pairs of lat and long values, and we will tell you which cities fall within the square.")
userList = user.split(" ")
userFloats = [float(x) for x in userList]

# This tests whether each city's lat and lon and both larger than the user's smallest lat and lon and smaller
# than the user's largest lat and lon
def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  smallestLat = None
  smallestLon = None
  largestLat = None
  largestLon = None

  if lat1 < lat2:
    smallestLat = lat1
    largestLat = lat2
  else:
    smallestLat = lat2
    largestLat = lat1

  if lon1 < lon2:
    smallestLon = lon1
    largestLon = lon2
  else:
    smallestLon = lon2
    largestLon = lon1

  print("lll", smallestLat, smallestLon, largestLat, largestLon)
  
  for c in cities:
    if c.lon > smallestLon and c.lon < largestLon and c.lat < largestLat and c.lat > smallestLat:
      within.append(c) 
  # TODO Ensure that the lat and lon values are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

within = cityreader_stretch(userFloats[0], userFloats[1], userFloats[2], userFloats[3], cities)

for c in within:
  print(f"{c.name}: ({c.lat}, {c.lon})")