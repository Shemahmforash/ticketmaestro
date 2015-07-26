class Event:

    """
    This class represents an event
    """

    # an array of arrays representing the venue structure
    venue = None

    # an array of arrays representing the bookings
    bookings = []

    def __init__(self, sections, rows):
        self.venue = []
        for s in range(sections):
            row = []
            for r in range(rows):
                row.append(0)
            pass

            self.venue.append(row)
            # make a copy of row and append it to bookings
            self.bookings.append(list(row))

        print(self.venue)

    def _get_event_data(self):
        """This should call an external API or
        some persistent storage, which would give the room information"""

        pass

    def book_tickets(self, section, positions, user_id):
        """
        User books a set of position in a specific section
        """

        # remove duplicates
        positions = set(positions)

        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        for position in positions:
            if (self.venue[section][position] == 1):
                raise Exception('position already bought!')

            if (self.bookings[section][position] and
                    self.bookings[section][position] != user_id):
                raise Exception('position already booked!')

            self.bookings[section][position] = user_id

        print('venue')
        print(self.venue)
        print('bookings')
        print(self.bookings)

    def buy_tickets(self, section, positions, user_id):
        """ In order to buy tickets, one must book them first
        """
        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        # remove duplicates
        positions = set(positions)

        for position in positions:
            if (self.venue[section][position] == 1):
                raise Exception('position already bought!')

            # if user as already booked the position, ignore
            if (self.bookings[section][position] != user_id):
                raise Exception('position already booked by someone else!')

            # add bought info to venue and remove booked info from bookings
            self.venue[section][position] = 1
            self.bookings[section][position] = 0

        print(self.venue)

    def section_best_tickets(section, howmany):
        pass

    def best_tickets(howmany):
        pass
