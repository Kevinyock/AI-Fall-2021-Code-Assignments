''' Assignment # 1
A* Pathing
Author: Kevin Do
File Creation Date: 8/26/2021
Last Modified Date: 9/3/2021
Due Date: 9/3/2021 @ 11:59 PM
'''

''' List of bugs
Best out in DisplayInfo() print out a list of all of the cities the algorithm visited
'''

import sys
import re
import math
import copy
####
# Open the files first
####
# Store the actual distance between connected cities
file_map = open("map.txt")
# Store the straight-line distance between connected cities
file_distance = open("distances.txt")

'''
f(n) = g(n) + h(n) with n being city where are at
G(n) - Distance between the current city and the other cities
F(n) - Total Cost of the distance so far
H(n) - Straight Line Distance between current city and the destination city
'''

# List of all the straight-line distances from the cities to Bucharest
straightDistList = {} #cityHValue

# Store The city and the straightline distance toward the destination and set the other values to Infinity

for line in file_distance:
    straightDist = line.split("-")
    straightDistList[straightDist[0]] = int(straightDist[1].strip())

CitiesNNeighborList = {}
NeighboringCityList = {}

lines = file_map.readlines()
for line in lines:
    CityNNeighbors = line.split("-") # City NeighboringCities
    NeighboringCity = CityNNeighbors[1]
    NeighboringCity = NeighboringCity.rstrip()
    NeighboringCity = NeighboringCity.split(",")

    for NeighborCity in NeighboringCity:
        NeighborCity = re.sub('[^0-9a-zA-Z]',' ',NeighborCity)
        NeighborCity = NeighborCity.split(" ")
        NeighborCityName = NeighborCity[0]
        NeighborCityDistance = NeighborCity[1]
        NeighboringCityList[NeighborCityName] = int(NeighborCityDistance)

    CitiesNNeighborList[CityNNeighbors[0]] = copy.deepcopy(NeighboringCityList)
    NeighboringCityList.clear()

initialCity = sys.argv[1]
# initialCity = "Mehadia" # For Debug Purpose
destinationCity = "Bucharest"
routeSteps = []

def A_Star(startingCity, destinationCity, straightDistList, CitiesNNeighborList):
    
    totalDistance = 0
    # We start at the city we are at
    CurrentRoute = [startingCity]

    # give me the current route of the city I had to travel to get to where im at
    previousCityVisited = []
    
    cityFValue = {}
    cityGValue = {}

    for key in straightDistList.keys():
        cityFValue[key] = math.inf
        cityGValue[key] = math.inf
    
    cityFValue[startingCity] = straightDistList.get(startingCity)
    cityGValue[startingCity] = 0

    while len(CurrentRoute) > 0:
        
        minimumF = math.inf
        CurrentCity = ""

        for city in CurrentRoute:
            if minimumF > cityFValue[city]:
                minimumF = cityFValue[city]
                CurrentCity = city
        
        # Are we there yet?
        if CurrentCity == destinationCity:
            previousCityVisited.append(CurrentCity)
            return previousCityVisited, totalDistance

        CurrentRoute.remove(CurrentCity)
        previousCityVisited.append(CurrentCity)
        
        # Check each of the Neighboring City to find the best route to the destinated city
        for NeighboringCity in CitiesNNeighborList.get(CurrentCity):

            tentativeGScore = cityGValue[CurrentCity] + CitiesNNeighborList.get(CurrentCity)[NeighboringCity]
            if tentativeGScore < cityGValue[NeighboringCity]:
                cityGValue[NeighboringCity] = tentativeGScore
                cityFValue[NeighboringCity] = cityGValue[NeighboringCity] + straightDistList.get(NeighboringCity)
                totalDistance = tentativeGScore

                if NeighboringCity not in CurrentRoute:
                    CurrentRoute.append(NeighboringCity)
    print("We were unable to get to the city")
    return 0

def displayInfo(initialCity,destinationCity,routeSteps,totalDistance):
    print("From City: " + initialCity)
    print("To City: " + destinationCity)
    print("Best Route: " + " - ".join(routeSteps))
    print("Total distance: " , totalDistance)


routeSteps,totalDistance = A_Star(initialCity,destinationCity,straightDistList,CitiesNNeighborList)
displayInfo(initialCity,destinationCity,routeSteps,totalDistance)