import string

plain_text  = "hello world"
#para desenciptar es 26-7
shift = 7
shift %= 26

alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted_alphabet)

encrypted_text = plain_text.translate(table)

print(encrypted_text)