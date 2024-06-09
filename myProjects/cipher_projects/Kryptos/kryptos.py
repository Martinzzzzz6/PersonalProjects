def construct_vigenere_table(shift):
    # Construct the keyed Vigenère table based on the provided keyword
    english_alphabet = [chr(i) for i in range(65, 91)]

    # Create the Vigenère table
    vigenere_table = []
    chars_of_shift = list(shift.upper())

    for char in chars_of_shift:
        english_alphabet.remove(char)
    
    english_alphabet = chars_of_shift + english_alphabet

    for i in range(26):
        vigenere_table.append(english_alphabet[i:] + english_alphabet[:i])
    
    return vigenere_table


def transform_keystream(keystream, secret_message):
    # Transform the keystream to match the length of the secret message
    keystream_input = ""
    keystream_index = 0

    for char in secret_message:
        if char == ' ':
            keystream_input += ' '
        else:
            keystream_input += keystream[keystream_index % len(keystream)]
            keystream_index += 1
    
    return keystream_input


def encrypt(secret_message, keystream, keyword):
    vigenere_table = construct_vigenere_table(keyword)
    shifted_table = construct_vigenere_table(keyword)[0]
    secret_message = secret_message.upper()
    keystream = keystream.upper()
    secret_message_list = list(secret_message)
    keystream_input = list(transform_keystream(keystream, secret_message))
    encrypted_message = ""

    letter_to_index = {letter: index for index, letter in enumerate(shifted_table, start=0)}

    for i in range(len(secret_message_list)):
        if secret_message_list[i] == ' ':
            encrypted_message += ' '
        else:
            message_letter = secret_message_list[i]
            keystream_letter = keystream_input[i]

            row_index = letter_to_index[keystream_letter]
            column_index = letter_to_index[message_letter]

            encrypted_letter = vigenere_table[row_index][column_index]
            encrypted_message += encrypted_letter
    
    return encrypted_message


def decrypt(ciphertext,keystream, keyword):
    vigenere_table = construct_vigenere_table(keyword)
    shifted_table = construct_vigenere_table(keyword)
    keystream = keystream.upper()
    ciphertext = ciphertext.upper()
    ciphertext_list = list(ciphertext)
    keystream_input = list(transform_keystream(keystream, ciphertext))

    decrypted_message = ""

    letter_to_index = {letter: index for index, letter in enumerate(shifted_table[0])}

    for i in range(len(ciphertext_list)):
        if ciphertext_list[i] == ' ':
            decrypted_message += ' '
        else:
            row_index = letter_to_index[keystream_input[i]]
            column_index = vigenere_table[row_index].index(ciphertext_list[i])
            decrypted_message += shifted_table[0][column_index]
    return decrypted_message



def main():
    message = input("Enter the message: ").upper()
    keystream = input("Enter the keystream: ").upper()
    keyword = input("Enter the keyword of the alphabet: ").capitalize()

    choice = input("Encrypt (E) or Decrypt (D): ").upper()
    if choice == 'E':
        ciphertext = encrypt(message,keystream, keyword)
        print("Ciphertext:", ciphertext)
    elif choice == 'D':
        plaintext = decrypt(message,keystream, keyword)
        print("Plaintext:", plaintext)
    else:
        print("Invalid choice.")


flag = True
while flag:
    main()
    flag = input("Do you want to continue? (Y/N): ").upper() == 'Y'