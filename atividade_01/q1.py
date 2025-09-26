ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, key):
    encrypted_message = ''
    for letter in message:
        pos = ALPHABET.find(letter)
        if pos == -1:
            encrypted_message += letter
        else:
            new_pos = pos + key
            if new_pos > 25:
                new_pos -= 26
            encrypted_message += ALPHABET[new_pos]
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ''
    for letter in encrypted_message:
        pos = ALPHABET.find(letter)
        if pos == -1:
            decrypted_message += letter
        else:
            new_pos = pos - key
            if new_pos < 0:
                new_pos += 26
            decrypted_message += ALPHABET[new_pos]
    return decrypted_message

def main():
    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Original message = " + message)
    print("Encrypted message = " + encrypted_message)
    print("Decrypted message = " + decrypted_message)

if __name__ == "__main__":
    main()