from tkinter import Toplevel


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FREQ_PORT = 'aeosrdnitmulcvpgqbfhãçjxzkw'

def count_letters(message):
    """
    Returns:
        dict: A dictionary mapping each letter from the alphabet to its
              frequency in the message.
    {
        'a': 2,
        'b': 1,
        'c': 3,
        'd': 0,
    }
    """
    letter_count = {letter: 0 for letter in ALPHABET}
    for letter in message.lower():
        if letter in ALPHABET:
            letter_count[letter] += 1
    return letter_count

def get_frequency_sequence(message):
    """
    returns: 'dcva' + ...ALFHABET
    """
    letter_count = count_letters(message)
    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

    return ''.join([letter for letter, _ in sorted_letters]) 

def break_cipher(message):
    freq_sequence = get_frequency_sequence(message)
    possible_keys = []
    
    for i in range(min(5, len(freq_sequence))): # para um i em 
        msg_char = freq_sequence[i]
        for j in range(min(5, len(FREQ_PORT))):
            port_char = FREQ_PORT[j]
            key = (ord(msg_char) - ord(port_char)) % 26
            possible_keys.append(key)
    
    # Get the most common key
    if possible_keys:
        best_key = max(set(possible_keys), key=possible_keys.count)
        return best_key
    return 0

def decrypt(encrypted_message, key):
    decrypted_message = ''
    for letter in encrypted_message.lower():
        if letter in ALPHABET:
            pos = ALPHABET.find(letter)
            new_pos = (pos - key) % 26
            decrypted_message += ALPHABET[new_pos]
        else:
            decrypted_message += letter
    return decrypted_message

if __name__ == '__main__':
    encrypted = input('Digite a mensagem criptografada: ').lower()
    key = break_cipher(encrypted)
    print(f'Chave provável: {key}')
    print(f'Mensagem decifrada: {decrypt(encrypted, key)}')