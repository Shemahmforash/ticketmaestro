import copy


class Event:

    """
    This class represents an event venue
    """

    # an array of arrays representing the venue structure
    venue = []

    # an array of arrays representing the bookings
    bookings = []

    def __init__(self, sections, rows, seats_per_row):
        for s in range(sections):
            section = []
            for r in range(rows):
                row = []
                for s in range(seats_per_row):
                    row.append(0)
                section.append(row)

            self.venue.append(section)

        # make bookings a copy of venue
        self.bookings = copy.deepcopy(self.venue)

        print('venue')
        print(self.venue)
        print('bookings')
        print(self.bookings)

    def _get_event_data(self):
        """This should call an external API or
        some persistent storage, which would give the room information"""

        pass

    def book_tickets(self, section, seats, user_id):
        """
        User books a set of seats in a specific section
        Seats - a dictionary with row: [positions]
        """

        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        for row, positions in seats.iteritems():
            # remove duplicates
            positions = set(positions)
            for position in positions:
                if (self.venue[section][row][position] == 1):
                    raise Exception('seat already bought!')

                if (self.bookings[section][row][position] and
                        self.bookings[section][row][position] != user_id):
                    raise Exception('position already booked!')

                self.bookings[section][row][position] = user_id

        print('venue')
        print(self.venue)
        print('bookings')
        print(self.bookings)

    def buy_tickets(self, section, seats, user_id):
        """ In order to buy tickets, one must book them first
        """
        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        for row, positions in seats.iteritems():
            # remove duplicates
            positions = set(positions)
            for position in positions:
                if (self.venue[section][row][position] == 1):
                    raise Exception('seat already bought!')

                if (self.bookings[section][row][position] and
                        self.bookings[section][row][position] != user_id):
                    raise Exception('position already booked by someone else!')

                # add bought info to venue and remove booked info from bookings
                self.bookings[section][row][position] = 0
                self.venue[section][row][position] = 1

        print('venue')
        print(self.venue)
        print('bookings')
        print(self.bookings)

    def buy_best_seats(self, howmany, user_id):
        tickets = self._best_seats(howmany)

        if (not tickets):
            raise Exception('No %d adjacent tickets found!' % howmany)

        self.book_tickets(tickets['section'], {
                          tickets['tickets']['row']:
                          tickets['tickets']['seats']
                          }, user_id)
        self.buy_tickets(tickets['section'], {
                         tickets['tickets']['row']:
                         tickets['tickets']['seats']
                         }, user_id)

    def buy_section_best_seats(self, section, howmany, user_id):
        tickets = self._section_best_seats(section, howmany)

        if (not tickets):
            raise Exception(
                'No %d adjacent tickets found in section!' %
                (howmany, section))

        self.book_tickets(section, {tickets['row']: tickets['seats']}, user_id)
        self.buy_tickets(section, {tickets['row']: tickets['seats']}, user_id)

    def _section_best_seats(self, section, howmany):
        if (not self.venue[section]):
            raise Exception('invalid section for venue')

        # go trough all rows in section and find n consecutive empty seats
        for row_idx, row in enumerate(self.venue[section]):
            idx = 0
            while idx < len(row):
                if [0] * howmany == row[idx:idx + howmany]:
                    return {'row': row_idx, 'seats': range(idx, idx + howmany)}

                idx += 1

        return []

    def _best_seats(self, howmany):
        for idx, section in enumerate(self.venue):

            tickets = self._section_best_seats(idx, howmany)
            print('tickets %s , section %s ' % (tickets, idx))
            if tickets:
                return {'section': idx, 'tickets': tickets}

        return {}
