import event
from sets import Set

ev = event.Event(5, 5)

user_id = 123

ev.book_tickets(0, Set([0, 2, 3]), user_id)


ev.book_tickets(0, Set([4]), user_id)
