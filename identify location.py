from cgitb import text
import numbers
import phonenumbers

from phonenumbers import timezone
text = "contact us at enter your number for reference"
numbers = phonenumbers.PhoneNumberMatcher(text,"Enter your country code")
print("Users Number")
phoneNumber = phonenumbers.parse("Enter the number here")
timezone = timezone.time_zones_for_number(phoneNumber)
print(phoneNumber)
print(timezone)
for number in numbers:
    print(number)
from phonenumbers import geocoder,carrier
Carrier = carrier.name_for_number(phoneNumber,'en')
Region = geocoder.description_for_number(phoneNumber,'en')
print(Carrier)
print(Region)
valid = phonenumbers.is_valid_number(phoneNumber)
possible=phonenumbers.is_possible_number(phoneNumber)
print(valid)
print(possible)