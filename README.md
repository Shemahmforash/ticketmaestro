#Event venue
This small module represents an event venue, and allows to book and buy tickets in it.
To use it one can proceed as following:
```
    import event

    user_id = 123

    ev = event.Event(2, 5, 10)
    ev.buy_best_seats(1, user_id)

    #book and buy tickets in section 0, row 3, seats 0,1,2
    ev.book_tickets(0, {3: [0, 1, 2]}, user_id)
    ev.buy_tickets(0, {3: [0, 1, 2]}, user_id)
```
