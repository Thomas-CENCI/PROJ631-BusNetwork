from BusStop import *
from BusLine import *
from datetime import *

Line1_data = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/1_Poisy-ParcDesGlaisins.txt'
Line2_data = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/2_Piscine-Patinoire_Campus.txt'


def data_managment(data):
    """
    Organize the data into a more usable dictionnary
    :param data type str: "path to the .txt that contains the data"
    :return type dict: {data_set1_name : data_set1, ...}
    """
    try:
        with open(data, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        # 'File not found' error message.
        print("File not found")

    # Creating the path that contains the order of the bus_stops
    split_content = content.split("\n\n")
    data = {}
    data['bus_stops_regular_order'] = [name.upper() for name in split_content[0].split(' ')]

    regular_path = split_content[0].replace('+', 'N').split(' N ')
    data['regular_path'] = [name.upper() for name in regular_path]

    data['regular_date_go'] = from_str_to_datetime([dates2dic(split_content[1])[key] for key in dates2dic(split_content[1]).keys()])

    data['regular_date_back'] = from_str_to_datetime([dates2dic(split_content[2])[key] for key in dates2dic(split_content[2]).keys()])

    data['bus_stops_we_holidays_order'] = [name.upper() for name in split_content[3].split(' ')]

    we_holidays_path = split_content[3].replace('+', 'N').split(' N ')
    data['we_holidays_path'] = [name.upper() for name in we_holidays_path]

    data['we_holidays_date_go'] = from_str_to_datetime([dates2dic(split_content[4])[key] for key in dates2dic(split_content[4]).keys()])

    data['we_holidays_date_back'] = from_str_to_datetime([dates2dic(split_content[5])[key] for key in dates2dic(split_content[5]).keys()])

    return data

def from_str_to_datetime(data):
    """
    Converts a string into a time using the datetime module
    :param data type list: [['hours:minutes', '-', ...], ...]
    :return type list: [[time1, '-', ...], ...]
    """
    for list_index in range(len(data)):
        for time_index in range(len(data[list_index])):
            if data[list_index][time_index] != '-':
                data[list_index][time_index] = datetime.strptime(data[list_index][time_index], '%H:%M')
    return data


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0].upper()] = tmp[1:]
    return dic


def from_name_to_busStop(name, bus_stops):
    """
    Finds the object that corresponds to the name given
    :param name type str: 'name'
    :param bus_stops type list: [bus_stop1, ...]
    :return type BusStop: bus_stop
    """
    for bus_stop in bus_stops:
        if bus_stop.get_bus_stop_name() == name:
            return bus_stop


def assign_regular_next_stop(data, bus_stops):
    """
    Assign the next bus stop(s) to the next_stop attibute of all bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param bus_stops type list: [bus_stop1, ...]
    """
    forked_bus_stops = list()
    bus_stop_order = data['bus_stops_regular_order']
    for bus_stop in bus_stops[:-1]:
        for index in range(0, len(bus_stop_order), 2):
            if bus_stop.get_bus_stop_name() == bus_stop_order[index]:
                if bus_stop_order[index + 1] == '+':
                    forked_bus_stops += [bus_stop]
                elif bus_stop_order[index + 1] == 'N':
                    forked_bus_stops.append(bus_stop)
                    for receiver in forked_bus_stops:
                        receiver.set_next_stop(from_name_to_busStop(bus_stop_order[index + 2], bus_stops))
        if bus_stop_order[bus_stop_order.index(bus_stop.get_bus_stop_name()) + 1] == 'N':
            forked_bus_stops = []


def assign_special_next_stop(data, bus_stops):
    """
    Assign the next bus stop(s) to the next_stop attibute of all bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param bus_stops type list: [bus_stop1, ...]
    """
    forked_bus_stops = list()
    bus_stop_order = data['bus_stops_we_holidays_order']
    for bus_stop in bus_stops[:-1]:
        for index in range(0, len(bus_stop_order), 2):
            if bus_stop.get_bus_stop_name() == bus_stop_order[index]:
                if bus_stop_order[index + 1] == '+':
                    forked_bus_stops += [bus_stop]
                elif bus_stop_order[index + 1] == 'N':
                    forked_bus_stops.append(bus_stop)
                    for receiver in forked_bus_stops:
                        receiver.set_next_stop(from_name_to_busStop(bus_stop_order[index + 2], bus_stops))
        if bus_stop_order[bus_stop_order.index(bus_stop.get_bus_stop_name()) + 1] == 'N':
            forked_bus_stops = []


def assign_regular_previous_stop(data, bus_stops):
    """
    Assign the previous bus stop(s) to the previous_stop attibute of all bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param bus_stops type list: [bus_stop1, ...]
    """
    forked_bus_stops = list()
    bus_stop_order = data['bus_stops_regular_order']
    for bus_stop in bus_stops[:-1]:
        for index in range(0, len(bus_stop_order), 2):
            if bus_stop.get_bus_stop_name() == bus_stop_order[index]:
                if bus_stop_order[index + 1] == '+':
                    forked_bus_stops.append(bus_stop)
                elif bus_stop_order[index - 1] == 'N':
                    bus_stop.set_previous_stop(forked_bus_stops)
                    forked_bus_stops.append(from_name_to_busStop(bus_stop_order[index - 2], bus_stops))
        if bus_stop_order[bus_stop_order.index(bus_stop.get_bus_stop_name()) - 1] == 'N':
            forked_bus_stops = []
    bus_stops[-1].set_previous_stop([from_name_to_busStop(bus_stop_order[-3], bus_stops)])


def assign_special_previous_stop(data, bus_stops):
    """
    Assign the previous bus stop(s) to the previous_stop attibute of all bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param bus_stops type list: [bus_stop1, ...]
    """
    forked_bus_stops = list()
    bus_stop_order = data['bus_stops_we_holidays_order']
    for bus_stop in bus_stops[:-1]:
        for index in range(0, len(bus_stop_order), 2):
            if bus_stop.get_bus_stop_name() == bus_stop_order[index]:
                if bus_stop_order[index + 1] == '+':
                    forked_bus_stops.append(bus_stop)
                elif bus_stop_order[index - 1] == 'N':
                    bus_stop.set_previous_stop(forked_bus_stops)
                    forked_bus_stops.append(from_name_to_busStop(bus_stop_order[index - 2], bus_stops))
        if bus_stop_order[bus_stop_order.index(bus_stop.get_bus_stop_name()) - 1] == 'N':
            forked_bus_stops = []
    bus_stops[-1].set_previous_stop([from_name_to_busStop(bus_stop_order[-3], bus_stops)])


def find_corresponding_bus_stop(line1, line2):
    """
    Finds the corresponding stops of the lines given
    :param line1 type BusLine:
    :param line2 type BusLine:
    """
    line1_bus_stops = line1.get_bus_stops()
    line2_bus_stops = line2.get_bus_stops()
    corresponding_stops = list()
    for bus_stop in line1_bus_stops:
        if bus_stop.get_bus_stop_name() in [bus.get_bus_stop_name() for bus in line2_bus_stops]:
            corresponding_stops.append(bus_stop)
    line1.set_corresponding_stops(corresponding_stops)
    line2.set_corresponding_stops(corresponding_stops)


def create_bus_line(data, line_number, holidays = False):
    """
    Creates the bus stops and the bus line that corresponds to those bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param line_number type int:
    """
    bus_stops = list()
    if holidays:
        dataset = data['we_holidays_path']

        # Setting up the bus stops for the bus line
        for _ in range(len(dataset)):
            # Creating all bus stops
            locals()['line' + str(line_number) + '_stop' + str(_)] = BusStop(dataset[_])

            # Creating a list of all the bus_stops
            bus_stops.append(locals()['line' + str(line_number) + '_stop' + str(_)])

            # Setting the special dates (go)
            locals()['line' + str(line_number) + '_stop' + str(_)].set_special_dates_go(data['we_holidays_date_go'][_])

            # Setting the special dates (back)
            locals()['line' + str(line_number) + '_stop' + str(_)].set_special_dates_back(
                data['we_holidays_date_back'][_])

            # Assigning the buses' next stop(s)
            assign_special_next_stop(data, bus_stops)

            # Assigning the buses' previous stop(s)
            assign_special_previous_stop(data, bus_stops)


    else:
        dataset = data['regular_path']

        # Setting up the bus stops for the bus line
        for _ in range(len(dataset)):
            # Creating all bus stops
            locals()['line' + str(line_number) + '_stop' + str(_)] = BusStop(dataset[_])

            # Creating a list of all the bus_stops
            bus_stops.append(locals()['line' + str(line_number) + '_stop' + str(_)])

            # Setting the regular dates (go)
            locals()['line' + str(line_number) + '_stop' + str(_)].set_regular_dates_go(data['regular_date_go'][_])

            # Setting the regular dates (back)
            locals()['line' + str(line_number) + '_stop' + str(_)].set_regular_dates_back(data['regular_date_back'][_])

            # Assigning the buses' next stop(s)
            assign_regular_next_stop(data, bus_stops)

            # Assigning the buses' previous stop(s)
            assign_regular_previous_stop(data, bus_stops)

    # Creating the bus line with all the bus stops created beforehand as well as the line number
    Line = BusLine(line_number, bus_stops)

    return (Line)


# Creating the first line twice : one for the regular dates and the other one for the holidays
Line1_regular = create_bus_line(data_managment(Line1_data), 1)
Line1_special = create_bus_line(data_managment(Line1_data), 1, holidays = True)

# Creating the second line twice : one for the regular dates and the other one for the holidays
Line2_regular = create_bus_line(data_managment(Line2_data), 2)
Line2_special = create_bus_line(data_managment(Line2_data), 2, holidays = True)

# Setting up the corresponding stops between the two lines
find_corresponding_bus_stop(Line1_regular, Line2_regular)
find_corresponding_bus_stop(Line1_special, Line2_special)