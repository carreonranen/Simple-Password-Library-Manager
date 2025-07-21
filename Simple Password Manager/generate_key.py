from cryptography.fernet import Fernet

#Generate a key
key = Fernet.generate_key()

#Save the key to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

print("\nKey has been generated and saved to secret.key\n")
#