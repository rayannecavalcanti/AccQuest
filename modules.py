import random
import string
from datetime import datetime, timedelta


FIRST_NAMES = ["John", "Emma", "Michael", "Sophia", "David", "Olivia", "James", "Ava"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Davis", "Rodriguez"]
GENDERS = ["Male", "Female", "Other"]
HOBBIES = ["Sports", "Reading", "Music"]
ADDRESSES = [
    "123 Main St, New York, NY",
    "456 Elm St, Los Angeles, CA",
    "789 Oak St, Chicago, IL",
    "321 Pine St, Houston, TX"
]

def first_name():
    return random.choice(FIRST_NAMES)

def last_name():
    return random.choice(LAST_NAMES)

def email():
    name = first_name().lower() + last_name().lower()
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com"])
    return f"{name}{random.randint(1, 99)}@{domain}"

def gender():
    return random.choice(GENDERS)

def mobile_number():
    return "".join(random.choices(string.digits, k=10))

def date_of_birth():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    date = start_date + timedelta(days=random_days)
    return date.strftime("%d %b %Y")

def hobbies():
    return random.choice(HOBBIES)

def current_address():
    return random.choice(ADDRESSES)



