class vehicle:
    def __init__(self,vehicle_id,brand,price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price
        
    def display_info(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Price:", self.price)

class car(vehicle):
    def __init__(self, vehicle_id, brand, price,num_doors,fuel_type):
        super().__init__(vehicle_id, brand, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
        
    def display_car(self):
        self.display_info()
        print("Fuel_type :",self.fuel_type)
        print("Num_doors :",self.num_doors)

car1 = car(201, "Toyota", 800000, 4, "Petrol")
car2 = car(202, "Hyundai", 750000, 4, "Diesel")

car1.display_car()
car2.display_car()