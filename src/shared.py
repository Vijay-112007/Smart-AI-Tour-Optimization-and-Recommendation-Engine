import datetime
from dateutil import parser

trip_request = {'origin': 'Nila Hostel B Block IIIT Kottayam, QM35+H33, Nechipuzhoor, Keralam 686635', 'destination': 'Kochi, Keralam', 'departure_time': '05:00 AM', 'travel_date': '16/11/2026', 'number_of_plans': 3}
trip = {'origin': {'name': 'Nila Hostel B Block IIIT Kottayam, QM35+H33, Nechipuzhoor, Keralam 686635', 'latitude': 9.7495486, 'longitude': 76.6257274}, 'destination': {'name': 'Kochi, Keralam', 'latitude': 9.9576168, 'longitude': 76.2511512}, 'departure_datetime': datetime.datetime(2026, 11, 16, 5, 0), 'preferences': {'number_of_plans': 3, 'objective': 'balanced'}}
