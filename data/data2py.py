data_file_name = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/1_Poisy-ParcDesGlaisins.txt'
data_file_name_2 = 'C:/Users/thcen/Documents/Polytech/3 - IDU3/Cours/TP/Projet/PROJ631-BusNetwork/data/2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r', encoding = 'utf-8') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic

slited_content = content.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])
