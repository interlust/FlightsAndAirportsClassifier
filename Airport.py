#This is the Airport Class that is used as a root for the Flight Class Origin and Destination .
#This code is largely written using the instructions of the assignment and doesn't contain much customization.

class Airport:
    def __init__(self,code,city,country):
        self._code = code.upper()
        self._city = city
        self._country = country

    def __repr__(self):
        return self._code + " (" + self._city + ", " + self._country + ")"

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self,city):
        self._city = city

    def setCountry(self, country):
        self._country = country


