import secrets
import string
import random
import argparse
from colorama import Fore

def generate_password(l):


    longitud = l

    caracteres = string.ascii_letters + string.digits + string.punctuation

    password = []

    password.append((random.choice(string.ascii_lowercase)))
    password.append((random.choice(string.ascii_uppercase)))
    password.append((random.choice(string.digits)))
    password.append((random.choice(string.punctuation)))

    while len(password) < longitud:
        password.append(secrets.choice(caracteres))

    random.shuffle(password)

    password = "".join(password)

    return password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creacion de contraseñas")
    parser.add_argument("--l", type=int, required=True, help="Especifica la longitud de la contraseña")
    args = parser.parse_args()
    longitud=args.l
    resul = generate_password(longitud)
    print(f"Password: {Fore.LIGHTGREEN_EX}{resul}")
    