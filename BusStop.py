class BusStop:
    """
    This class represents a bus stop within a bus line
    """

    def __init__(self, bus_stop_name, next_stop = [], previous_stop = [], regular_dates = [], we_h_dates = []):
        self.name = bus_stop_name
        self.previous_stop = previous_stop
        self.next_stop = next_stop
        self.regular_dates = regular_dates
        self.we_h_dates = we_h_dates

    def get_bus_stop_name(self):
        """
        Get the bus stop's name
        :return type str: '*bus stop's name*'
        """
        return self.bus_stop_name

    def get_previous_stop(self):
        """
        Get the previous stop(s)
        :return type list: [previous_stop1(, previous_stop2, ...)]
        """
        return self.previous_stop

    def get_next_stop(self):
        """
        Get the next stop(s)
        :return type list: [next_stop1(, next_stop2, ...)]
        """
        return self.next_stop

    def get_regular_dates(self):
        """
        Get the regular dates
        :return type list: [date1, ...]
        """
        return self.regular_dates

    def get_we_h_dates(self):
        """
        Get the holidays dates
        :return type list: [date1, ...]
        """
        return self.we_h_dates