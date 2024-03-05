import random
import string

class PhoneNumberGenerator:
    def __init__(self):
        self.country_prefixes = {'US': '+1', 'UK': '+44', 'FR': '+33', 'DK': '+45', 'IT': '+39'}
        self.country_digit_counts = {'US': 10, 'UK': 11, 'FR': 9, 'DK': 8, 'IT': 10}

    def generate_random_phone_number(self, country_code):
        prefix = self.country_prefixes.get(country_code, '+00')
        digits_count = self.country_digit_counts.get(country_code, 10)
        remaining_digits = digits_count - len(prefix)
        phone_number = prefix + ''.join(random.choices(string.digits, k=remaining_digits))
        return phone_number

def generate_random_name():
    first_names = ['John', 'Alice', 'Michael', 'Emily', 'David', 'Sarah']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_random_email(name):
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'live.com', 'apple.icloud.com']
    name_parts = name.lower().split()
    username = ''.join(name_parts) + str(random.randint(1, 100))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_contact(generator, country_code):
    name = generate_random_name()
    email = generate_random_email(name)
    phone_number = generator.generate_random_phone_number(country_code)
    return {'name': name, 'email': email, 'phone_number': phone_number}

def write_contacts_to_file(contacts):
    with open('contacts.txt', 'a') as file:
        for contact in contacts:
            file.write(f"Name: {contact['name']}, Email: {contact['email']}, Phone Number: {contact['phone_number']}\n")

def main():
    num_contacts = 5
    country_codes = ['US', 'UK', 'FR', 'IT', 'DK']  # Example country codes
    phone_number_generator = PhoneNumberGenerator()  # Instantiate the generator
    selected_country_code = random.choice(country_codes) 
    
    if random.choice(selected_country_code) == 'US':

        generate_random_contact(phone_number_generator, generate_random_contact)
         # Choose a country code before the loop
    contacts = [generate_random_contact(phone_number_generator, selected_country_code) for _ in range(num_contacts)]
    write_contacts_to_file(contacts)

if __name__ == "__main__":
    main()

