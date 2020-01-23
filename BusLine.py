from BusStop import *

class BusLine(BusStop):
    """
    This class represents a bus line within the bus network
    """

    def __init__(self, number, bus_stops = [], corresponding_stops = []):
        self.number = number
        self.bus_stops = bus_stops
        self.corresponding_stops = corresponding_stops

    def get_bus_stops(self):
        """
        Get all the bus stops within this line
        :return type list: List of all the bus stops
        """
        return self.bus_stops

    def get_line_number(self):
        """
        Get the line number
        :return type int: line_number
        """
        return self.number

    def get_corresponding_stops(self):
        """
        Get the corresponding stops
        :return type list: [stop1, ...]
        """
        return self.corresponding_stops

    def set_bus_stops(self, data):
        """
        Fills the self.bus_stops list with all the bus stops from the data provided
        :param data type list: [stop1, ...]
        """
        self.bus_stops = data

    def set_corresponding_stops(self, data):
        """
        Fills the self.corresponding_stops list with all the corresponding stops of the two lines
        :param data type list: [stop1, ...]
        """
        self.corresponding_stops = data