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

    data['regular_date_go'] = convert_to_time_format([dates2dic(split_content[1])[key] for key in dates2dic(split_content[1]).keys()])

    data['regular_date_back'] = convert_to_time_format([dates2dic(split_content[2])[key] for key in dates2dic(split_content[2]).keys()])

    data['bus_stops_we_holidays_order'] = [name.upper() for name in split_content[3].split(' ')]

    we_holidays_path = split_content[3].replace('+', 'N').split(' N ')
    data['we_holidays_path'] = [name.upper() for name in we_holidays_path]

    data['we_holidays_date_go'] = convert_to_time_format([dates2dic(split_content[4])[key] for key in dates2dic(split_content[4]).keys()])

    data['we_holidays_date_back'] = convert_to_time_format([dates2dic(split_content[5])[key] for key in dates2dic(split_content[5]).keys()])

    return data

def convert_to_time_format(data):
    """
    Converts a string into a time using the datetime module
    :param data type list: [['hours:minutes', '-', ...], ...]
    :return type list: [[time1, '-', ...], ...]
    """
    for list_index in range(len(data)):
        for time_index in range(len(data[list_index])):
            if data[list_index][time_index] != '-':
                data[list_index][time_index] = timedelta(hours = int(data[list_index][time_index].split(':')[0]), minutes = int(data[list_index][time_index].split(':')[1]))
    return data


def dates2dic(dates):
    dic = dict()
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
                        receiver.set_next_stop([from_name_to_busStop(bus_stop_order[index + 2], bus_stops)])
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
                        receiver.set_next_stop([from_name_to_busStop(bus_stop_order[index + 2], bus_stops)])
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
    Assigns the previous bus stop(s) to the previous_stop attibute of all bus stops
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


def assign_line_number_to_bus_stops(line):
    """
    Assigns the number of the line in which the bus stop belongs to its .line attribute
    :param line type BusLine:
    """
    line_number = line.get_line_number()
    bus_stops = line.get_bus_stops()
    for bus_stop in bus_stops:
        bus_stop.set_line_number(line_number)


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



def get_next_stops(bus_stop, next_stops = []):
    """
    Create a list containing all next stops according to the bus stop given
    :param bus_stop type BusStop:
    :param next_stops type list: default []
    :return type list: [bus_stop1, ...]
    """
    while bus_stop.get_next_stop() != []:
        for stop in bus_stop.get_next_stop():
            next_stops.append(stop)
        bus_stop = bus_stop.get_next_stop()[0]
        return get_next_stops(bus_stop, next_stops)
    return next_stops


def get_previous_stops(bus_stop, previous_stops = []):
    """
    Create a list containing all previous stops according to the bus stop given
    :param bus_stop type BusStop:
    :param previous_stops type list: default []
    :return type list: [bus_stop1, ...]
    """
    while bus_stop.get_previous_stop() != [None]:
        for stop in bus_stop.get_previous_stop():
            previous_stops.append(stop)
        bus_stop = bus_stop.get_previous_stop()[0]
        return get_previous_stops(bus_stop, previous_stops)
    return previous_stops

def find_first_schedule(time, bus_stop, dates):
    """
    Finds the earliest bus according to the time given that will leave at the bus stop given
    :param time type datetime:
    :param bus_stop type BusStop:
    :param dates type list:
    :return type list: [time, time_index]
    """
    for date in dates:
        if date >= time:
            time = date
            time_index = dates.index(time)
            return [time, time_index]


def makes_trip(departure_stop, arrival_stop, departure_time, duration ="00:00", holidays = False):
    """
    Outputs the time needed to go from one stop to another
    :param departure_stop type BusStop:
    :param arrival_stop type BusStop:
    :param departure_time type str: default '00:00'
    :param duration type str: default "00:00"
    :param holidays type bool: default False
    :return type list: [arrival_stop, arrival_time, duration_of_the_trip]
    """
    departure_time = timedelta(hours = int(departure_time.split(':')[0]), minutes = int(departure_time.split(':')[1]))
    duration = timedelta(hours = int(duration.split(':')[0]), minutes = int(duration.split(':')[1]))
    next_stops = get_next_stops(departure_stop)
    previous_stops = get_previous_stops(departure_stop)

    direction = 1
    if arrival_stop not in next_stops:
        direction = -1

    # Tests if the bus has arrived
    if departure_stop != arrival_stop:

        #Tests if the bus stops are on the same line
        if departure_stop.get_line_number() == arrival_stop.get_line_number():

            # Regular time period and "go" direction
            if not holidays and direction == 1:

                departure_time, time_index = find_first_schedule(departure_time, departure_stop, departure_stop.get_regular_dates_go())
                duration += departure_stop.get_next_stop()[0].get_regular_dates_go()[time_index] - departure_time
                duration = str(duration)[:4]
                departure_stop = departure_stop.get_next_stop()[0]
                return(makes_trip(departure_stop, arrival_stop, str(departure_time)[:5], str(duration)[:5], holidays))

            # Special time and "go" direction
            elif holidays and direction == 1:
                departure_time, time_index = find_first_schedule(departure_time, departure_stop, departure_stop.get_special_dates_go())
                duration += departure_stop.get_next_stop()[0].get_special_dates_go()[time_index] - departure_time
                duration = str(duration)[:4]
                departure_stop = departure_stop.get_next_stop()[0]
                return(makes_trip(departure_stop, arrival_stop, str(departure_time)[:5], str(duration)[:5], holidays))

            # Regular time and "back" direction
            elif not holidays and direction == -1:
                departure_time, time_index = find_first_schedule(departure_time, departure_stop, departure_stop.get_regular_dates_back())
                duration += departure_time - departure_stop.get_previous_stop()[0].get_regular_dates_back()[time_index]
                duration = str(duration)[:4]
                departure_stop = departure_stop.get_previous_stop()[0]
                return(makes_trip(departure_stop, arrival_stop, str(departure_time)[:5], str(duration)[:5], holidays))

            # Special time and "back" direction
            elif holidays and direction == -1:
                departure_time, time_index = find_first_schedule(departure_time, departure_stop, departure_stop.get_special_dates_back())
                duration += departure_stop.get_previous_stop()[0].get_special_dates_back()[time_index] - departure_time
                duration = str(duration)[:4]
                departure_stop = departure_stop.get_previous_stop()[0]
                return(makes_trip(departure_stop, arrival_stop, str(departure_time)[:5], str(duration)[:5], holidays))

    return arrival_stop.get_bus_stop_name(), 'in', str(duration)[:4]

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
            locals()['line' + str(line_number) + '_stop' + str(_)].set_special_dates_back(data['we_holidays_date_back'][_])

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

    # Setting the bus.line_number
    assign_line_number_to_bus_stops(Line)

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


# Trip example :
holidays = bool(int(input('Est-ce les vacances (0/1)?\n')))
departure_stop = str(input('Departure stop :\n')).upper()
arrival_stop = str(input('Destination :\n')).upper()

for bus_stop in Line1_regular.get_bus_stops():
    if bus_stop.get_bus_stop_name() == departure_stop:
        line_number = 1
for bus_stop in Line1_special.get_bus_stops():
    if bus_stop.get_bus_stop_name() == departure_stop:
        line_number = 1
for bus_stop in Line2_regular.get_bus_stops():
    if bus_stop.get_bus_stop_name() == departure_stop:
        line_number = 2
for bus_stop in Line2_special.get_bus_stops():
    if bus_stop.get_bus_stop_name() == departure_stop:
        line_number = 2
if line_number == 1:
    if holidays:
        bus_stops = Line1_special.get_bus_stops()
    else:
        bus_stops = Line1_regular.get_bus_stops()
else:
    if holidays:
        bus_stops = Line2_special.get_bus_stops()
    else:
        bus_stops = Line2_regular.get_bus_stops()

print('What time is it ?')
hours = str(input('Hours : '))
minutes = str(input('Minutes : '))
time = hours + ':' + minutes

print('From', from_name_to_busStop(departure_stop, bus_stops).get_bus_stop_name(), 'to', makes_trip(from_name_to_busStop(departure_stop, bus_stops), from_name_to_busStop(arrival_stop, bus_stops), time, holidays = holidays)[0], makes_trip(from_name_to_busStop(departure_stop, bus_stops), from_name_to_busStop(arrival_stop, bus_stops), time, holidays = holidays)[1], makes_trip(from_name_to_busStop(departure_stop, bus_stops), from_name_to_busStop(arrival_stop, bus_stops), time, holidays = holidays)[2])