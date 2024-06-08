alphabet = [chr(i) for i in range(97, 123)]

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[int(new_position)]
        else:
            encrypted_text += char
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % 26
            decrypted_text += alphabet[int((new_position))]
        else:
            decrypted_text += char
    print(f"The decoded text is {decrypted_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    
    command_line = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if command_line == 'no':
        should_continue = False
        print("Goodbye")
    else:
        should_continue = True

