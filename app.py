from werkzeug.security import generate_password_hash

def main():

    hash = hash_password(input("Enter the password to be hashed: "))
    print(hash)

def hash_password(password):
    """
    Returns a password hash.
    """
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)


if __name__ == "__main__":
    main()