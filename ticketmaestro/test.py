import event
from sets import Set

ev = event.Event(5, 5)


ev.book_tickets(0, Set([0, 2, 3]))


ev.book_tickets(0, Set([4]))
