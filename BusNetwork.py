from BusStop import *
from BusLine import *

Line1_data = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/1_Poisy-ParcDesGlaisins.txt'
Line2_data = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/2_Piscine-Patinoire_Campus.txt'

try:
    with open(Line1_data, 'r', encoding ='utf-8') as file1:
        Line1_content = file1.read()
    with open(Line2_data, 'r', encoding = 'utf-8') as file2:
        Line2_content = file2.read()
except OSError:
    # 'File not found' error message.
    print("File not found")


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0].upper()] = tmp[1:]
    return dic


# Tidying up the data for the first line
Line1_split_content = Line1_content.split("\n\n")

Line1_regular_path = Line1_split_content[0].replace('+', 'N').split(' N ')
Line1_regular_path = [name.upper() for name in Line1_regular_path]

Line1_regular_date_go = dates2dic(Line1_split_content[1])
Line1_regular_date_back = dates2dic(Line1_split_content[2])
Line1_we_holidays_path = Line1_split_content[3]
Line1_we_holidays_date_go = dates2dic(Line1_split_content[4])


# Tidying up the data for the second line
Line2_split_content = Line2_content.split("\n\n")

Line2_regular_path = Line2_split_content[0].replace('+', 'N').split(' N ')
Line2_regular_path = [name.upper() for name in Line2_regular_path]

Line2_regular_date_go = dates2dic(Line2_split_content[1])
Line2_regular_date_back = dates2dic(Line2_split_content[2])
Line2_we_holidays_path = Line2_split_content[3]
Line2_we_holidays_date_go = dates2dic(Line2_split_content[4])
Line2_we_holidays_date_back = dates2dic(Line2_split_content[5])


# Setting up the bus stops' name for the first line
for _ in range(len(Line1_regular_path)):
    globals()['line1_stop' + str(_)] = BusStop(Line1_regular_path[_])

# Creating the first line
Line1 = BusLine(1, )


# Setting up the bus stops' name for the second line
for _ in range(len(Line2_regular_path)):
    globals()['line2_stop' + str(_)] = BusStop(Line2_regular_path[_])

# Creating the second line
Line1 = BusLine(1, )