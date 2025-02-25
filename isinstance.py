class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def info(self):
        return self.__brand
    def info(self):
        print(f"{self.brand} is of {self.model} variant")

class ElectricCar(car):
    def __init__(self,battery_size,brand,model):
        super().__init__(brand,model)
        self.battery_size=battery_size
new=ElectricCar("5000mh","tesla","S")
new.info()
mycar=car("tata","safari")
print(new.info())
print(isinstance(mycar,new))