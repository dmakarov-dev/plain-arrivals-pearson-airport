import datetime

# Define a class to represent flights
class Flight:
    def __init__(self, flight_number, origin, arrival_time, status):
        self.flight_number = flight_number
        self.origin = origin
        self.arrival_time = arrival_time
        self.status = status

    def __str__(self):
        return f"{self.flight_number} from {self.origin} arriving at {self.arrival_time} - {self.status}"

# Create a list of mock flights
flights = [
    Flight("AC101", "Vancouver", datetime.time(10, 30), "On Time"),
    Flight("WS205", "Calgary", datetime.time(11, 15), "Delayed"),
    Flight("DL303", "New York", datetime.time(12, 45), "On Time"),
    Flight("UA404", "Chicago", datetime.time(13, 30), "On Time"),
    Flight("AA505", "Los Angeles", datetime.time(14, 10), "Cancelled"),
]

# Display the arrivals schedule
print("Arrivals Schedule - Pearson Airport")
print("-----------------------------------")
for flight in flights:
    print(flight)
