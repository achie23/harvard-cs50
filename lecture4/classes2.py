class Flight:
    
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
    
    
def main():

    flight_1 = Flight(origin="New York", destination="Paris", duration=540)
    flight_1.print_info()
    
    flight_2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)
    flight_2.print_info()    


if __name__ == '__main__':
    main()
        