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

















    def get_au_plus_tot(self):
        """
        :return type int: duree au plus tot
        """
        return self.tot

    def get_au_plus_tard(self):
        """
        :return type int: duree au plus tard
        """
        return self.tard

    def get_number(self):
        """
        :return type int: numero de l'etape
        """
        return self.number

    def get_next_steps(self):
        """
        :return type list: liste des etapes suivantes
        """
        NextSteps = []
        for task in self.tasks['out']:
            NextSteps.append(task.get_end_step())
        return NextSteps

    def get_next_steps(self):
        """
        :return type list: liste des etapes precedente
        """
        PreviousSteps = []
        for task in self.tasks['in']:
            PreviousSteps.append(task.get_begin_step())
        return PreviousSteps

    def critique(self, chemin = []):
        """
        :return type list: Liste des noeud appartenant au chemin critique
        """
        if not len(self.tasks['out']):
            chemin.append(self.get_number())
            return chemin

        for task in self.tasks['out']:
            if task.get_end_step().tot == task.get_end_step().tard:
                chemin.append(self.get_number())
                return task.get_end_step().critique(chemin)

    def compute_au_plus_tot(self):
        """
        :return type DAG: calcule les dates au plus tot
        """
        for task in self.tasks['out']:
            if task.get_end_step().get_au_plus_tot() < task.get_duration() + self.get_au_plus_tot():
                task.get_end_step().set_AuPlusTot(task.get_duration() + self.get_au_plus_tot())
            # print(task.get_end_step().get_number(), task.get_end_step().get_au_plus_tot())
            task.get_end_step().compute_au_plus_tot()

    def compute_au_plus_tard(self):
        """
        :return type DAG: calcule les dates au plus tard
        """
        for task in self.tasks['in']:
            if task.get_begin_step().get_au_plus_tard() > self.get_au_plus_tard() - task.get_duration():
                task.get_begin_step().set_AuPlusTard(self.get_au_plus_tard() - task.get_duration())
            # print(task.get_begin_step().get_number(), task.get_begin_step().get_au_plus_tard())
            task.get_begin_step().compute_au_plus_tard()