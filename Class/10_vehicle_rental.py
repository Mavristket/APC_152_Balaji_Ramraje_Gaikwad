class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, available=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent(self):
        if self.available:
            self.available = False
            print(self.model, "has been rented.")
        else:
            print("Vehicle is not available.")

    def calculate_charge(self, days):
        return self.rental_rate * days

    def return_vehicle(self, days):
        if self.available:
            print("This vehicle was not rented.")
        else:
            self.available = True
            if days > 0:
                print("Rental charge for", days, "day(s): Rs.", self.calculate_charge(days))
            else:
                print("Number of days must be greater than zero.")


vehicle = Vehicle("MH-12-AB-1234", "Swift", 1500)
print("Vehicle Number:", vehicle.vehicle_no)
print("Model:", vehicle.model)
print("Rental Rate per Day: Rs.", vehicle.rental_rate)
print("Available:", vehicle.available)
vehicle.rent()
days = int(input("Enter number of rental days: "))
vehicle.return_vehicle(days)
print("Available now:", vehicle.available)
