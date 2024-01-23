alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

length = len(alphabet)


def encrypy(text, shift):
    encrypted_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position+shift
        if new_position > (length-1):
            new_position = new_position - length
        encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}")



def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position-shift
        decrypted_text += alphabet[new_position]
    print(f"The decoded text is {decrypted_text}")


if direction == 'encode':
    encrypy(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print('You have entered unknown text...')