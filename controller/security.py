import os
# import hashlib as os
import binascii
import hashlib 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


# stored_password=hash_password("sdfsdfsdf")
# print (stored_password)
# print verify_password("be6e24addda9e72963be318f1f41f299d6e35f33500cc9f3c20a8870e834d128ca5cc2052b6e76d1f9c10c10850c24ec9403be2af16ff5616cdfd45b919f96a8bd018dad8c8d07b9953e0d7403373a2286bbd9251e541d6876a297e1ea0077c7","sdfsdfsdf")
#    