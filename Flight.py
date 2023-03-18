#This class is the parent class of the Airport Class where it uses Airport Class to produce results.
from Airport import Airport

class Flight:
    def __init__(self, flightNo, origin, destination): #Checking to make sure the inputted Origin and Destination are part of the Airport Class
        if isinstance(origin,Airport) == True and isinstance(destination,Airport) == True:
            self._flightNo = flightNo.upper()
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError ("The origin and destination must be Airport objects")

    def __eq__(self, other): #When inputted in an object, this method checks if the other object is equal to the existing self object.
        if isinstance(other,Flight):
            if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
                return True
            else:
                return False
        else:
            return False

    def getFlightNumber(self): #This method is used to get the Flight Number
        try:
            return self._flightNo
        except:
            return "The Flight Number must be a string"

    def getOrigin(self): #This method is used to get the Flight Origin
        try:
            return self._origin

        except:
            return "The origin must be a valid Airport object"

    def getDestination(self): #This method is used to get the Flight Destination
        try:
            return self._destination
        except:
            return "The destination must be a valid Airport object"

    def isDomesticFlight(self): #This method is used to check whether the flight object is a domestic or international flight
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    def setOrigin(self,newOrigin): #This method is used to set the Flight Origin
        try:
            self._origin = newOrigin
        except:
            return "The new origin must be an Airport object"

    def setDestination(self,newDestination): #This method is used to set the Flight Destination
        try:
            self._destination = newDestination
        except:
            return "The new destination must be an Airport object"

    def __repr__(self): #This repr method returns the output of the flight class when asked to print the object.
        if self.isDomesticFlight() == True:
            return "Flight: " + self._flightNo + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {Domestic}"
        elif self.isDomesticFlight() == False:
            return "Flight: " + self._flightNo + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {International}"

