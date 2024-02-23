class Passenger:
    def __init__(self, name, booking_reference, seat_number, gender, age, nationality):
        # Initialize passenger attributes
        self.name = name
        self.booking_reference = booking_reference
        self.seat_number = seat_number
        self.gender = gender
        self.age = age
        self.nationality = nationality

    # Getter and setter methods for passenger attributes
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_booking_reference(self):
        return self.booking_reference

    def set_booking_reference(self, booking_reference):
        self.booking_reference = booking_reference

    def get_seat_number(self):
        return self.seat_number

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality


class Flight:
    def __init__(self, flight_number, destination, departure_time, gate_number, status):
        # Initialize flight attributes
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.gate_number = gate_number
        self.status = status

    # Getter and setter methods for flight attributes
    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_gate_number(self):
        return self.gate_number

    def set_gate_number(self, gate_number):
        self.gate_number = gate_number

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


class AirportStaff:
    def __init__(self, name, employee_id, role, shift, department):
        # Initialize airport staff attributes
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.shift = shift
        self.department = department

    # Getter and setter methods for airport staff attributes
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department


class GateStaff(AirportStaff):
    def __init__(self, name, employee_id, role, shift, department, contact_number):
        # Initialize gate staff attributes, inheriting from AirportStaff
        super().__init__(name, employee_id, role, shift, department)
        self.contact_number = contact_number

    # Getter and setter methods for gate staff attributes
    def get_contact_number(self):
        return self.contact_number

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number


# Creating objects for Passenger, Flight, AirportStaff, and GateStaff classes
salem = Passenger("Salem Mohammed", "WF578", "Maldives", "Male", 35, "UAE")
flight = Flight("WF578", "Maldives", "2022-02-23 08:30:00", "H8", "Scheduled")
meera = AirportStaff("Meera Ahmed", "T568383", "Security Officer", "Night Shift", "Security Department")
yara = GateStaff("Yara Hassan", "F68370", "Gate Agent", "Morning Shift", "Gate Department", "05589457")

# Displaying passenger, flight, airport staff, and gate staff details
print("Passenger Details:")
print("Name:", salem.get_name())
print("Booking Reference:", salem.get_booking_reference())
print("Seat Number:", salem.get_seat_number())
print("Gender:", salem.get_gender())
print("Age:", salem.get_age())
print("Nationality:", salem.get_nationality())

print("\nFlight Details:")
print("Flight Number:", flight.get_flight_number())
print("Destination:", flight.get_destination())
print("Departure Time:", flight.get_departure_time())
print("Gate Number:", flight.get_gate_number())
print("Status:", flight.get_status())

print("\nAirport Staff Details:")
print("Name:", meera.get_name())
print("Employee ID:", meera.get_employee_id())
print("Role:", meera.get_role())
print("Shift:", meera.get_shift())
print("Department:", meera.get_department())

print("\nGate Staff Details:")
print("Name:", yara.get_name())
print("Employee ID:", yara.get_employee_id())
print("Role:", yara.get_role())
print("Shift:", yara.get_shift())
print("Department:", yara.get_department())
print("Contact Number:", yara.get_contact_number())
