import random
import string

def generate_participation_number():
    prefix = random.choice(string.ascii_uppercase)  # Префикс буквы
    participation_number = random.randint(1000, 9999)
    return f"{prefix}{participation_number}"
