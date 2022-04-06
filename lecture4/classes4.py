class Flight:
    
    counter = 1
    
    def __init__(self, origin, destination, duration):
        
        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1
        
        # Keep track of passengers.
        self.passengers = []
        
        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        
        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")
        
    def delay(self, amount):
        self.duration += amount
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        passenger.flight_id = self.id


class Passenger:
    
    def __init__(self, name):
        self.name = name
        
        
    
def main():

    # Create flight.
    flight_1 = Flight(origin="New York", destination="Paris", duration=540)
    
    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")
    
    # Add passengers.
    flight_1.add_passenger(alice)
    flight_1.add_passenger(bob)
    
    flight_1.print_info()  


if __name__ == '__main__':
    main()
        