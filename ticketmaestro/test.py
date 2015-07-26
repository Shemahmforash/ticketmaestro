import event
import unittest


class TestStructure(unittest.TestCase):

    def setUp(self):
        super(TestStructure, self).setUp()
        self.ev = event.Event(1, 5, 10)

    def test_structure(self):
        self.assertTrue(isinstance(self.ev, event.Event))
        self.assertTrue(isinstance(self.ev.venue, list))
        self.assertTrue(len(self.ev.venue), 1)
        self.assertTrue(len(self.ev.venue[0]), 5)
        self.assertTrue(len(self.ev.venue[0][0]), 10)


class TestBooking(unittest.TestCase):

    def setUp(self):
        super(TestBooking, self).setUp()
        self.ev = event.Event(1, 5, 10)
        self.user_id = 123

    def test_book(self):
        self.ev.book_tickets(0, {3: [0, 1, 2]}, self.user_id)
        self.assertEqual(self.ev.bookings[0][3][0], self.user_id)
        self.assertEqual(self.ev.bookings[0][3][1], self.user_id)
        self.assertEqual(self.ev.bookings[0][3][2], self.user_id)

        # test booking outside bounds
        with self.assertRaisesRegexp(Exception, 'invalid section'):
            self.ev.book_tickets(2, {0: [0, 1, 2]}, self.user_id)

        # try to book something booked buy other user
        self.ev.book_tickets(0, {0: [5]}, self.user_id - 1)
        with self.assertRaisesRegexp(Exception, 'seat already booked'):
            self.ev.book_tickets(0, {0: [5]}, self.user_id)

    def test_buy(self):
        # buy without book raises exception
        with self.assertRaisesRegexp(Exception, 'Cannot buy without booking'):
            self.ev.buy_tickets(0, {1: [0, 1, 2]}, self.user_id)

        # valid purchase
        self.ev.book_tickets(0, {1: [0, 1, 2]}, self.user_id)
        self.ev.buy_tickets(0, {1: [0, 1, 2]}, self.user_id)

        self.assertEqual(self.ev.venue[0][1][0], 1)
        self.assertEqual(self.ev.venue[0][1][1], 1)
        self.assertEqual(self.ev.venue[0][1][2], 1)

        with self.assertRaisesRegexp(Exception, 'seat already bought!'):
            self.ev.book_tickets(0, {1: [0, 1, 2]}, self.user_id)

    def test_best_tickets(self):
        # best ticket in empty venue is [0][0][0]
        self.ev.buy_best_seats(1, self.user_id)


"""
user_id = 123

ev.book_tickets(0, {0: [0, 1, 2]}, user_id)
ev.buy_tickets(0, {0: [0, 1, 2]}, user_id)

ev.buy_best_seats(5, user_id)

ev.buy_best_seats(6, user_id)
ev.buy_best_seats(2, user_id)
"""

# ev.book_tickets(0, {1: [0, 2, 3]}, user_id)

# ev.book_tickets(0, {0: [0]}, user_id)


# ev.buy_tickets(0, {0: [0]}, user_id)
# ev.buy_tickets(0, {0: [0]}, user_id)

# ev.buy_tickets(0, Set([4]), user_id)
