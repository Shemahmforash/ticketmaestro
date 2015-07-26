import event

ev = event.Event(1, 5, 10)


user_id = 123

ev.book_tickets(0, {0: [0, 1, 2]}, user_id)
ev.buy_tickets(0, {0: [0, 1, 2]}, user_id)

ev.buy_best_seats(5, user_id)

ev.buy_best_seats(6, user_id)
ev.buy_best_seats(2, user_id)


#ev.book_tickets(0, {1: [0, 2, 3]}, user_id)

#ev.book_tickets(0, {0: [0]}, user_id)


#ev.buy_tickets(0, {0: [0]}, user_id)
#ev.buy_tickets(0, {0: [0]}, user_id)

# ev.buy_tickets(0, Set([4]), user_id)
