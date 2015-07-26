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
        self.ev.book_tickets(0, {0: [0, 1, 2]}, self.user_id)
        self.assertEqual(self.ev.bookings[0][0][0], self.user_id)
        self.assertEqual(self.ev.bookings[0][0][1], self.user_id)
        self.assertEqual(self.ev.bookings[0][0][2], self.user_id)

        with self.assertRaises(Exception):
            self.ev.book_tickets(2, {0: [0, 1, 2]}, self.user_id)


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
