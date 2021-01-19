import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier

ch_nmbr = phonenumbers.parse(number, "CH")
print("Country Name:")
print(geocoder.description_for_number(ch_nmbr, "en"))
print("Service Provder:")
service = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service, "en"))