class Event:

    """
    This class represents an event
    """
    venue = None

    def __init__(self, sections, rows):
        self.venue = []
        for s in range(sections):
            row = []
            for r in range(rows):
                row.append(0)
            pass
            self.venue.append(row)

        print(self.venue)

    def _get_event_data(self):
        """This should call an external API or
        some persistent storage, which would give the room information"""

        pass

    def book_tickets(self, section, positions):
        """
        User books a set of position in a specific section
        """
        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        for position in positions:
            if (self.venue[section][position] == 1):
                raise Exception('position already bought!')

            if (self.venue[section][position] == '-'):
                raise Exception('position already booked!')

            self.venue[section][position] = '-'

        print(self.venue)

    def buy_tickets(self, section, positions):
        """ In order to buy tickets, one must book them first
        """
        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        for position in positions:
            if (self.venue[section][position] == 1):
                raise Exception('position already bought!')

            if (self.venue[section][position] != '-'):
                raise Exception('position already booked!')

            self.venue[section][position] = '-'

        print(self.venue)

    def section_best_tickets(section, howmany):
        pass

    def best_tickets(howmany):
        pass
