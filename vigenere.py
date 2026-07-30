import string

alphabet = string.ascii_lowercase

letter = dict(zip(alphabet, range(len(alphabet))))
reverse_letter = dict(zip(range(len(alphabet)), alphabet))

def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char in letter:
            shift = letter[key[i % key_length]]
            encrypted_char = reverse_letter[(letter[char] + shift) % 26]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        if char in letter:
            shift = letter[key[i % key_length]]
            decrypted_char = reverse_letter[(letter[char] - shift) % 26]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
            
    return decrypted_text

def main():
    plain_text = "legendary"
    key = "waitforit"
    
    encrypted_text = vigenere_encrypt(plain_text, key)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")


main()