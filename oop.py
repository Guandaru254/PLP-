class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method")
        
