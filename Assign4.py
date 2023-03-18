# This is the main file of the program that uses both the Flight.py and the Airport.py Classes

from Airport import Airport
from Flight import Flight
allAirports = []
allFlights = {}
parentAirplaneList = []
parentFlightList = []

def getAirportByCode(code): #This method lets us retrieve the Airport By Code. This function is used in LoadData as a major helper
    for j in allAirports:
        if j.getCode() == code:
            return j
    return -1

def loadData(airplaneFile,flightFile): #This method is used to load the data from the two given files and acts as the parent method for all other methods.
    #Loading the Data for the Airport File.
    try:

        #This block of code takes the Airplane File and throw multiple commands, formats it, stores it in a list to finally append the Airport Objects for them

        global allFlights #This global variable is essential to make the allFlights filled list work everywhere outside the function.
        with open(airplaneFile,'r') as f:
            lines = f.readlines()
            airplaneLinesTemp = []
            for line in lines:
                airplaneLinesTemp.append(line.split(","))

            airplaneList = []
            for i in airplaneLinesTemp:
                airplaneList.append(i[0].strip())
                airplaneList.append(i[2].strip())
                airplaneList.append(i[1].strip())
                parentAirplaneList.append(airplaneList)
                airplaneList = []


            for i in parentAirplaneList:
                g = Airport(i[0],i[1],i[2])
                allAirports.append(g)


    except:
        return False


#This block of code uses the Flight File, formats it and stores its objects in allFlights to be accessible by other methods.
    try:
        with open(flightFile,"r") as f:
            lines = f.readlines()
            flightList = []
            flightLinesTemp = []
            for line in lines:
                flightLinesTemp.append(line.split(","))

            for i in flightLinesTemp:
                flightList.append(i[0].strip())
                flightList.append(i[1].strip())
                flightList.append(i[2].strip())
                flightNo = i[0].strip()
                origin = getAirportByCode(i[1].strip())
                destination = getAirportByCode(i[2].strip())
                flightObject = Flight(flightNo,origin,destination)
                if i[1].strip() in allFlights.keys():
                    allFlights[i[1].strip()].append(flightObject)
                else:
                    allFlights[i[1].strip()] = [flightObject]

        return True

    except :
        return False

#This function finds all flights relevant with the given city.
def findAllCityFlights(city):
    flightCityObjects = []
    for i in allFlights.values(): #I perform this task by iterating through the allFlight Dict and checks if any object (Origin or Destination) has the city name
        for j in i:
            if j.getOrigin().getCity().upper() == city.upper() or j.getDestination().getCity().upper() == city.upper():
                flightCityObjects.append(j)

    return flightCityObjects

#This code finds all the flights of the specified country and return that in a list.
def findAllCountryFlights(country):
    flightCountryObjects = []
    try:
        for i in allFlights.values():
            for j in i:
                if j.getOrigin().getCountry().upper() == country.upper() or j.getDestination().getCountry().upper() == country.upper():
                    flightCountryObjects.append(j)

        return flightCountryObjects

    except:
        return "Invalid Country"

def findFlightBetween(origAirport,destAirport): #This function finds direct flights between the given two airports or single-hop flights (with one airport in between)
    try:
        global potentialHopAirport
        potentialHopAirport = []
        singleHopAirports = set()
        for i in allFlights.values():
            for j in i:
                if j.getOrigin().getCode().upper() == origAirport.getCode().upper() and j.getDestination().getCode().upper() == destAirport.getCode().upper():
                    return "Direct Flight: " + j.getOrigin().getCode().upper() + " to " + j.getDestination().getCode().upper()
        # print(1)
        for i in allFlights.values():
            for j in i:
                if j.getOrigin().getCode().upper() == origAirport.getCode().upper() and j.getDestination().getCode().upper() != destAirport.getCode().upper():
                            potentialHopAirport.append(j.getDestination().getCode().upper())

        for i in allFlights.values():
            for j in i:
                for l in potentialHopAirport:
                    if l == j.getOrigin().getCode().upper() and j.getDestination().getCode().upper() == destAirport.getCode().upper():
                        singleHopAirports.add(l)

        if singleHopAirports == set():
            return -1
        else:
            return singleHopAirports
    except:
        return "The inputted airport objects do not exist"

def findReturnFlight(firstFlight): #this method returns a flight object with the opposite variation of the given flight object. i.e. the origin of the given flight object will be the departure of the returned flight object and vice versa.
    try:
        givenOrgin = firstFlight.getOrigin().getCode().upper()
        givenDepart = firstFlight.getDestination().getCode().upper()
        for i in allFlights.values():
            for j in i:
                if j.getOrigin().getCode().upper() == givenDepart and j.getDestination().getCode().upper() == givenOrgin:
                    return(j)
        return -1
    except:
        "The inputted airport object do not exist"













