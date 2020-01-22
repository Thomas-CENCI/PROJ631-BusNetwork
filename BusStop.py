class BusStop:
    """
    This class represents a bus stop within a bus line
    """

    def __init__(self, bus_stop_name, next_stop = [], previous_stop = [], regular_dates_go = [], regular_dates_back = [], special_dates_go = [], special_dates_back = []):
        self.name = bus_stop_name
        self.previous_stop = previous_stop
        self.next_stop = next_stop
        self.regular_dates_go = regular_dates_go
        self.regular_dates_back = regular_dates_back
        self.special_dates_go = special_dates_go
        self.special_dates_back = special_dates_back

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

    def get_regular_dates_go(self):
        """
        Get the regular dates (first direction)
        :return type list: [date1, ...]
        """
        return self.regular_dates_go

    def get_regular_dates_back(self):
        """
        Get the regular dates (second direction)
        :return type list: [date1, ...]
        """
        return self.regular_dates_back

    def get_special_dates_go(self):
        """
        Get the holidays dates (first direction)
        :return type list: [date1, ...]
        """
        return self.special_dates_go

    def get_special_dates_back(self):
        """
        Get the holidays dates (second direction)
        :return type list: [date1, ...]
        """
        return self.special_dates_back

    def set_previous_stop(self, stop):
        """
        Update the stop's previous stop
        :param stop type BusStop:
        """
        self.previous_stop.append(stop)

    def set_next_stop(self, stop):
        """
        Update the stop's next stop
        :param stop type BusStop:
        """
        self.next_stop.append(stop)

    def set_regular_dates_go(self, dates):
        """
        Update the stop's regular dates (first direction)
        :param stop type BusStop:
        """
        self.regular_dates_go.append(dates)

    def set_regular_dates_back(self, dates):
        """
        Update the stop's regular dates (second direction)
        :param stop type BusStop:
        """
        self.regular_dates_back.append(dates)

    def set_special_dates_go(self, dates):
        """
        Update the stop's special dates (first direction)
        :param stop type BusStop:
        """
        self.special_dates_go.append(dates)

    def set_special_dates_back(self, dates):
        """
        Update the stop's special dates (second direction)
        :param stop type BusStop:
        """
        self.special_dates_back.append(dates)