class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.__rental_price = rental_price
        self.is_available = True

    def get_rental_price(self):
        return self.__rental_price

    def check_availability(self):
        return self.is_available

    def calculate_total_cost(self, days):
        return self.__rental_price * days

    def display_details(self):
        print(f"{self.make} {self.model}")
        print(f"Price per day: ${self.__rental_price}")
        print(f"Availability: {'Available' if self.is_available else 'Rented'}")

    def rent(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.make} {self.model} has been rented.")
        else:
            print(f"Sorry, {self.make} {self.model} is currently not available.")

    def return_vehicle(self):
        self.is_available = True
        print(f"{self.make} {self.model} has been returned and is now available.")


class Car(Vehicle):
    def display_details(self):
        print("Car Details:")
        super().display_details()


class SUV(Vehicle):
    def display_details(self):
        print("SUV Details:")
        super().display_details()


class Truck(Vehicle):
    def display_details(self):
        print("Truck Details:")
        super().display_details()


class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.__contact_number = contact_number
        self.rental_history = []

    def get_contact_number(self):
        return self.__contact_number

    def add_rental(self, reservation):
        self.rental_history.append(reservation)

    def display_rental_history(self):
        print(f"\nRental history for {self.name}:")
        if not self.rental_history:
            print("No past rentals.")
        else:
            for res in self.rental_history:
                res.display_details()


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date, days):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.days = days
        self.total_cost = self.vehicle.calculate_total_cost(days)
        self.vehicle.rent()
        self.customer.add_rental(self)

    def display_details(self):
        print("\nRental Reservation Details:")
        print(f"Customer: {self.customer.name}")
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Total Days: {self.days}")
        print(f"Total Cost: ${self.total_cost:,.2f}")


def display_item_details(item):
    print("\n--- Displaying Details ---")
    item.display_details()



car = Car("Toyota", "Corolla", 50)
suv = SUV("Honda", "CR-V", 80)
truck = Truck("Ford", "F-150", 120)
customer = Customer("Alice Johnson", "9876543210")
reservation1 = RentalReservation(customer, car, "2025-10-20", "2025-10-25", 5)
display_item_details(car)
display_item_details(reservation1)
customer.display_rental_history()
car.return_vehicle()
reservation2 = RentalReservation(customer, suv, "2025-11-01", "2025-11-05", 4)
customer.display_rental_history()
