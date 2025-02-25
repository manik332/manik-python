class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def info(self):
        return self.__brand
    def info(self):
        print(f"{self.brand} is of {self.model} variant")
    
    def fueltype(self):
        return "petrol or diesel"

class ElectricCar(car):
    def __init__(self,battery_size,brand,model):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fueltype(self):
        return "electric charge"
new=ElectricCar("5000mh","tesla","S")
new.info()
print(new.fueltype)
mycar=car("tata","safari")
print(mycar.fueltype)
print(new.info())