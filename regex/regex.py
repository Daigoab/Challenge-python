import re

def extract_phone_numbers(string):
    pattern = r"\d{3}\D{0,3}\d{3}\D{0,3}\d{4}"
    phone_numbers = re.findall(pattern, string)
    return phone_numbers

def extract_email_addresses(string):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses = re.findall(pattern, string)
    return email_addresses

def replace_email_addresses(string, replacement):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    new_string = re.sub(pattern, replacement, string)
    return new_string

string = "Abraham's phone number is (123) 456-7890. His email is abrahamli001@gmail.com."
phone_numbers = extract_phone_numbers(string)
email_addresses = extract_email_addresses(string)
new_string = replace_email_addresses(string, "[REDACTED]")

print("Phone Number: ", phone_numbers)
print("Email Address: ", email_addresses)
print("Original String: ", string)
print("New String: ", new_string)
