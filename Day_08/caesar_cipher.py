from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    length = len(alphabet)
    shift = shift % length

    def caesar(text, shift, direction):
        result = ''
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = 0
                if direction == 'encode':
                    new_position = position+shift
                    if new_position > (length-1):
                        new_position = new_position - length
                else:
                    new_position = position - shift
                result += alphabet[new_position]
            else:
                result += char
        print(f"The {direction}d text is {result}")

    if direction == 'encode' or direction == 'decode':
        caesar(text, shift, direction)
    else:
        print('You have entered unknown text...')

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == 'yes':
        caesar_cipher()
    else:
        print('Goodbye!')


print(logo)
caesar_cipher()
