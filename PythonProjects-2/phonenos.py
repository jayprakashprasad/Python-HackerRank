####phonenumbers
from phonenumbers import geocoder,carrier
import phonenumbers
phone_number = phonenumbers.parse("Number with country code")
print(geocoder.description_for_number(phone_number,'utf-8'))
print(carrier.name_for_number(phone_number,'utf-8'))