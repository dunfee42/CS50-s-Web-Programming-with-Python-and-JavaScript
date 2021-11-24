class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron" , "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(F"Added {person} to the flight successfully")
    else:  
        print(F"Not enough room on the flight for {person}")
    