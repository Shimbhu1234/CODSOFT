import secrets
import string

def generate_password(length=12, use_symbols=True):
    if length < 8:
        raise ValueError("Password length should be at least 6")

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-="   

    pool = letters + digits
    if use_symbols:
        pool += symbols
        
    
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(digits)
    ]

    if use_symbols:
        password.append(secrets.choice(symbols))

    
    password += [secrets.choice(pool) for _ in range(length - len(password))]


    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        print("Generated Password:", generate_password(length, use_symbols))

    except ValueError:
        print("Invalid input")
