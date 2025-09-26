ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def descrypt(encrypted_message, key):
    decrypted_message = ''
    for letter in encrypted_message:
        pos = ALPHABET.find(letter)

        if pos == -1:
            decrypted_message += ' '
        else:
            new_pos = pos - key
            if new_pos < 0:
                new_pos += 26

            decrypted_message += ALPHABET[new_pos]

    return decrypted_message

# alias so other code can use `decrypt` too
def decrypt(encrypted_message, key):
    return descrypt(encrypted_message, key)

if __name__ == '__main__':
    encrypted_message = input('Encrypted message: ')
    for i in range(26):
        print('Key = ' + str(i) + ' = ' + descrypt(encrypted_message, i) + '\n')