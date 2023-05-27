def encrypt():
    plaintext = list(input('Plaintext: ').strip().lower().replace(' ', '').replace(',', '').replace("'", '').replace('.', ''))
    len_plaintext = len(plaintext)

    count = 0
    for char in plaintext:
        if count % 2 == 0:
            if char == 'e': plaintext[count] = 'U'
            elif char == 'a': plaintext[count] = 'G'
            elif char == 'i': plaintext[count] = 'S'
            elif char == 'o': plaintext[count] = 'D'
            elif char == 'u': plaintext[count] = 'A'
            elif char == 'b': plaintext[count] = 'W'
            elif char == 'c': plaintext[count] = 'M'
            elif char == 'd': plaintext[count] = 'J'
            elif char == 'f': plaintext[count] = 'K'
            elif char == 'g': plaintext[count] = 'L'
            elif char == 'h': plaintext[count] = 'Z'
            elif char == 'j': plaintext[count] = 'X'
            elif char == 'k': plaintext[count] = 'C'
            elif char == 'l': plaintext[count] = 'V'
            elif char == 'm': plaintext[count] = 'R'
            elif char == 'n': plaintext[count] = 'E'
            elif char == 'p': plaintext[count] = 'F'
            elif char == 'q': plaintext[count] = 'T'
            elif char == 'r': plaintext[count] = 'I'
            elif char == 's': plaintext[count] = 'H'
            elif char == 't': plaintext[count] = 'O'
            elif char == 'v': plaintext[count] = 'Q'
            elif char == 'w': plaintext[count] = 'Y'
            elif char == 'x': plaintext[count] = 'N'
            elif char == 'y': plaintext[count] = 'P'
            elif char == 'z': plaintext[count] = 'B'
            else: plaintext[count] = '?'
        else:
            if char == 'e': plaintext[count] = 'B'
            elif char == 'a': plaintext[count] = 'X'
            elif char == 'i': plaintext[count] = 'F'
            elif char == 'o': plaintext[count] = 'L'
            elif char == 'u': plaintext[count] = 'R'
            elif char == 'b': plaintext[count] = 'Y'
            elif char == 'c': plaintext[count] = 'Z'
            elif char == 'd': plaintext[count] = 'A'
            elif char == 'f': plaintext[count] = 'C'
            elif char == 'g': plaintext[count] = 'D'
            elif char == 'h': plaintext[count] = 'E'
            elif char == 'j': plaintext[count] = 'G'
            elif char == 'k': plaintext[count] = 'H'
            elif char == 'l': plaintext[count] = 'I'
            elif char == 'm': plaintext[count] = 'J'
            elif char == 'n': plaintext[count] = 'K'
            elif char == 'p': plaintext[count] = 'M'
            elif char == 'q': plaintext[count] = 'N'
            elif char == 'r': plaintext[count] = 'O'
            elif char == 's': plaintext[count] = 'P'
            elif char == 't': plaintext[count] = 'Q'
            elif char == 'v': plaintext[count] = 'S'
            elif char == 'w': plaintext[count] = 'T'
            elif char == 'x': plaintext[count] = 'U'
            elif char == 'y': plaintext[count] = 'V'
            elif char == 'z': plaintext[count] = 'W'
            else: plaintext[count] = '?'
        count += 1

    if len_plaintext >= 5:
        for i in range(len_plaintext // 5):
            change = i * 5
            plaintext[0 + change], plaintext[4 + change] = plaintext[4 + change], plaintext[0 + change]
            plaintext[1 + change], plaintext[3 + change] = plaintext[3 + change], plaintext[1 + change]

    if len_plaintext >= 2:
        for i in range(len_plaintext // 2):
            change = i * 2
            plaintext[0 + change], plaintext[1 + change] = plaintext[1 + change], plaintext[0 + change]

    plaintext = "".join(plaintext)
    print('Ciphertext: ', plaintext)


def decrypt():
    ciphertext = list(input('Ciphertext: ').strip().lower())
    len_ciphertext = len(ciphertext)

    if len_ciphertext >= 2:
        for i in range(len_ciphertext // 2):
            change = i * 2
            ciphertext[0 + change], ciphertext[1 + change] = ciphertext[1 + change], ciphertext[0 + change]

    if len_ciphertext >= 5:
        for i in range(len_ciphertext // 5):
            change = i * 5
            ciphertext[0 + change], ciphertext[4 + change] = ciphertext[4 + change], ciphertext[0 + change]
            ciphertext[1 + change], ciphertext[3 + change] = ciphertext[3 + change], ciphertext[1 + change]

    count = 0
    for char in ciphertext:
        if count % 2 == 0:
            if char == 'u': ciphertext[count] = 'E'
            elif char == 'g': ciphertext[count] = 'A'
            elif char == 's': ciphertext[count] = 'I'
            elif char == 'd': ciphertext[count] = 'O'
            elif char == 'a': ciphertext[count] = 'U'
            elif char == 'w': ciphertext[count] = 'B'
            elif char == 'm': ciphertext[count] = 'C'
            elif char == 'j': ciphertext[count] = 'D'
            elif char == 'k': ciphertext[count] = 'F'
            elif char == 'l': ciphertext[count] = 'G'
            elif char == 'z': ciphertext[count] = 'H'
            elif char == 'x': ciphertext[count] = 'J'
            elif char == 'c': ciphertext[count] = 'K'
            elif char == 'v': ciphertext[count] = 'L'
            elif char == 'r': ciphertext[count] = 'M'
            elif char == 'e': ciphertext[count] = 'N'
            elif char == 'f': ciphertext[count] = 'P'
            elif char == 't': ciphertext[count] = 'Q'
            elif char == 'i': ciphertext[count] = 'R'
            elif char == 'h': ciphertext[count] = 'S'
            elif char == 'o': ciphertext[count] = 'T'
            elif char == 'q': ciphertext[count] = 'V'
            elif char == 'y': ciphertext[count] = 'W'
            elif char == 'n': ciphertext[count] = 'X'
            elif char == 'p': ciphertext[count] = 'Y'
            elif char == 'b': ciphertext[count] = 'Z'
            else: ciphertext[count] = '?'
        else:
            if char == 'b': ciphertext[count] = 'E'
            elif char == 'x': ciphertext[count] = 'A'
            elif char == 'f': ciphertext[count] = 'I'
            elif char == 'l': ciphertext[count] = 'O'
            elif char == 'r': ciphertext[count] = 'U'
            elif char == 'y': ciphertext[count] = 'B'
            elif char == 'z': ciphertext[count] = 'C'
            elif char == 'a': ciphertext[count] = 'D'
            elif char == 'c': ciphertext[count] = 'F'
            elif char == 'd': ciphertext[count] = 'G'
            elif char == 'e': ciphertext[count] = 'H'
            elif char == 'g': ciphertext[count] = 'J'
            elif char == 'h': ciphertext[count] = 'K'
            elif char == 'i': ciphertext[count] = 'L'
            elif char == 'j': ciphertext[count] = 'M'
            elif char == 'k': ciphertext[count] = 'N'
            elif char == 'm': ciphertext[count] = 'P'
            elif char == 'n': ciphertext[count] = 'Q'
            elif char == 'o': ciphertext[count] = 'R'
            elif char == 'p': ciphertext[count] = 'S'
            elif char == 'q': ciphertext[count] = 'T'
            elif char == 's': ciphertext[count] = 'V'
            elif char == 't': ciphertext[count] = 'W'
            elif char == 'u': ciphertext[count] = 'X'
            elif char == 'v': ciphertext[count] = 'Y'
            elif char == 'w': ciphertext[count] = 'Z'
            else: ciphertext[count] = '?'

        count += 1

    ciphertext = "".join(ciphertext)
    print('Decrypted text: ', ciphertext)


while True:
    decryptencrypt = input('Would you like to encrypt or decrypt?("exit" to exit): ').upper().strip()
    if 'D' in decryptencrypt:
        decrypt()
    elif 'N' in decryptencrypt:
        encrypt()
    elif 'EXIT' in decryptencrypt:
        quit()
    else:
        print('That is not a valid input.')
