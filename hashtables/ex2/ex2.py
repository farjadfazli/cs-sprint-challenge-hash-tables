#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    route = [None] * (length - 1)
    
    hash_table = {ticket.source:ticket.destination for ticket in tickets}
    
    route[0] = hash_table["NONE"]     
    
    for i in range(1, len(route)):
        route[i] = hash_table[route[i-1]]
    
    route.append("NONE")
    
    return route