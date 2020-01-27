from BusStop import *
from BusLine import *

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

    # Tidying up the data for the bus line
    split_content = content.split("\n\n")
    data = {}
    data['bus_stops_regular_order'] = [name.upper() for name in split_content[0].split(' ')]
                                    # [bus_stop1, seperator, bus_stop2, ...]
    regular_path = split_content[0].replace('+', 'N').split(' N ')
    data['regular_path'] = [name.upper() for name in regular_path]
                         # [bus_stop1, bus_stop2, ...]
    data['regular_date_go'] = dates2dic(split_content[1]) # A AMELIORER AVEC LE MODULE TIME
                            # [time1, time2, ...]
    data['regular_date_back'] = dates2dic(split_content[2]) # A AMELIORER AVEC LE MODULE TIME
                              # [time1, time2, ...]
    data['bus_stops_we_holidays_order'] = [name.upper() for name in split_content[3].split(' ')]
                                        # [bus_stop1, seperator, bus_stop2, ...]
    we_holidays_path = split_content[3].replace('+', 'N').split(' N ')
    data['we_holidays_path'] = [name.upper() for name in we_holidays_path]
                             # [bus_stop1, bus_stop2, ...]
    data['we_holidays_date_go'] = dates2dic(split_content[4]) # A AMELIORER AVEC LE MODULE TIME
                                # [time1, time2, ...]
    data['we_holidays_date_back'] = dates2dic(split_content[5]) # A AMELIORER AVEC LE MODULE TIME
                                  # [time1, time2, ...]
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


def assign_next_stop(data, bus_stops):
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


def assign_previous_stop(data, bus_stops):
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


def create_bus_line(data, line_number):
    """
    Creates the bus stops and the bus line that corresponds to those bus stops
    :param data type dict: {data_set1_name : data_set1, ...}
    :param line_number type int:
    """
    bus_stops = list()
    # Setting up the bus stops for the bus line
    for _ in range(len(data['regular_path'])):
        # Creating all bus stops
        locals()['line' + str(line_number) + '_stop' + str(_)] = BusStop(data['regular_path'][_])

        # Creating a list of all the bus_stops
        bus_stops.append(locals()['line' + str(line_number) + '_stop' + str(_)])

        # Setting the regular dates (go)
        locals()['line' + str(line_number) + '_stop' + str(_)].set_regular_dates_go(data['regular_date_go'][locals()['line' + str(line_number) + '_stop' + str(_)].get_bus_stop_name()])

        # Setting the regular dates (back)
        locals()['line' + str(line_number) + '_stop' + str(_)].set_regular_dates_back(data['regular_date_back'][locals()['line' + str(line_number) + '_stop' + str(_)].get_bus_stop_name()])

        # Setting the special dates (go)
        locals()['line' + str(line_number) + '_stop' + str(_)].set_special_dates_go(data['we_holidays_date_go'][locals()['line' + str(line_number) + '_stop' + str(_)].get_bus_stop_name()])

        # Setting the special dates (back)
        locals()['line' + str(line_number) + '_stop' + str(_)].set_special_dates_back(data['we_holidays_date_back'][locals()['line' + str(line_number) + '_stop' + str(_)].get_bus_stop_name()])

    # Assigning the buses' next stop(s)
    assign_next_stop(data, bus_stops)

    # Assigning the buses' previous stop(s)
    assign_previous_stop(data, bus_stops)

    # Creating the bus line with all the bus stops created beforehand as well as the line number
    Line = BusLine(line_number, bus_stops)

    return (Line)


Line1 = create_bus_line(data_managment(Line1_data), 1)
Line2 = create_bus_line(data_managment(Line2_data), 2)

# print('\n', data_managment(Line1_data)['regular_date_go'], '\n', [bus.get_regular_dates_go() for bus in Line1.bus_stops])
# print('\n', data_managment(Line2_data)['regular_date_go'], '\n', [bus.get_regular_dates_go() for bus in Line2.bus_stops])